#from codecs import namereplace_errors
#from curses import ACS_GEQUAL
#import traceback


class Student:
    # [assignment] Skeleton class. Add your code here
    at1 = "name"
    at2= "age"
    at3 = "track" 
    at4  = "score" 
    def __init__(self,name,age,track,score):
        self.name = str(name)
        self.age = int(age)
        self.track= list(track)
        self.score = float(score)
    def change_name(self,newname):
        self.name = newname
        print("name:", self.name)


    def change_age(self,newage):
        self.age = newage
        print("age:",self.age )   
    def add_track(self,new_track): 
        self.track.append(new_track)
        print("track:" ,self.track)
    def  get_score(self,):

        print("score:", self.score)
    

Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
