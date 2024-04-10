from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref= 'user')


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    image = db.Column(db.String(500), nullable= True)
    description = db.Column(db.String(100), nullable= False )
    favorites = db.relationship('Favorites', backref= 'people' )
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "description": self.description,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    image = db.Column(db.String(500), nullable= True)
    description = db.Column(db.String(100), nullable= False )
    favorites = db.relationship('Favorites', backref= 'planets' )

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "description": self.description,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable= True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def serialize(self):
        return{
            "id": self.id,
            "people_id": self.people_id,
            "planets_id": self.planets_id,
            "user_id": self.user_id,
        }
