#a
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")
    #b
    def override(self):
        print("I am the parrent")
    #C
    def altered(self):
        print("Parent altered()")


class child(Parent):
    pass
    
    def better(self):
        print("Anything you can do i can do better")
    #b
    def override(self):
        print("I am the child")
    #c
    def altered(self):
        print("Child before parent altered()")
        super(child, self).altered()
        print("Child after parent altered()")

dad = Parent()
son = child()

dad.implicit()
son.implicit()
son.better()
#b
dad.override()
son.override()
#c
dad.altered()
son.altered()
#d Everything thus far combined

#e
class other(object):
    def implicit(self):
        print("other implicit()")
    
    def override(self):
        print("I am the Other")
    
    def altered(self):
        print("Other altered()")

class child1(object):
    def __init__(self):
        self.other = other()

    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("child1 override()")

    def altered(self):
        print("child1 before altered")
        self.other.altered()
        print("child1 after other altered")

son = child1()
son.implicit()
son.override()
son.altered()
