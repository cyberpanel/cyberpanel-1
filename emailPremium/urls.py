from django.conf.urls import url
import views

urlpatterns = [

    url(r'^listDomains$', views.listDomains, name='listDomains'),
    url(r'^getFurtherDomains$', views.getFurtherDomains, name='getFurtherDomains'),
    url(r'^enableDisableEmailLimits$', views.enableDisableEmailLimits, name='enableDisableEmailLimits'),

    url(r'^(?P<domain>([\da-z\.-]+\.[a-z\.]{2,12}|[\d\.]+)([\/:?=&#]{1}[\da-z\.-]+)*[\/\?]?)$', views.emailLimits, name='emailLimits'),
    url(r'^changeDomainLimit$', views.changeDomainLimit, name='changeDomainLimit'),
    url(r'^getFurtherEmail$', views.getFurtherEmail, name='getFurtherEmail'),

    url(r'^enableDisableIndividualEmailLimits$', views.enableDisableIndividualEmailLimits, name='enableDisableIndividualEmailLimits'),

    url(r'(?P<emailAddress>\w+@.+)', views.emailPage, name='emailPage'),
    url(r'^getEmailStats$', views.getEmailStats, name='getEmailStats'),


    url(r'^enableDisableIndividualEmailLogs$', views.enableDisableIndividualEmailLogs, name='enableDisableIndividualEmailLogs'),
    url(r'^changeDomainEmailLimitsIndividual$', views.changeDomainEmailLimitsIndividual, name='changeDomainEmailLimitsIndividual'),
    url(r'^getEmailLogs$', views.getEmailLogs, name='getEmailLogs'),
    url(r'^flushEmailLogs$', views.flushEmailLogs, name='flushEmailLogs'),




]