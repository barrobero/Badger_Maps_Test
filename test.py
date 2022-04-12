import csv 

customer_list = []

class Customer: 
	FirstName = ""
	LastName = ""
	Street = ""
	Zip = ""
	City = ""
	Type = ""
	LastCheckInDate = ""
	Job = ""
	Phone = ""
	Company = ""

	def __init__(self, fn, ln, s, z, c, t, lci, j, p, co): # encapsulation
		self.FirstName = fn
		self.LastName = ln 
		self.Street = s # required
		self.Zip = z 	#required
		self.City = c 	#required
		self.Type = t 	
		self.LastCheckInDate = lci # required 
		self.Job = j 
		self.Phone = p 
		self.Company = co # required


