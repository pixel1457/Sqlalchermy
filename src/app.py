from unicodedata import name

from sqlalchemy import create_engine, Column, INTEGER, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///digishop.db')
engine.connect()

Base = declarative_base()


class User(Base):
    __tablename__ = "userInfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


Base.metadata.create_all(engine)


class Product(Base):
    __tablename__ = "productInfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionLocal = Session()

# |----------------------------------------------------------

# user1 = User(name="Parsa", address="Ahwaz", email="siyabiparsa@gmail.com")
# user2 = User(name="Padmira", address="Tehran", email="padmira@gmail.com")

# sessionLocal.add(user1)
# sessionLocal.add(user2)
# sessionLocal.commit()

# user3= User(name="Amir", address="Ahwaz", email="amir@gmail.com")
# user4 = User(name="mmad", address="Tehran", email="mmad@gmail.com")
# sessionLocal.add_all([user3, user4])
# sessionLocal.commit()

# users = sessionLocal.query(User).all()
# print(users)
# for item in users:
#     print("name: ", item.name)
#     print("address: ", item.address)
#     print("email: ", item.email)
#     print("----------------------------")

# |----------------------------------------------------------


# product1 = Product(name="Laptop", price=1000.0, description="A high-performance laptop.")
# product2 = Product(name="Smartphone", price=500.0, description="A latest model smartphone.")
# product3 = Product(name="Headphones", price=150.0, description="Noise-cancelling headphones.")
# product4 = Product(name="Smartwatch", price=200.0, description="A smartwatch with fitness tracking features.")

# sessionLocal.add(product1)
# sessionLocal.add(product2)
# sessionLocal.add(product3)
# sessionLocal.add(product4)

# sessionLocal.commit()

# products = sessionLocal.query(Product).all()
# for item in products:
#     print("name: ", item.name)
#     print("price: ", item.price)
#     print("description: ", item.description)
#     print("----------------------------")

# |----------------------------------------------------------

# temp_user = sessionLocal.query(User).filter_by(name="Parsa").first()
# if temp_user:
#     print("User found:")
#     print("Name:", temp_user.name)
#     print("Address:", temp_user.address)
#     print("Email:", temp_user.email)
#     print("----------------------------")

# temp_product = sessionLocal.query(Product).filter_by(name="Laptop").first()
# if temp_product:
#     print("Product found:")
#     print("Name:", temp_product.name)
#     print("Price:", temp_product.price)
#     print("Description:", temp_product.description)
#     print("----------------------------")

# |----------------------------------------------------------

# temp_user = sessionLocal.query(User).filter(User.name.like("%Parsa%")).all()
# for item in temp_user:
#     print("name: ", item.name)
#     print("address: ", item.address)
#     print("email: ", item.email)
#     print("----------------------------")
# |----------------------------------------------------------

# temp_product = sessionLocal.query(Product).filter(Product.price > 1000.0).all()

# for item in temp_product:
#     print("name: ", item.name)
#     print("price: ", item.price)
#     print("description: ", item.description)
#     print("----------------------------")

# temp_product = sessionLocal.query(Product).filter(Product.name.like("%Laptop%")).all()

# for item in temp_product:
#     print("name: ", item.name)
#     print("price: ", item.price)
#     print("description: ", item.description)
#     print("----------------------------")

# |----------------------------------------------------------

# user = sessionLocal.query(User).filter_by(id=1).first()

# user.name = "Parsa Siyabi"
# user.address = "Ahwaz, Iran"
# user.email = "parsa.siyabi@example.com"

# sessionLocal.commit()

# |----------------------------------------------------------

# if user != None:
#     sessionLocal.delete(user)
#     sessionLocal.commit()
#     print("User deleted successfully.")

# |----------------------------------------------------------

product = sessionLocal.query(Product).filter(Product.price > 1000.0).first()

if product:
    sessionLocal.delete(product)
    sessionLocal.commit()
    print("Product deleted successfully.")
