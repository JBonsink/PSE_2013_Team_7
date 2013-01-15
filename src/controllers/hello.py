# Author : Dexter Drupsteen
# Descrp : Contains controller logic for the hello mvc
# Changes:
# Comment:

from flask import render_template
from models.Hello import Model
from dbconnection import session

class Hello():
    def __init__(self,request):
        # create a few database items
        for model in session.query(Model):
            break
        else:
            session.add(Model("hello"))
            session.add(Model("Groep"))
            session.add(Model("2!"))
            session.commit()
        self.request = request


    def render(self):
        if self.request.form.has_key('answer'):
            if self.request.form['timerTicked']:
                return render_template('hello-timerticked.html')
            return render_template('hello.html',formString="You answered a question")
        return render_template('hello.html',formString=str(self.request.form))
