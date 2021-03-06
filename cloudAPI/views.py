# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cloudManager import CloudManager
import json

def router(request):
    try:
        data = json.loads(request.body)
        controller = data['controller']

        cm = CloudManager(data)

        if controller == 'verifyLogin':
            return cm.verifyLogin()
        elif controller == 'fetchWebsites':
            return cm.fetchWebsites()
        elif controller == 'fetchWebsiteDataJSON':
            return cm.fetchWebsiteDataJSON()
        elif controller == 'fetchWebsiteData':
            return cm.fetchWebsiteData()
        elif controller == 'submitWebsiteCreation':
            return cm.submitWebsiteCreation()
        elif controller == 'fetchModifyData':
            return cm.fetchModifyData()
        elif controller == 'saveModifications':
            return cm.saveModifications()
        elif controller == 'submitDBCreation':
            return cm.submitDBCreation()
        elif controller == 'fetchDatabases':
            return cm.fetchDatabases()
        elif controller == 'submitDatabaseDeletion':
            return cm.submitDatabaseDeletion()
        elif controller == 'changePassword':
            return cm.changePassword()
        elif controller == 'getCurrentRecordsForDomain':
            return cm.getCurrentRecordsForDomain()
        elif controller == 'deleteDNSRecord':
            return cm.deleteDNSRecord()
        elif controller == 'addDNSRecord':
            return cm.addDNSRecord()
        elif controller == 'submitEmailCreation':
            return cm.submitEmailCreation(request)
        elif controller == 'getEmailsForDomain':
            return cm.getEmailsForDomain(request)
        elif controller == 'submitEmailDeletion':
            return cm.submitEmailDeletion(request)
        elif controller == 'submitPasswordChange':
            return cm.submitPasswordChange(request)
        elif controller == 'fetchCurrentForwardings':
            return cm.fetchCurrentForwardings(request)
        elif controller == 'submitForwardDeletion':
            return cm.submitForwardDeletion(request)
        elif controller == 'submitEmailForwardingCreation':
            return cm.submitEmailForwardingCreation(request)
        elif controller == 'fetchDKIMKeys':
            return cm.fetchDKIMKeys(request)
        elif controller == 'generateDKIMKeys':
            return cm.generateDKIMKeys(request)
        elif controller == 'submitFTPCreation':
            return cm.submitFTPCreation(request)
        elif controller == 'getAllFTPAccounts':
            return cm.getAllFTPAccounts(request)
        elif controller == 'submitFTPDelete':
            return cm.submitFTPDelete(request)
        elif controller == 'changeFTPPassword':
            return cm.changeFTPPassword(request)
        elif controller == 'issueSSL':
            return cm.issueSSL(request)
        elif controller == 'submitWebsiteDeletion':
            return cm.submitWebsiteDeletion(request)
        elif controller == 'statusFunc':
            return cm.statusFunc()
        elif controller == 'submitDomainCreation':
            return cm.submitDomainCreation()
        elif controller == 'fetchDomains':
            return cm.fetchDomains()
        elif controller == 'submitDomainDeletion':
            return cm.submitDomainDeletion()
        elif controller == 'changeOpenBasedir':
            return cm.changeOpenBasedir()
        elif controller == 'changePHP':
            return cm.changePHP()
        elif controller == 'backupStatusFunc':
            return cm.backupStatusFunc()
        elif controller == 'submitBackupCreation':
            return cm.submitBackupCreation()
        elif controller == 'getCurrentBackups':
            return cm.getCurrentBackups()
        elif controller == 'deleteBackup':
            return cm.deleteBackup()

    except BaseException, msg:
        cm = CloudManager(None)
        return cm.ajaxPre(0, str(msg))
