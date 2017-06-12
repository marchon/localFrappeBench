# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class MyProjects(WebsiteGenerator):
	website = frappe._dict(
			template = "templates/includes/myprojects.html"
		)
	def validate(self):
		self.page_name = self.name.lower()
		self.dept = set_dep(self.project_guide)

@frappe.whitelist()
def set_dep(guide):
	print guide
	ins = frappe.get_doc("Instructor",guide)
	I = {}
	I['department']=ins.department
	I['instructor_name']=ins.instructor_name
	return json.dumps(I)