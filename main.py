from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('killrvideo')
rows = session.execute("SELECT * FROM videos;")
for row in rows:
    print(row.title)