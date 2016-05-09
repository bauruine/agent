import json
import urllib2

from classes.encoder import MyEncoder
from lib.httpsclientauthconnection import HTTPSClientAuthConnection


def __getBasePath(_config):
    return "/api" + _config.getApiVersion()


def getRegisterPath(_config):
    return __getBasePath(_config) + "/register"


def getSystemNotifyPath(_config, urn):
    return __getBasePath(_config) + "/system/" + urn + "/notify"


def getSystemRefreshInstalledPath(_config, urn):
    return __getBasePath(_config) + "/system/" + urn + "/refresh-installed"


def getTaskNotifyPath(_config, taskid):
    return __getBasePath(_config) + "/task/" + taskid + "/notify"


def push(_config, path, data):
    host = _config.getServerHost()
    port = _config.getServerPort()
    ca = _config.getTlsPath() + '/' + _config.getTlsCa()
    key = _config.getTlsPath() + '/' + _config.getTlsPrivKey()
    crt = _config.getTlsPath() + '/' + _config.getTlsPubCert()
    headers = {"Content-type": "application/json"}
    jsondata = json.dumps(data, cls=MyEncoder)
    answer = ''

    # print host, port, ca, key, crt, headers
    # print jsondata

    try:
        conn = HTTPSClientAuthConnection(
            host, port, key_file=key, cert_file=crt, ca_file=ca)
        conn.request('POST', path, jsondata, headers)
        response = conn.getresponse()
        print response.status, response.reason
        answer = response.read()
        conn.close()
    except Exception as e:
        print('exception!')
        print(type(e))
        print(e)

    return answer


def pushRegister(_config, sys):
    path = getRegisterPath(_config)
    return push(_config, path, sys)


def pushSystemNotify(_config, urn, sys):
    path = getSystemNotifyPath(_config, urn)
    return push(_config, path, sys)


def pushSystemRefreshInstalled(_config, urn, packages):
    path = getSystemRefreshInstalledPath(_config, urn)
    return push(_config, path, packages)


def pushTaskNotify(_config, taskid, tasknotify):
    path = getTaskNotifyPath(_config, taskid)
    return push(_config, path, tasknotify)
