#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
""" preserve case, whitespace, punctuation. escape html
"""
import webapp2
import cgi

form="""
<form method="post" action="/">
    <h2>Enter some text to encrypt</h2> 
        <label>Offset:</label>
        <input type="text" name="offset" value="%(offset)s">
        <br>
        <br>
        <textarea rows="8" cols="80" name="encrypted">%(encrypted)s</textarea>
        <div style="color: red">%(error)s</div>
    <br>
    <br>
<input type="submit">
</form>
"""

def rot13_encrypt(s):
    new_str = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                new_str += chr( ( (ord(ch) - ord('A') ) + 13) % 26 + ord('A') )
            else:
                new_str += chr( ( (ord(ch) - ord('a') ) + 13) % 26 + ord('a') )
        elif ch.isdigit():
            new_str += chr( ( (ord(ch) - ord('0') ) + 13) % 10 + ord('0') )
        else:
            new_str += ch

    return new_str

def caeser_encrypt(s, offset):
    new_str = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                new_str += chr( ( (ord(ch) - ord('A') ) + int(offset) ) % 26 + ord('A') )
            else:
                new_str += chr( ( (ord(ch) - ord('a') ) + int(offset)) % 26 + ord('a') )
        elif ch.isdigit():
            new_str += chr( ( (ord(ch) - ord('0') ) + int(offset)) % 10 + ord('0') )
        else:
            new_str += ch

    return new_str


class MainHandler(webapp2.RequestHandler):
    def write_form(self, encrypted="", offset="", error=""):
        self.response.write(form % {"encrypted": encrypted, "offset": offset, "error": error})

    def get(self):
        self.write_form()

    def post(self):
        #encrypted = rot13_encrypt( cgi.escape(self.request.get('encrypted')) )
        text = cgi.escape(self.request.get('encrypted'))
        offset = cgi.escape(self.request.get('offset'))

        if not text:
            error = "You need to input some text."
        elif not offset.isdigit():
            error = "Invalid offset \'%s\'" % offset
        else:
            error = ""
        
        if error:
            self.write_form(text, "", error)
        else:
            encrypted = caeser_encrypt(text, offset)
            self.write_form(encrypted, offset, error) 

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
