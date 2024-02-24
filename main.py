from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    userq = User()
    userq.surname = "Хазивалиев"
    userq.name = "Альберт"
    userq.age = 18
    userq.position = 'ученик'
    userq.speciality = 'без спец.образования'
    userq.address = 'ул.Птрова, д.34'
    userq.email = 'xaziv@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(userq)
    db_sess.commit()
    uare = User()
    uare.surname = "Михалков"
    uare.name = "Никита"
    uare.age = 34
    uare.position = 'Актер'
    uare.speciality = 'Постановщик-сценарист'
    uare.address = 'ул.Зилюково, д.45'
    uare.email = 'sheff@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(uare)
    db_sess.commit()
    uares = User()
    uares.surname = "Булгакин"
    uares.name = "Андрей"
    uares.age = 56
    uares.position = 'Рабочий'
    uares.speciality = 'Электрик'
    uares.address = 'ул.Мазлева, д.143'
    uares.email = 'grandiof@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(uares)
    db_sess.commit()
    uarese = User()
    uarese.surname = "Родоний"
    uarese.name = "Брадин"
    uarese.age = 19
    uarese.position = 'Инженер'
    uarese.speciality = 'Технолог'
    uarese.address = 'ул.Краснеева, д.34'
    uarese.email = 'master@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(uarese)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
