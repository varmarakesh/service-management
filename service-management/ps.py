__author__ = 'rakesh.varma'
import psutil

class ps:

    results = []

    def __init__(self):
        self.results = []

    def __match(self, filter, pname):
        if pname['name']:
            return pname['name'].upper() == filter.upper()
        else:
            return False

    def getProcess(self, filter = None):
        """
        Return the list of processes as dict array
        :param filter: process filter text match
        :return:
        """
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict()
            except psutil.NoSuchProcess:
                pass

            if filter:
                if self.__match(filter, pinfo):
                    self.results.append(pinfo)
            else:
                self.results.append(pinfo)
        return self.results


#p = ps()
#print len(p.getProcess(filter=None))
#k = ps()
#print len(k.getProcess(filter='launchd'))