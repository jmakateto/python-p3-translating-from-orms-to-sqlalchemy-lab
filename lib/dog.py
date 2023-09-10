from .models import Dog

def create_table(base):
   
    base.metadata.create_all()

def save(session, dog):
    #  new dog record to the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Retrieve all dog records from the database
    return session.query(Dog).all()

def find_by_name(session, name):
    # Find a dog by name in the database
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # Find a dog by ID in the database
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    # Find a dog by name and breed in the database
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    # Update the breed of a dog in the database
    dog.breed = new_breed
    session.commit()
