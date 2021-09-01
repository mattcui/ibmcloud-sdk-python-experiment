"""
Examples for GlobalSearchV2
"""

import json
import os
from ibm_platform_services.global_search_v2 import GlobalSearchV2
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator

#
# This file provides an example of how to use the Global Search service.
#
# The following configuration properties are assumed to be defined:
#
# The following configuration properties are assumed to be defined in the external configuration file:
# GLOBAL_SEARCH_URL=<service url>
# GLOBAL_SEARCH_AUTHTYPE=iam
# GLOBAL_SEARCH_APIKEY=<IAM api key>
# GLOBAL_SEARCH_AUTH_URL=<IAM token service URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#

global_search_service = None

class Session():
    def __init__(self):
        self.token = os.environ.get('TOKEN')

    def client(self):
        authenticator = BearerTokenAuthenticator(self.token)
        global_search_v2 = GlobalSearchV2(authenticator=authenticator)
        global_search_v2.set_service_url('https://api.global-search-tagging.cloud.ibm.com')

        return global_search_v2
