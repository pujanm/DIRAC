# $HeadURL:  $
''' Command

  Base class for all commands.

'''

from DIRAC import S_OK

__RCSID__ = '$Id:  $'

class Command( object ):
  ''' 
    The Command class is a simple base class for all the commands
    for interacting with the clients
  '''

  def __init__( self, args = None, clients = None ):
    
    self.args            = ( 1 and args ) or {}      
    self.apis            = ( 1 and clients ) or {}

  def doCommand( self ):
    ''' To be extended by real commands
    '''
    
    return S_OK( { 'Result' : None } )
  
  def returnERROR( self, s_error ):
    '''
      Overwrites S_ERROR message with command name, much easier to debug
    '''
    
    s_error[ 'Message' ] = '%s %s' % ( self.__class__.__name__, s_error[ 'Message' ] )
    
    return s_error
    
    
################################################################################
#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF