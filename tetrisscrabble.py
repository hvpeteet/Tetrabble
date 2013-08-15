# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# IMPORTS AND ENVIRONMENT
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import jinja2
import os
import webapp2
import logging
import datetime
from google.appengine.api import users
from google.appengine.ext import ndb
# import enchant

LOADER = jinja2.FileSystemLoader(os.path.dirname(__file__))
jinja_environment = jinja2.Environment(loader = LOADER)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# DATA STRUCTURES / CLASSES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# class ExampleClass(ndb.Model):
    # data
    # methods

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# HANDLERS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Dictionary = {}
Disabled = {'b':1,'c':1,'d':1,'e':1,'f':1,
            'g':1,'h':1,'j':1,'k':1,'l':1,
            'm':1,'n':1,'o':1,'p':1,'q':1, 
            'r':1,'s':1,'t':1,'u':1,'v':1,
            'w':1,'x':1,'y':1,'z':1

}

def makeDict(text):
    words = []
    text = text.lower().translate(None, '\\')
    words = text.split()
    for word in words :
        Dictionary[word] ="enabled"
        if(word in Disabled):
            Dictionary[word] = 'disabled';
    
    

def main():
  # Open the file, read it into memory as a single string.
  with open('web2.txt') as web2_file:
    words = web2_file.read()
    
  return makeDict(words)       
  
class PlayHandler(webapp2.RequestHandler):    
    def get(self): 
        #Get Values
        tile_side_len = 30
        n_tiles_wide = 8
        n_tiles_high = 10
        queue_len = 3
        #Modify Values
        template_values = {'tile_side_len' : tile_side_len, 
                            'n_tiles_wide' : n_tiles_wide, 
                            'n_tiles_high' : n_tiles_high,
                            'queue_len' : queue_len,
                            'Dictionary' : Dictionary,
                            }
        
        #Write Values
        template = jinja_environment.get_template('templates/play.html')
        self.response.out.write(template.render(template_values))
#     def post(self): 
        # respond to submitted data
        
        
        
class ProfileHandler(webapp2.RequestHandler):    
    def get(self): 
        #Get Values
        #Modify Values
        template_values = {}
        #Write Values
        template = jinja_environment.get_template('templates/profile.html')
        self.response.out.write(template.render(template_values))
       
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# SEND TO HANDLERS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
main()

routes = [
    ('.*', PlayHandler), 
#      ('/.*', ProfileHandler),

]
app = webapp2.WSGIApplication(routes, debug=True)