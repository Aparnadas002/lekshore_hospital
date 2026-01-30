# Copyright (c) 2026, aparna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AppointmentRecord(Document):
	def validate(self):
		# import frappe
		check_schedule = frappe.db.exists("Doctor Schedule", {
			"doctor": self.doctor,
			"appointment_data":self.appointment_date,
            "available_date": self.appointment_date,
            "time_slot": self.time_slot
        })

		#if not check_schedule:
			
			#frappe.throw("തിരഞ്ഞെടുത്ത സമയത്ത് ഡോക്ടർ ലഭ്യമല്ല. ദയവായി ഡോക്ടറുടെ ഷെഡ്യൂൾ പരിശോധിക്കുക.<br><br> (Doctor is not available at the selected time.)")
        	
		
			
        	
        
        
