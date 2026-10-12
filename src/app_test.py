from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

engine = create_engine("sqlite:///test.db")
Base.metadata.create_all(engine)  

with Session(engine) as session:
    
    session.add(User(name="علی"))
    session.commit()

    user = session.query(User).filter_by(name="علی").first()
    print(user.name)