# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "fms"
app_title = "Fms"
app_publisher = "New Indictrans Technology Pvt Ltd"
app_description = "Facility Management System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sagar.s@indictranstech.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fms/css/fms.css"
# app_include_js = "/assets/fms/js/fms.js"

# include js, css files in header of web template
# web_include_css = "/assets/fms/css/fms.css"
# web_include_js = "/assets/fms/js/fms.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "fms.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "fms.install.before_install"
# after_install = "fms.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fms.tasks.all"
# 	],
# 	"daily": [
# 		"fms.tasks.daily"
# 	],
# 	"hourly": [
# 		"fms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fms.tasks.weekly"
# 	]
# 	"monthly": [
# 		"fms.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "fms.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fms.event.get_events"
# }

