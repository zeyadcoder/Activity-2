from abc import ABC
class absclass (ABC):
    def print(self,x):
        print("passed value", x)
    def task(self):
        print("we are inside abstract class")
class subclass (absclass):
    def task(self):
     print("We are inside subclass")
obj = subclass()
obj.task()
obj.print(18)


    