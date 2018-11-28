#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

int T, C=1, S;
string N;

inline int ton(char c) {
	return c - '0';
}

void main2() {
	int f = S;
	for (int i = S-1; i > 0; i--) {
		if (ton(N[i-1]) > ton(N[i])) {
			N[i-1]--;
			f = i;
		}
	}

	for (int i = f; i < S; i++) {
		N[i] = '9';
	}

	printf("Case #%d: ", C++);
	f = 1;
	for (int i = 0; i < S; i++) {
		if (f && N[i] == '0') {
			continue;
		}
		f = 0;
		printf("%c", N[i]);
	}
	putchar(10);
}

int main(void) {
	scanf("%d", &T);
	while (T--) {
		cin >> N;
		S = N.size();
		main2();
	}
	return 0;
}