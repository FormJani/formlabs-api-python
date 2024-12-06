# coding: utf-8

"""
    Formlabs Web API

     # Introduction  The Formlabs Web API provides access to Formlabs’ remote control and remote monitoring features for Internet-connected Formlabs products registered to your Dashboard account.  Some example use cases of the Dashboard Developer API: 1.  Create automated custom reports on Printer usage, material usage, and job history to gain more insights into print production 2.  More efficiently manage Printers by integrating Printer status data into existing systems (ERP/MES/custom) # Terms and Conditions -   Formlabs reserves the right to revoke or invalidate your API key at any time without warning. -   As a beta, conditions of access to the API may change in the future, access may be bundled into other future software products, etc. (we will make an effort to provide as much warning as possible) -   As a beta, the API may change at any time without warning in such a way that it may fail to support existing workflows (though we will make an effort to provide advanced notice where possible) -   You agree not to exceed the Dashboard Developer API rate limit as detailed in the \"Rate Limit\" section below. -   You will be given access to certain non-public information, software, and specifications that are confidential and proprietary to Formlabs. You will not share these outside your organization. -   By participating in this Beta you may be sharing information with Formlabs. Any information shared is governed by our Privacy Policy [https://formlabs.com/support/privacy-policy/](https://formlabs.com/support/privacy-policy/) -   The Dashboard Developer API works with Formlabs Printers that are connected to the internet and registered to Dashboard. Printers registered to Dashboard share data with Formlabs (detailed in the Data Collection section of the Privacy Policy: [https://formlabs.com/support/privacy-policy/#Data-Collection](https://formlabs.com/support/privacy-policy/#Data-Collection)). For more information about how to set up Printers and register them to Dashboard, see this link: [https://support.formlabs.com/s/article/Dashboard-Overview-and-Setup](https://support.formlabs.com/s/article/Dashboard-Overview-and-Setup)  # Technical Overview The Formlabs Dashboard Developer API is a REST HTTP API using JSON as the response data format.   Formlabs Dashboard Developer API is HTTP-based. Send a HTTP GET request to an endpoint to retrieve data from that endpoint. The integrating system should be able to make HTTP requests and process responses in JSON format.   Formlabs Dashboard Developer API uses the standard [OAuth Authentication Flow](https://tools.ietf.org/html/rfc6749#section-4.4), and all API endpoints require authentication. The access token created is valid for a day, so make sure to refresh the token regularly to maintain seamless integration with the Dashboard Developer API and ensure uninterrupted workflow.  ## Versioning  The Dashboard Developer API uses resource-based versioning, meaning API endpoints are versioned independently, rather than globally across all endpoints.  Formlabs may change the version of an endpoint to first keep in sync with product updates (could be an addition or a removal of data), in addition to any changes based on customer feedback to allow easier integrations.  Versioning can occur in the following situations:  -   The format of the response data is required to change -   The format of the response type is required to change  Any outstanding version changes or upgrades occurred on endpoints will be highlighted and documented.  ## Rate Limit  The rate of requests to the Dashboard Developer API is limited to prevent the abuse of the system. Requests from the same IP address are limited to **100 requests/second**. Requests from the same authenticated user are limited to **1500 requests/hour**. After a rate limit is exceeded, requests will return a HTTP status code of 429 with a “Retry-after” header outlining when the next request can be made.  ## Account Setup & Printer Registration  The Dashboard Developer API is only available to Formlabs.com account-holding users that are registered and have active Formlabs 3D Printer(s) associated with their accounts. If you do not have a Formlabs.com account, or you have an account but don’t have your Printers connected to it, please follow the instructions below:  1.  Sign up for a Formlabs.com account at [https://formlabs.com/dashboard/#register](https://formlabs.com/dashboard/#register) 2.  Register the Formlabs 3D Printers at [https://formlabs.com/dashboard/#setup](https://formlabs.com/dashboard/#setup). This involves connecting a Formlabs 3D Printer to the Internet and then visiting the Dashboard Registration screen on the Printer to get a registration code. Type this registration code on the Dashboard Printer registration page to complete the registration. 3.  Now the Dashboard should show your Printer’s live status, show a history of prints, etc. 4.  Visit the [Developer Tools page at](https://dashboard.formlabs.com/#developer), and create your **Application credentials** 6.  Once you have your **Client ID** and the **Client Secret**, go to the [Authentication](#tag/Authentication) section for instructions on how to get an API access token and start using the Dashboard Developer API. 

    The version of the OpenAPI document: 0.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import copy
import http.client as httplib
import logging
from logging import FileHandler
import multiprocessing
import sys
from typing import Any, ClassVar, Dict, List, Literal, Optional, TypedDict
from typing_extensions import NotRequired, Self

import urllib3


JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

ServerVariablesT = Dict[str, str]

GenericAuthSetting = TypedDict(
    "GenericAuthSetting",
    {
        "type": str,
        "in": str,
        "key": str,
        "value": str,
    },
)


OAuth2AuthSetting = TypedDict(
    "OAuth2AuthSetting",
    {
        "type": Literal["oauth2"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


APIKeyAuthSetting = TypedDict(
    "APIKeyAuthSetting",
    {
        "type": Literal["api_key"],
        "in": str,
        "key": str,
        "value": Optional[str],
    },
)


BasicAuthSetting = TypedDict(
    "BasicAuthSetting",
    {
        "type": Literal["basic"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": Optional[str],
    },
)


BearerFormatAuthSetting = TypedDict(
    "BearerFormatAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "format": Literal["JWT"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


BearerAuthSetting = TypedDict(
    "BearerAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


HTTPSignatureAuthSetting = TypedDict(
    "HTTPSignatureAuthSetting",
    {
        "type": Literal["http-signature"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": None,
    },
)


AuthSettings = TypedDict(
    "AuthSettings",
    {
        "bearerAuth": BearerAuthSetting,
    },
    total=False,
)


class HostSettingVariable(TypedDict):
    description: str
    default_value: str
    enum_values: List[str]


class HostSetting(TypedDict):
    url: str
    description: str
    variables: NotRequired[Dict[str, HostSettingVariable]]


class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param ignore_operation_servers
      Boolean to ignore operation servers for the API client.
      Config will use `host` as the base url regardless of the operation servers.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.
    :param retries: Number of retries for API requests.

    :Example:
    """

    _default: ClassVar[Optional[Self]] = None

    def __init__(
        self,
        host: Optional[str]=None,
        api_key: Optional[Dict[str, str]]=None,
        api_key_prefix: Optional[Dict[str, str]]=None,
        username: Optional[str]=None,
        password: Optional[str]=None,
        access_token: Optional[str]=None,
        server_index: Optional[int]=None, 
        server_variables: Optional[ServerVariablesT]=None,
        server_operation_index: Optional[Dict[int, int]]=None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]]=None,
        ignore_operation_servers: bool=False,
        ssl_ca_cert: Optional[str]=None,
        retries: Optional[int] = None,
        *,
        debug: Optional[bool] = None,
    ) -> None:
        """Constructor
        """
        self._base_path = "https://api.formlabs.com" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.ignore_operation_servers = ignore_operation_servers
        """Ignore operation servers
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.access_token = access_token
        """Access token
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("formlabs_web_api")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler: Optional[FileHandler] = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        if debug is not None:
            self.debug = debug
        else:
            self.__debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy: Optional[str] = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = retries
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo:  Dict[int, Any]) -> Self:
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default: Optional[Self]) -> None:
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default_copy(cls) -> Self:
        """Deprecated. Please use `get_default` instead.

        Deprecated. Please use `get_default` instead.

        :return: The configuration object.
        """
        return cls.get_default()

    @classmethod
    def get_default(cls) -> Self:
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = cls()
        return cls._default

    @property
    def logger_file(self) -> Optional[str]:
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value: Optional[str]) -> None:
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self) -> bool:
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value: bool) -> None:
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self) -> str:
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value: str) -> None:
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier: str, alias: Optional[str]=None) -> Optional[str]:
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

        return None

    def get_basic_auth_token(self) -> Optional[str]:
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self)-> AuthSettings:
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth: AuthSettings = {}
        if self.access_token is not None:
            auth['bearerAuth'] = {
                'type': 'bearer',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        return auth

    def to_debug_report(self) -> str:
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 0.8.1\n"\
               "SDK Package Version: 0.8.1".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self) -> List[HostSetting]:
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://api.formlabs.com",
                'description': "Formlabs Web API Server",
            }
        ]

    def get_host_from_settings(
        self,
        index: Optional[int],
        variables: Optional[ServerVariablesT]=None,
        servers: Optional[List[HostSetting]]=None,
    ) -> str:
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self) -> str:
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value: str) -> None:
        """Fix base path."""
        self._base_path = value
        self.server_index = None
