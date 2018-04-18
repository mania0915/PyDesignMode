#! /usr/binenv python
#ecoding=utf-8

import time
import threading

#这里使用方法__new__来实现单例模式
class SingleTon(object): #
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls ,'_instance'):
            orig =super(SingleTon, cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
        return cls._instance

class Bus(SingleTon):
    lock =  threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending  Signal Data ...",data)
        self.lock.release()



class VisitEntity(threading.Thread):
    my_bus=""
    name=""
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)



if  __name__=="__main__":
    for i in range(3):
        print("Entity %d begin run .."%i)
        my_entity = VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()

