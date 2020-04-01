from web import *

index = NewPage("index", title="Github Search")
index.header("Multipacations Facts", centered=True)
for i in range(1,36):
    index.text(f"{i}*{i}={i*i}")
index.start()