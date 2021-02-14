import os
import os.path
import json

path = "videos"

videos = [os.path.join(path, f) for f in os.listdir(path)]

objs = [
    (os.path.basename(p).split(" ")[0], {"src": p, "is_choosen": False}) for p in videos
]

output = dict(objs)

print(json.dumps(output))
