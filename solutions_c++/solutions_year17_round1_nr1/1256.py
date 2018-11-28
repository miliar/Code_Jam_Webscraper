#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

#define INF 999999999
#define pb push_back
#define fs first
#define sc second
#define mp make_pair

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UI;
typedef vector < int > VI;
typedef vector < unsigned int > VUI;
typedef vector < string > VS;
typedef vector < pair < int, int > > VII;

char A[30][30];

int main(){
    // freopen(".in", "rt", stdin);
    // freopen(".out", "wt", stdout);

	int T, R, C;
	cin >> T;
	for (int step = 0; step < T; ++step) {

		cin >> R >> C;
		for (int i = 0; i < R; ++i)
			for (int j = 0; j < C; ++j)
				cin >> A[i][j];

		for (int i = 0; i < R; ++i) {

			int countZ = 0;
			for (int j = 0; j < C; ++j)
				if (A[i][j] == '?')
					++countZ;

			if (countZ == 0)
				continue;

			if (countZ == C) {
				if (i == 0) continue;
				for (int j = 0; j < C; ++j)
					A[i][j] = A[i - 1][j];
				continue;
			}

			for (int j = 0; j < C; ++j)
				if (A[i][j] != '?') {
					for (int k = 1; j - k >= 0 && A[i][j - k] == '?'; ++k) A[i][j - k] = A[i][j];
					for (int k = 1; j + k < C && A[i][j + k] == '?'; ++k) A[i][j + k] = A[i][j];
				}

		}

		for (int i = 0; i < R; ++i) {

			int countZ = 0;
			for (int j = 0; j < C; ++j)
				if (A[i][j] == '?')
					++countZ;

			if (countZ != C) {
				for (int i1 = 0; i1 < i; ++i1)
					for (int j = 0; j < C; ++j)
						A[i1][j] = A[i][j];
				break;
			}
		}

		cout << "Case #" << step + 1 << ":\n";
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j)
				cout << A[i][j];
			cout << endl;
		}

	}

    return 0;
}
