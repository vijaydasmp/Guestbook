import cgi
from google.appengine.api import users
import webapp2

MAIN_PAGE_HTML = """\
<html>
  <body bgcolor="#E6E6FA">
    <H1><center>Welcome to Care Pysche</center></H1>
    <form action="/sign" method="post">
      <div align = "center">
	  Checkpoints
	  <select>
          <option value="PCStartReminder"> Remind me to Start my PC </option>
          <option value="pacemaker">Recharge pacemaker</option>
          <option value="Smartlight">Switch on Smart Light</option>
          <option value="Medi">Connect to Medical Help</option>
      </select>
	  at <input type="time" name="usr_time"> 
	  <input type="submit" value="Submit">
	  </div>  
      
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write('<div align="right"> hello, ' + user.nickname() + '</div>')
        else:
            self.redirect(users.create_login_url(self.request.uri))
        self.response.write(MAIN_PAGE_HTML)
class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body><center>Alright we will send you a reminder message on your phone number at ')
        self.response.write(cgi.escape(self.request.get('usr_time')))
        self.response.write('</center></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)