from .database import *

def create_db():
    db.drop_all()
    db.create_all()

def init_db():
    create_db()

    admin = User(
        name="Enmanuel",
        lastName="Pereira",
        username="iElectro",
        email="ejose.acc@gmail.com",
        is_admin=True,
        cellphone="12345678"
    )
    admin.set_password("1234admin")
    db.session.add(admin)
    db.session.commit()