import pulp


def knapsack(objs, weights, knapweight):

    # x = 1 if item in the knapsack
    # x = 0 otherwise
    # x is a vector of length = available items

    my_lp_problem = pulp.LpProblem('Knapsack', pulp.LpMaximize)
    print
    xs = [pulp.LpVariable("x{}".format(i+1), cat="Binary") for i in range(len(objs))]
    print(xs)

    # add objective
    total_prof = sum(x * obj for x, obj in zip(xs, objs))
    my_lp_problem += total_prof

    # add constraint
    total_weight = sum(x * w for x, w in zip(xs, weights))
    my_lp_problem += total_weight <= knapweight

    print(my_lp_problem)

    my_lp_problem.solve()
    print(pulp.LpStatus[my_lp_problem.status])

    for variable in my_lp_problem.variables():
        print("{} = {}".format(variable.name, variable.varValue))

    print(pulp.value(my_lp_problem.objective))

if __name__ == '__main__':
    objs = [8,11,9,12,14,10,6,7,13]
    weights = [0, 1, 1,1, 0,0,1, 1,1]
    knapweight = 16
    knapsack(objs, weights, knapweight)
