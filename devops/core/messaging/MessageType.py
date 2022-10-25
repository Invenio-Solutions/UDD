'''
Created on 12-Aug-2022

@author: narayana.rallabandi
'''
import enum


@enum.unique
class MessageType(enum.Enum):
    '''
    classdocs
    '''
    EMAIL = 1
    WHATSAPP = 2
    TELEGRAM = 3
    SLACK = 4
    TEAMS = 5

    def __init__(self, params):
        '''
        Constructor
        '''
