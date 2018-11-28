#include <stdio.h>
#include <iostream>
#include <stack>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

int T, R, C;
string A[30];
int main() {
	freopen("c:\\users\\ahsalam\\documents\\gcj\\round_a\\A-large.in", "r", stdin);
	freopen("c:\\users\\ahsalam\\documents\\gcj\\round_a\\a-large.out", "w", stdout);

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> R >> C;

		for (int i = 0; i < R; i++) {
			cin >> A[i];
		}

		for (int i = 0; i < R; i++)
		for (int j = 1; j < C; j++) 
			if (A[i][j] == '?' && A[i][j - 1] != '?') A[i][j] = A[i][j - 1];

		for (int i = 0; i < R; i++)
		for (int j = C - 2; j >= 0; j--) 
			if (A[i][j] == '?' && A[i][j + 1] != '?') A[i][j] = A[i][j + 1];

		for (int j = 0; j < C; j++)
		for (int i = 1; i < R; i++)
			if (A[i][j] == '?' && A[i - 1][j] != '?') A[i][j] = A[i - 1][j];

		for (int j = 0; j < C; j++)
		for (int i = R - 2; i >= 0; i--)
			if (A[i][j] == '?' && A[i + 1][j] != '?') A[i][j] = A[i + 1][j];

		printf("Case #%d:\n", t);
		for (int i = 0; i < R; i++)
			printf("%s\n", A[i].c_str());
	}

	return 0;
}