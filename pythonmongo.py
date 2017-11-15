######################### SIMPLE CRUD OPERATIONS PYTHON MONGODB #####################################
# DBNAME : MYTEST
# COLLECTION NAME : student
# MONGODB PORT 27017


from pymongo import MongoClient

#Connect MongoDB Client


client = MongoClient()
client = MongoClient('localhost',27017)

#Getting database
db = client['mytest']


#Menu Function to access to all functions


def startProgram():
	flag =1 

	while flag :
		option = raw_input("Select your option")
		if option == '1':
			createStudent()
		elif option =='2' :
			deleteStudent()
		elif option =='3' :
			updateStudent()
		elif option =='4' :
			readAllStudent()
		else:
			print "\nChoose the correct option\n"
	return




def createStudent():

        thename = raw_input("Enter the student name")
        prenoms = raw_input("Enter the student last name")
        age = raw_input("Enter the student age")
        likes = raw_input("Enter the student number of likes")
        mark1 = raw_input ("Enter the student marks 1")
        mark2 = raw_input ("Enter the student marks 2")
        mark3 = raw_input ("Enter the student marks 3")
        mark4 = raw_input ("Enter the student marks 4")
        marks = [mark1,mark2,mark3,mark4]

        student = {
        "name" : thename,
        "prenoms":prenoms,
        "age" : age,
        "likes" : likes,
        "marks": marks
        }

        student_id = db.student.insert_one(student)
        print student_id

        return


def readAllStudent():
        studentList = db.student.find()
        print  "\n All the student of the database are:\n "
        for studentLists in studentList:
                print studentLists

        return


def deleteStudent():
	thename = raw_input("Enter the student name you want to delete")
	db.student.delete_many({ "name": thename })
	print "\nRecords updated successfully\n"
	return


def updateStudent():
	thename = raw_input("Enter the student name you want to update")
        age = raw_input("Enter the student new age")

	db.student.update_one(
	{ "name": thename},
	{
	"$set": {
		"age": age
		}
	}
	)
	print "\nRecords updated successfully\n" 
	return

startProgram()
