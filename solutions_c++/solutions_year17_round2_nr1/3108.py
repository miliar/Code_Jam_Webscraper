
export SHELL = /bin/bash -o pipefail

.PHONY: run default
default: run

run: ./a.out
	printf '%s\n' 3 '2525 1' '2400 5' '300 2' '120 60' '60 90' '100 2' '80 100' '70 10' | ./a.out | { x="$$(cat)";  echo "$$x";  test "$$x" = "$$(printf '%s\n' 'Case #1: 101.000000' 'Case #2: 100.000000' 'Case #3: 33.333333')"; }

./a.out: *.cpp
	g++ -Wall -Wextra -std=c++0x -pedantic -Werror $+
