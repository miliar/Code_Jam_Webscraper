#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <deque>
#include <queue>
#include <functional>
#include <string>
#define FLIP(a){(a=='+')? '-':'+'}

using namespace std;

string solve(char *S, int K) {
	bool solved = true;
	int pos = 0;
	int count = 0;
	int length = strlen(S);
	while (pos != length - K + 1) {
		if (S[pos] == '-') {
			for (int i = pos; i < pos+K; ++i) {
				S[i] = FLIP(S[i]);
			}
			++count;
		}
		++pos;
	}
	for (int i = pos; i < length; ++i) {
		if (S[i] == '-') {
			return "IMPOSSIBLE";
		}
	}
	return to_string(count);
}

int main(int argc, char** argv) {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	setbuf(stdout, NULL);

	int T;
	int test_case;
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case) {
		string answer;
		char S[1001];
		int K;

		scanf("%s", &S);
		scanf("%d", &K);

		answer = solve(S, K);

		printf("Case #%d: ", test_case);
		printf("%s\n", answer.c_str());
	}

	return 0;	
}

