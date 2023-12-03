from frappe import _

def get_routes():
    return [
        {"route": "/abc", "name": "About", "template": "templates/about.html"},
        {"route": "/contact", "name": "Contact", "template": "templates/contact.html"},
    ]
