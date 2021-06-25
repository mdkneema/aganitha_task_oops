class X:  # creating class X with 3 methods init, execute and shutdown
    def __init__(self):  # initializing class with object name (constructor for all three classes that extends it)
        y = self.__repr__()
        self.object = y

    def execute(self, *a): # for unknown number of arguments

        self.a = a
        print("class-->", self.__class__.__name__)  # printing class name
        print("object-->", self.__repr__())  # printing location of the object stored in ram
        if self.a != []:
            print("Arguments-->",end=" ")
            for i in self.a:
                print(i, end=" ")  # print args in single line
            print("\n")
        else:
            print('no arguments')  # if no arguments in class

        return 1

    def shutdown(self):
        print("class-->", self.__class__.__name__)
        print("object-->",self.__repr__())
class A(X): # class A extends X

    pass


class B(X): # class B extends X
    pass

class C(X): # class C extends X
    pass

#obj = A()
#obj.execute('My','Name','is','Mann')  #testing execute method that it prints all args or not

#print(obj.__repr__())


