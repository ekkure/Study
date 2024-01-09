class complex:
    def __init__(self, realpart, imagpart):
        self.x = realpart
        self.i = imagpart
    #带 __的是私有属性或者方法
    #__fun__ 代表的是，类中的专有属性，类似于c++中的运算符重载 
    #也可以继承 class son(father):
    #之后可以使用父类的init方法初始化
    #def __init__(self, x, y):
        #  father.__init__(self, x, y)
        

x = complex(33, 22)

print(x.x, x.i)