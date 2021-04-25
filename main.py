from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Login_Form(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(),Email()])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.config['SECRET_KEY'] = "Very Secret Key"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data == "admin@email.com" and form.password.data == "123456789":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)