from sqlalchemy import ForeignKey, create_engine, Column, INTEGER, String, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///Social_Media.db')
engine.connect()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    username = Column(String)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(INTEGER, primary_key=True)
    title = Column(String)

    user_id = Column(INTEGER, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionLocal = Session()

# user1 = User(name="Parsa Siyabi", username="parsa siyabi")
# user2 = User(name="Padmira momtazan", username="padmira momtazan")
# sessionLocal.add_all([user1, user2]),
# sessionLocal.commit()

# post1 = Post(title="My first post", user_id=3)
# post2 = Post(title="My second post", user_id=4)
# sessionLocal.add_all([post1, post2])
# sessionLocal.commit()

temp = sessionLocal.query(User).filter_by(id=4).first()
print("User: ", temp.name)
print("Posts: ", temp.posts)

