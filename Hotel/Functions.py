import psycopg2
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker #Run pip install sqlalchemy
from sqlalchemy import create_engine

with SSHTunnelForwarder(
    ('192.168.0.198', 22), #Remote server IP and SSH port
    ssh_username = "mikethesilver",
    ssh_password = "Pa55w0rd",
    remote_bind_address=('192.168.0.198', 5432)) as server: #PostgreSQL server IP and sever port on remote machine
        
    server.start() #start ssh sever
    print('Server connected via SSH')
    
    #connect to PostgreSQL
    local_port = str(server.local_bind_port)
    engine = create_engine('postgresql://mikethesilver:Pa55w0rd@localhost:' + local_port +'/db_for_test')

    Session = sessionmaker(bind=engine)
    session = Session()
    
    print('Database session created')
    
    #test data retrieval
    test = session.execute("SELECT * FROM users")
    for row in test:
        print(row)
    session.close()

"""
server = SSHTunnelForwarder(
    'mikethesilver-Latitude-E6540',
    ssh_username="mikethesilver",
    ssh_password="Pa55w0rd",
    remote_bind_address=('192.168.0.198', 22)
)

server.start()

print(server.local_bind_port)  # show assigned local port


with SSHTunnelForwarder(
        ('192.168.0.198',22),
        ssh_username="mikethesilver",
        ssh_password="Pa55w0rd",
        remote_bind_address=('192.168.0.198', 5432)) as server:

    print("connecting")
    print(server.local_bind_address)
    print(server.local_bind_port)
    print("connected")
    print("connecting with database")
    conn = psycopg2.connect(database="db_for_test",port=server.local_bind_port,host=server.local_bind_host)
    curs = conn.cursor()
    sql = "select * from users"
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
"""