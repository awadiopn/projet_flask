from crypt import methods
from email import message
from flask import Flask ,render_template, request
from wtforms import Form, StringField, TextAreaField,validators

class postForm(Form):
    title=StringField('title',[validators.length(max=100),validators.DataRequired()],render_kw={"placeholder":"Title"})
    message=TextAreaField('message', render_kw={"placeholder":"Message"})




app = Flask(__name__)


@app.route('/test',methods=['GET','POST'])
def teste():
    form=postForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.title.data,form.message.data)
    else:
        print('error')
    
    return render_template('test.html',form=form)

@app.route('/')
def home():
    return render_template('pages/home.html')















@app.route('/connexion')
def login():
    return render_template('pages/connexion.html')

@app.route('/compte')
def compte():
    return render_template('pages/compte.html')
if __name__=='__main__':
    app.run(debug=True,port=5000)