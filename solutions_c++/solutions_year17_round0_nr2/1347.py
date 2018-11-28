#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>
#include <limits.h>
#include <assert.h>
#include <string.h>
#include <Util.h>

using namespace std;

void solve(int CASE, string s) {
	int L = s.length();
	int S[1024];

	for (int i = 0; i < L; i++) {
		S[i] = s[i] - '0';
	}

	bool changed = true;
	while (changed) {
		changed = false;
		for (int i = 0; i < L - 1; i++) {
			if (S[i] > S[i + 1]) {
				changed = true;
				S[i]--;
				for (int j = i + 1; j < L; j++) {
					S[j] = 9;
				}
			}
		}
	}

	printf("Case #%d: ", CASE);
	bool seenFirstNonZero = false;
	for (int i = 0; i < L; i++) {
		if (S[i] != 0) seenFirstNonZero = true;
		if (S[i] == 0 && !seenFirstNonZero) continue;
		printf("%d", S[i]);
	}
	printf("\n");
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	string s;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> s;
		solve(CASE, s);
	}
    return 0;
}
