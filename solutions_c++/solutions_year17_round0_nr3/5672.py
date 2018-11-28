#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <queue>
#include <algorithm>
using namespace std;
priority_queue<int>myQ;
int main() {
	FILE* fi;
	fi = fopen("input.txt", "r");
	FILE* fo;
	fo = fopen("output.txt", "w");
	int T, N, M, tmp, left, right;
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%d%d", &N, &M) == EOF;
		myQ.push(N);
		while (M--) {
			right = myQ.top() / 2;
			left = (myQ.top() - 1) / 2;
			myQ.pop();
			myQ.push(right);
			myQ.push(left);
		}
		while (!myQ.empty()) {
			myQ.pop();
		}
		fprintf(fo, "Case #%d: %d %d\n", t, right, left);
	}
	fclose(fo);
	fclose(fi);
	return 0;
}