
export SHELL = /bin/bash -o pipefail

.PHONY: run default
default: run

run: ./a.out
	printf '%s\n' 4 '2 1' '100 20' '200 10' '2 2' '100 20' '200 10' '3 2' '100 10' '100 10' '100 10' '4 2' '9 3' '7 1' '10 1' '8 4' | ./a.out | { x="$$(cat)";  echo "$$x";  test "$$x" = "$$(printf '%s\n' 'Case #1: 138230.076757951' 'Case #2: 150796.447372310' 'Case #3: 43982.297150257' 'Case #4: 625.176938064')"; }

./a.out: *.cpp
	g++ -Wall -Wextra -std=c++0x -pedantic -Werror $+
