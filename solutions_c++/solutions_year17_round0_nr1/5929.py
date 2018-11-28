#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

static inline void flip(char* status, int idx, int k) {
	for (int i = idx ; i < idx + k; ++i) {
		status[i] = status[i] == '+' ? '-' : '+';
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		char status[1000];
		int k;
		scanf("%s %d", status, &k);

		int end = strlen(status);
		int step = 0;
		int begin = 0;
		//cout << status << endl;
		for (; begin <= end - k; ++begin) {
			if (status[begin] == '+') continue;
			++step;
			flip(status, begin, k);
		}
		//cout << status << endl;
		for (; begin < end; ++begin) {
			if (status[begin] == '-') break;
		}
		if (begin != end) {
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		}
		else {
			printf("Case #%d: %d\n", i+1, step);
		}
	}
	
}
