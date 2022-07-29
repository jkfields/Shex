from platform import system
from subprocess import Popen, PIPE

class ExecutionError(Exception):
    '''Raised when Popen returns and error'''
    pass
    
    
class Shex:
    '''
    Executes a shell command catching/raising errors when encountered
    '''
    
    def __init__(self, cmd):
        self.command = cmd
        self.system = system().lower()
        self.returncode = 0
        
        
    def __repr__(self):
        return (self.system, self.cmd)
        
        
    def  __str__(self):
        return self.out or None
        
        
    def execute(self):
        try:
            proc = Popen(self.command.split(),
                         shell=False,
                         stderr=PIPE,
                         stdout=PIPE)
                         
        except OSError as ex:
            self.out = ""
            self.returncode = ex.errno
            raise RuntimeError(self.errmsg.format(self.command, str(ex)))
            
        else:
            out, err = proc.communicate()
            self.returncode = proc.returncode
            
            if self.rtncode != 0:
                self.out = ""
                err = "[Errno {0}] " + err.strip()
                raise ExecutionError(err)
                
            self.out = out
