import http
import re

from main import index, login, dologin, dologout

init = False
re_mail = None

def setreq(req):
    global re_mail
    global init

    if not init:
        re_mail = re.compile("^[a-z0-9\-_\.]+@[a-z0-9\-_\.]+$")

        req.log_error('Reinicalizace ...', http.LOG_DEBUG)
        init = True
    #endif
    
    req.re_mail = re_mail
#enddef

handlers = {
    '/'             : (http.METHOD_GET, index),
    '/login'        : (http.METHOD_GET, login),
    '/dologin'      : (http.METHOD_GET, dologin),
    '/dologout'     : (http.METHOD_GET, dologout),
}
