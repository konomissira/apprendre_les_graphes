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

def parcours_en_profondeur(graph, node, visited=[]):
    print("Visiting...", node)
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            parcours_en_profondeur(graph, neighbor, visited)

parcours_en_profondeur(general, "Robert")