import sys;

def triangleCenter(pt1, pt2, pt3):
    rv = [];

    rv.append ( (pt1[0] + pt2[0] + pt3[0]) / 3.0 );
    rv.append ( (pt1[1] + pt2[1] + pt3[1]) / 3.0 );

    return rv;

fNameBase = "A-small-attempt0";

fIn = file(fNameBase + ".in");
fOut= file(fNameBase + ".out", "w");

num_tests = int(fIn.readline().strip());

current_test = 1;

while current_test <= num_tests:
    trial = fIn.readline().strip().split(' ');
    num_trees = int(trial.pop(0));
    A = int(trial.pop(0));
    B = int(trial.pop(0));
    C = int(trial.pop(0));
    D = int(trial.pop(0));
    x0 = int(trial.pop(0));
    y0 = int(trial.pop(0));
    M = int(trial.pop(0));

    trees = [];
    trees.append([x0, y0]);
    i = 1;
    X = x0;
    Y = y0;
    while i < num_trees:
        X = (A * X + B) % M;
        Y = (C * Y + D) % M;
        trees.append([X, Y]);
        i += 1;

    total = 0;
    start_tree = 0;
    while start_tree < len(trees):
        second_tree = start_tree + 1;
        while second_tree < len(trees):
            if (second_tree != start_tree):
                third_tree = second_tree + 1;
                while third_tree < len(trees):
                    if (third_tree != start_tree and third_tree != second_tree):
                        center = triangleCenter(trees[start_tree], trees[second_tree], trees[third_tree]);
                        if center[0] % 1 == 0 and center[1] % 1 == 0:
                            total += 1;
                    third_tree += 1;
            second_tree += 1;
        start_tree += 1;
    fOut.write("Case #" + str(current_test) + ": " + str(total) + "\n");
    current_test += 1;


fIn.close();
fOut.close();
