import pymysql
from pymysql import cursors
import config
from sqlalchemy.sql import select
from sqlalchemy import Table, MetaData
from sqlalchemy import create_engine
import profile


# Replace these variables in a separate .py called config.py in the same directory as this script.
db_type = config.db_type
db_user = config.db_user
db_pass = config.db_pass
db_host = config.db_host
database = config.database

def engine_instance(DB_TYPE, DB_USER, DB_PASS, DB_HOST, DATABASE, DB_PORT=3306):
    if DB_PORT is not None:
        DB_HOST = "%s:%s" % (DB_HOST, DB_PORT)
    connect_string = "mysql+%s://%s:%s@%s/%s" % (DB_TYPE, DB_USER, DB_PASS, DB_HOST, DATABASE)
    engine = create_engine(connect_string)
    return engine


def init():
    try:
        new_engine = engine_instance(db_type, db_user, db_pass, db_host, database)
        connection = new_engine.connect()
        metadata = MetaData()
        t_servers = Table('cxy', metadata, autoload=True, autoload_with=new_engine)
        s = select([t_servers])
        result = connection.execute(s)
        for row in result:
            print(row)
    except Exception:
        raise
    finally:
        connection.close()

if __name__ == '__main__':
    init()
