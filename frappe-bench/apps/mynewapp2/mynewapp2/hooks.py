# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mynewapp2"
app_title = "Random"
app_publisher = "RoyProtim"
app_description = "Testing Purpose"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "p@v.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mynewapp2/css/mynewapp2.css"
# app_include_js = "/assets/mynewapp2/js/mynewapp2.js"

# include js, css files in header of web template
# web_include_css = "/assets/mynewapp2/css/mynewapp2.css"
# web_include_js = "/assets/mynewapp2/js/mynewapp2.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mynewapp2.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["MyProjects"]

# Installation
# ------------

# before_install = "mynewapp2.install.before_install"
# after_install = "mynewapp2.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mynewapp2.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"MyProjects": "mynewapp2.mynewapp2.random.myprojects.set_dep",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"MyProjects": {
# 		"validate": "mynewapp2.mynewapp2.random.myprojects.set_dep",
		
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mynewapp2.tasks.all"
# 	],
# 	"daily": [
# 		"mynewapp2.tasks.daily"
# 	],
# 	"hourly": [
# 		"mynewapp2.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mynewapp2.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mynewapp2.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mynewapp2.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mynewapp2.event.get_events"
# }
fixtures = ["Custom Field","Custom Script"]
