import sys
import pycurl
import base64
from pysdee import idsmxml
from time import sleep

ip = "the.ip.add.ress"
sdeeUrl = "https://$ip/cgi-bin/sdee-server"
sdeeUser = "username"
sdeePassword = "password"
# a change

def getSubscription(url, user, password):
    "Establishes the re-usable session to the IPS module"
#	assemble the URL
#	connect and get a result
#	store the subId


def parseEvents():
    "Examines and parses out the returned XML into event fields"


def getEvents():
    "Gets events using an established subscriptionId"
#	assemble the URL
#	consider how many to get
#	if $subId exists get next events in subscription
#		connect and get a result
#		getSubscription()
#		connect and get first results in subscription
#	endif
#	parseEvents()
