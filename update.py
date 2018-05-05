import datetime
import MalwareDetection2 as MD
import pickle
import os
now = datetime.datetime.now()

def updating_the_date():
    
    
    string=str(now.month)
    open('dateandtime.pkl','wb').write(pickle.dumps(now))

def update():
    MD.learning()
    updating_the_date()


def compare():

    f=pickle.loads(open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'dateandtime.pkl'),'rb').read())
    #print(f.month)
    #string=f.readline()
    #year=int(string[2]+string[3])
    
    #month=int(string[5]+string[6])
    
    #datetime_object = datetime.datetime.strptime(string, '%Y/%m/%d %H:%M')
    
    if (f.month- now.month)>=1:
        print ("!")
        update()
        updating_the_date()
    #print("Arjun")


def driver():
    compare()

"""
print
print "Current date and time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

print
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")
"""
