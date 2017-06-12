from __future__ import unicode_literals
import frappe

def get_context(context):
	context.instructors = frappe.db.sql("select * from `tabInstructor`", as_dict=True)