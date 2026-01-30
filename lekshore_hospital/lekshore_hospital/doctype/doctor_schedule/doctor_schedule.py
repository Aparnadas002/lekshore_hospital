# Copyright (c) 2026, aparna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DoctorSchedule(Document):
	def validate(self):
		# import frappe
		if frappe.db.exists("Doctor Schedule",{
		"doctor_name": self.doctor_name,
        "available_date": self.available_date,
        "time_slot": self.time_slot,
        "name": ["!=", self.name]
		}):
		   frappe.throw("This doctor already has a schedule for the selected date and time!")
			

    
    
        
        

