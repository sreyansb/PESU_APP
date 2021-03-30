#admin table will be ID,email(1* key)

from key_generator.key_generator import generate
import mysql.connector

class Admin:
	def __init__(self, email = ""):
		# start database connection
		self.db_conn = mysql.connector.connect(
			host = "localhost",
			port = 3306,
			user = "root",
			password = "root",
			database = "pesuapp"
		)
		# get details from database
		cur = self.db_conn.cursor()
		q = "SELECT id, name FROM admin WHERE email = %s"
		cur.execute(q, (email,))
		res = cur.fetchone()
		# update admin attributes from database
		self.ID = res[0]
		self.email = email
		self.name = res[1]
	
	def AddStudent(self):
		pass

	def EditStudent(self):
		pass

	def AddFaculty(self):
		pass

	def EditFaculty(self):
		pass

	def AddCourse(self):
		pass

	def EditCourse(self):
		pass

	def AddAnnouncement(self):
		pass

	def AssignFacultyToCourse(self):
		pass

	def SendAnnouncement(self):
		pass

	def __repr__(self):
		return "\nADMIN:\nID = {0}\nEmail = {1}\nName = {2}".format(self.ID, self.email, self.name)

A1 = Admin("sahith02@yahoo.com")
print(A1)