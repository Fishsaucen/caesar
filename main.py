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
import webapp2

form="""
<form method="post">
    <h2>Enter some text to ROT13</h2> 
    <br/>
        <textarea rows="8" cols="80" name="rot13" value="%(rot13)s">
        </textarea>
        <div style="color: red">%(error)s</div>
    <br>
    <br>
<input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, rot13="", error=""):
        self.response.write(form % {"rot13": rot13, "error": error})

    def get(self):
        self.write_form()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
