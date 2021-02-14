class Error(Exception):
    'to raise a user defined errors'
    pass
class ReCheckPassword(Error):
    'raise when given passcode is wrong'
    pass

class ReCheckUserName(Error):
    'raise when given username is wrong'
    pass