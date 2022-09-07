# 1. Use a dict and get len
# 2. Get key of max freq

# Add node_id to visited
# Get node
# Iterate through children
# Recurse with (child, visited)
import requests
from collections import defaultdict


def call_api(node_id):
    url = f"https://nodes-on-nodes-challenge.herokuapp.com/nodes/{node_id}"
    response = requests.get(url)
    json_obj = response.json()
    return json_obj[0]


def traverse(node_id, visited):
    visited[node_id] += 1
    node = call_api(node_id)

    for child_node_id in node["child_node_ids"]:
        traverse(child_node_id, visited)

    return visited


visited = defaultdict(int)
node_id = "089ef556-dfff-4ff2-9733-654645be56fe"
traverse(node_id, visited)
# 1
print("Unique ids ", len(visited.keys()))  # 30
# 2
most_common_node_id = max(visited, key=visited.get)
print("Most common", most_common_node_id)  # a06c90bf-e635-4812-992e-f7b1e2408a3f
