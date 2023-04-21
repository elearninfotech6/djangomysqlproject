class abc:
    def __init__(self,name,rno):
        self.__name=name
        self.__rno=rno
    def m(self):
        print(self.__name)
        print(self.__rno)
obj=abc('a',1001)
print(obj.__name)
obj.m()
