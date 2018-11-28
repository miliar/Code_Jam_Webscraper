#include <map>
#include <vector>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>


using namespace std;

#define p(r,c) ((c) + (r) * cols)

int main() {

	int rows;
	int cols;
	int T;

	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> rows >> cols;

		vector<char> cake;
		cake.resize(rows * cols);

		for (int j = 0; j < rows * cols; j++) {
			cin >> cake[j];
			if (cake[j] == '?') {
				cake[j] = 0;
			}
		}


		for (int r = 0; r < rows; r++) {
			char cur_kid = cake[p(r,0)];
			bool started = cur_kid != 0;

			for (int c = 0; c < cols; c++) {
				if (cake[p(r,c)]) {
					cur_kid = cake[p(r,c)];

					// fill in prev cols
					if (!started) {
						started = true;
						for (int cc = c-1; cc >= 0; cc--) {
							cake[p(r,cc)] = cur_kid;
						}
					}
				} else {
					cake[p(r,c)] = cur_kid;
				}
			}
		}

		// now fill in complete rows
		{
			bool started = false;
			for (int r = 0; r < rows; r++) {
				if (started && cake[p(r,0)] == 0) {
					for (int c = 0; c < cols; c++) {
						cake[p(r,c)] = cake[p(r-1,c)];
					}
				} else if (!started && cake[p(r,0)]) {
					started = true;
					// printf("started at row %d\n", r + 1);
					for (int c = 0; c < cols; c++) {
						for (int rr = r-1; rr >= 0; rr--) {
							cake[p(rr,c)] = cake[p(r,c)];
						}
					}
					
				}
			}
		}


		// print
		printf("Case #%d:\n", i);

		for (int r = 0; r < rows; r++) {
			for (int c = 0; c < cols; c++) {
				printf("%c", cake[p(r,c)]);
			}
			printf("\n");
		}

	}
}