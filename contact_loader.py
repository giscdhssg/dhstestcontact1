from google.appengine.ext import db
from google.appengine.tools import bulkloader


class Contact(db.Expando):
	''' User data model '''
	pid = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	email = db.EmailProperty(required=True)

	
class ContactLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Contact',
                                   [('pid', str),
                                    ('name', str),
									('email', str)		
                                   ])

loaders = [ContactLoader]	