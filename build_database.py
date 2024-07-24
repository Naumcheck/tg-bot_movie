from database.models import db, bot_users, films, wish_list, actors

db.create_tables([actors, bot_users, films, wish_list])
