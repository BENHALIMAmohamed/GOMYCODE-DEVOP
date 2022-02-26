

def Create_Tree(nbrSommet: int):
    br = {}
    for i in range(nbrSommet):
        l = []
        sommeet = input("saisie sommet : ")
        points = input(
            "saisie tous les points voisin avec un espace entre eux")
        list_point = points.split()
        print(list_point)

        for i in list_point:
            print(i)
            l.append([i, int(input("saisie le poids :  "))])
        br[sommeet] = l

    return br


def Create_Heuristic(Nbr_Point: int):
    H_dic = {}
    for num_de_sommet_h in Nbr_Point:
        point = input("saisie point : ")
        print(num_de_sommet_h)
        poid = input("l'estimation' entre le target et sommet au dessus :  ")
        H_dic[num_de_sommet_h] = int(poid)
    return H_dic

    # total cost for nodes visite


def AStarSearch():
    global tree, heuristic
    closed = []             # closed nodes
    opened = [['S', 8]]     # opened nodes

    '''find the visited nodes'''
    while True:
        fn = [i[1] for i in opened]     # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # current node
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == Target:        # break the loop if node G has been found
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            # add nodes to cost dictionary
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + \
                item[1]     # calculate f(n) of current node
            temp = [item[0], fn_node]
            # store f(n) of current node in array opened
            opened.append(temp)

    '''find optimal sequence'''
    trace_node = 'G'                        # correct optimal tracing node, initialize as node G
    optimal_sequence = ['G']                # optimal node sequence
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]           # current node
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
            change the correct optimal tracing node to current node'''
            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()              # reverse the optimal sequence

    return closed, optimal_sequence


nbr_de_noeuds = int(input('donner le nombre de noeuds :     '))
nbr_de_sommets = int(input('donner le nombre de sommets :   '))

# tree = {'S': [['A', 1], ['B', 5], ['C', 8]],
#         'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
#         'B': [['S', 5], ['G', 4]],
#         'C': [['S', 8], ['G', 5]],
#         'D': [['A', 3]],
#         'E': [['A', 7]]}
tree = Create_Tree(nbr_de_noeuds)
print(tree)
sommet_de_début = input('donner les sommet de début:    ')
Target = input('donner le sommet target:   ')
heuristic = Create_Heuristic(nbr_de_sommets)
print(heuristic)
print(heuristic)
cost = {sommet_de_début: 0}
print('la sommet de début a un cout egal a =   ', cost)
if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))


# heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}
