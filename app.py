from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# የፋይል ስህተትን ለማስወገድ ሙሉውን መንገድ እናገኛለን
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# የመረጃ ቋቱን እናዘጋጃለን
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'game_data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# የተጫዋችን መረጃ ለመያዝ የሚያስችል "blueprint" እንፈጥራለን
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)
    profit_per_hour = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def index():
    return "የመረጃ ቋቱ ዝግጅት ተጠናቋል። አሁን ተጠቃሚዎችን እናስገባለን!"

if __name__ == '__main__':
    with app.app_context():
        # የመረጃ ቋት ፋይሉን ለመፍጠር ይህንን እንጠቀማለን
        db.create_all()
    app.run(debug=True)
