from neo4j import GraphDatabase
import time
driver = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","utkarsh"))
session = driver.session()


query="""
MATCH (N:Movie) RETURN N 
"""
results = session.run(query)
n_repeat =2
with driver.session() as session:
    total_time=0 
    for _ in range(n_repeat):
        with session.begin_transaction() as tx:
            start = time.time()
            result = tx.run(query)
            for record in results:
                print(record[0]["title"])
            tx.commit()
            total_time+=time.time()-start
"""
def create_rule():
    conflicts = find_conflicts(rule)
    if(conflicts == NULL)
        
"""
print(total_time*1000 / n_repeat)