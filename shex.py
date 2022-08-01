from platform import system
from subprocess import Popen, PIPE

class ExecutionError(Exception):
    '''Raised when Popen returns an error'''
    pass
    
    
class Shex:
    '''
    Executes a shell command catching/raising errors when encountered
    '''
    self.errmsgs = { "OSError":  ":( uh oh! \"{0}\" failed to execute. The error was \"{1}\".",
                     "CmdError": ":( uh oh! [Errno {0}] {1}",
                   }
    
    def __init__(self, cmd):
        self.command = cmd
        self.system = system().lower()
        self.returncode = 0
        
        
    def __repr__(self):
        return (self.system, self.command)
        
        
    def  __str__(self):
        return self.out or None
        
        
    def execute(self):
        self.out = ""
        
        try:
            proc = Popen(self.command.split(),
                         shell=False,
                         stderr=PIPE,
                         stdout=PIPE)
                         
        except OSError as ex:
            # update the returncode from the OSError
            self.returncode = ex.errno
            
            _msg = self.errmsgs.get("OSError")
            raise RuntimeError(_msg.format(self.command, str(ex)))
            
        else:
            # get stdout and stderr
            _out, _err = _proc.communicate()
            
            # return code from the command executed
            self.returncode = _proc.returncode
            
            # if command execution resulted in an error, raise it
            if self.returncode != 0:
                _msg = self.errmsgs.get("CmdError")
                raise ExecutionError(_msg.format(self.returncode, _err.strip()))
            
             # successful execution
            self.out = _out
