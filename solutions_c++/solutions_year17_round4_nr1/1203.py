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

bool debug = false;

int N, P;
int G[1000];
int count0 = 0, count1 = 0, count2 = 0, count3 = 0;

int solve2(int CASE) {
	int c = count0;
	count0 = 0;
	while (count1 >= 2) {
		count1 -= 2;
		c++;
	}
	if (count1 > 0) {
		c++;
	}
	return c;
}

int solve3(int CASE) {
	int c = count0;
	count0 = 0;
	while (count1 > 0 && count2 > 0) {
		count1--; count2--;
		c++;
	}
	while (count1 >= 3) {
		count1 -= 3;
		c++;
	}
	while (count2 >= 3) {
		count2 -= 3;
		c++;
	}
	if (count1 > 0 || count2 > 0) c++;
	return c;
}

int solve4(int CASE) {
	int c = count0;
	count0 = 0;
	while (count1 > 0 && count3 > 0) {
		count1--; count3--;
		c++;
	}
	while (count2 >= 2) {
		count2 -= 2;
		c++;
	}
	if (count2 >= 1 && count1 >= 2) {
		count2 -= 1; count1 -= 2;
		c++;
	}
	if (count2 >= 1 && count3 >= 2) {
		count2 -= 1; count3 -= 2;
		c++;
	}
	while (count1 >= 4) {
		count1 -= 4;
		c++;
	}
	while (count3 >= 4) {
		count3 -= 4;
		c++;
	}
	if (count1 > 0 || count2 > 0 || count3 > 0) {
		c++;
	}

	return c;
}

void solve(int CASE) {
	count0 = count1 = count2 = count3 = 0;
	for (int i = 0; i < N; i++) {
		if (G[i] == 0) count0++;
		if (G[i] == 1) count1++;
		if (G[i] == 2) count2++;
		if (G[i] == 3) count3++;
	}	
	int answer = 0;
	if (P == 2) {
		answer = solve2(CASE);
	} else if (P == 3) {
		answer = solve3(CASE);
	} else if (P == 4) {
		answer = solve4(CASE);
	}
	cout << "Case #" << CASE << ": " << answer << endl;
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> N >> P;
		for (int r = 0; r < N; r++) {
			int g = 0;
			fin >> g; g = g % P;
			G[r] = g;
		}
		solve(CASE);
	}
    return 0;
}
