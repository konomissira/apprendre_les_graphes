from collections import deque

print()
general = {}

general['Robert'] = ['William', 'Marta', 'John']
general['William'] = ['Amy']
general['Amy'] = ['Steve', 'kim']
general['Steve'] = []
general['kim'] = []
general['Marta'] = []
general['John'] = ['Alison', 'Jack']
general['Alison'] = []
general['Jack'] = ['Julia', 'Madison']
general['Julia'] = []
general['Madison'] = []

#print(general['John'])

'''
    def parcours_en_largeur(graph, starter):
    to_visit = deque()
    to_visit.appendleft(starter)
    visited = [starter]

    while to_visit:
        node = to_visit.popleft()
        print("Visitin...", node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                to_visit.appendleft(neighbor)
                visited.append(neighbor)
    print(visited)
'''

def parcours_largeur(graph, starter):
    to_visit = deque()
    to_visit.appendleft(starter)
    visited = [starter]

    while to_visit:
        node = to_visit.pop()
        print("Visiting...", node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                to_visit.appendleft(neighbor)
                visited.append(neighbor)
                
    print(visited)

#parcours_en_largeur(general, "Robert")
parcours_largeur(general, "Robert")