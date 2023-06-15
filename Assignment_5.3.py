# Challenge 3: Implement the Complete Student Class

class Student:

    def setName(self, Name):
        self.Name = Name

    def getName(self):
        return self.Name
    
    def setRollNumber(self, RollNumber):
        self.RollNumber = RollNumber

    def getRollNumber(self):
        return self.RollNumber
    
Student1 = Student()
Student1.setName('Shubham Wagh')
Student1.setRollNumber('EN-2015/77')
print('Student Name : ',Student1.getName())
print('Student Roll Number : ',Student1.getRollNumber())

