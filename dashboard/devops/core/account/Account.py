'''
Created on 14-Aug-2022

@author: narayana.rallabandi
'''
import json
from devops.core.utils import SchemaValidators

class Accout(object):
    '''
    classdocs
    This class represents the base event
    It contains the attributes and a payload object
    The attributes section will talk about the payload type or
    its the metadata about the payload
    '''

    def __init__(self, parameters):
        '''
        Constructor
        '''

