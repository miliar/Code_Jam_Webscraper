from contextlib import contextmanager


@contextmanager
def in_out(problem, size):
    """
    gcj_context.py
    Beta work.
    Created by Robert King
    https://plus.google.com/107945104877181936322/

    "It works on my machine"

    Approximately how to get it working:

    1) install the command line tool:
    https://code.google.com/p/codejam-commandline/

    2) C:\Users\robert\code\play\codejam\codejam-commandline-1.2-beta1>python gcj_clear_contest.py

    3) Update config\user_config.py note the password is an application specific password from gmail:

    {
    'host'                : 'code.google.com',
    'user'                : 'youraccount@gmail.com',
    'data_directory'      : './source',
    'input_name_format'   : '{problem}-{input}-{id}.in',
    'output_name_format'  : '{problem}-{input}-{id}.out',
    'source_names_format' : ['{problem}-{input}-{id}.py'],
    'password'            : "qwerppjjjjiiasdf"
    }

    4) replace 1460488 with the id of whatever contest you want (found in the contest dashboard url):
     C:\Users\robert\code\play\codejam\codejam-commandline-1.2-beta1>python gcj_init_contest.py 1460488

    5) create the folder C:\Users\robert\code\play\codejam\codejam-commandline-1.2-beta1\source

    5a) make sure the "source" folder is empty of solutions from previous contests to avoid bugs.

    for the following examples I'll use B.y (although it could be A.py or C.py etc)

    6) to solve problem B, inside the source folder, create file B.py (in general for problem X make X.py)

    7) inside B.py, create your solution:

from gcj_context import in_out, test_in_out


def solve_test_case(data):
    stuff = next(data)
    return "my_answer_from_stuff"


def main():
    #with test_in_out() as (in_file, out_file):
    with in_out("B", "small") as (in_file, out_file):
        data = (line.strip() for line in in_file)
        test_cases = int(next(data))
        for case in range(1, test_cases + 1):
            answer = solve_test_case(data)
            out_file.write("Case #{}: {}\n".format(case, answer))
            print "solved {} (I hope)".format(case)


main()



    8) save gcj_context.py to the source folder .\source\gcj_context.py

    9) from the folder "codejam-commandline-1.2-beta1" (as your working directory), type "python source\B.py"
    """
    problem = problem.upper()
    size = size.lower()
    import os
    from time import sleep
    from functools import partial
    join = partial(os.path.join, "source")
    attempt = 0
    existing_attempts = set(os.listdir("source"))
    while True:
        name_solution = "{}-{}-{}.py".format(problem, size, attempt)
        name_in = "{}-{}-{}.in".format(problem, size, attempt)
        name_out = "{}-{}-{}.out".format(problem, size, attempt)
        if existing_attempts.isdisjoint(set([name_solution, name_in, name_out])):
            print "using " + " & ".join([name_solution, name_in, name_out])
            break
        attempt += 1

    with open(join("gcj_context.py")) as gcj_context_file:
        code = gcj_context_file.read()
    with open(join(problem+".py")) as code_file:
        code += code_file.read()
    with open(join(name_solution), 'w') as submitted_code:
        submitted_code.write(code)

    os.system("python gcj_download_input.py {} {} {}".format(problem, size, attempt))
    with open(join(name_in)) as in_file, open(join(name_out), 'w') as out_file:
        yield in_file, out_file
    os.system("python gcj_submit_solution.py {} {} {}".format(problem, size, attempt))
    sleep(3)
    print "getting status.."
    os.system("python gcj_get_status.py")

@contextmanager
def test_in_out(name_in="in.txt", name_out="out.txt"):
    import os
    from functools import partial
    join = partial(os.path.join, "source")
    print "Running Test from {} to {}".format(name_in, name_out)
    with open(join(name_in)) as in_file, open(join(name_out), 'w') as out_file:
        yield in_file, out_file
    print "test complete, check {}".format(name_out)
    #feel free to add a diff tool to compare between out.txt and sample_out.txtfrom gcj_context import in_out, test_in_out

def solve(data):
    rows = [next(data) for i in range(4)]
    cols = zip(*rows)
    for r in rows:
        if r.count("X") == 3:
            if "T" in r:
                return "X won"
        elif r.count("X") == 4:
            return "X won"
        elif r.count("O") == 3:
            if "T" in r:
                return "O won"
        elif r.count("O") == 4:
            return "O won"
    for r in cols:
        if r.count("X") == 3:
            if "T" in r:
                return "X won"
        elif r.count("X") == 4:
            return "X won"
        elif r.count("O") == 3:
            if "T" in r:
                return "O won"
        elif r.count("O") == 4:
            return "O won"
    print rows
    diags = [[i[0][0], i[1][1], i[2][2], i[3][3]] for i in (rows, rows[::-1])]
    for r in diags:
        if r.count("X") == 3:
            if "T" in r:
                return "X won"
        elif r.count("X") == 4:
            return "X won"
        elif r.count("O") == 3:
            if "T" in r:
                return "O won"
        elif r.count("O") == 4:
            return "O won"
    if any("." in r for r in rows):
        return "Game has not completed"
    else:
        return "Draw"

def main():
    #with test_in_out() as (in_file, out_file):
    with in_out("A", "large") as (in_file, out_file):
        data = (line.strip() for line in in_file if line.strip())
        test_cases = int(next(data))
        for case in range(1, test_cases + 1):
            answer = solve(data)
            out_file.write("Case #{}: {}\n".format(case, answer))
            print "solved {} (I hope)".format(case)


main()

