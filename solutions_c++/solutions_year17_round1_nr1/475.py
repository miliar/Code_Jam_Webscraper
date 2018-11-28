#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxSize	25

char mat[maxSize][maxSize];

int main() {
	int T, caso=1;
	cin >> T;
	while (T--) {
		int R, C;
		cin >> R >> C;
		FOR(i, 0, R) FOR(j, 0, C) cin >> mat[i][j];
		FOR(i, 0, R) {
			int last = -1;
			FOR(j, 0, C) {
				if (mat[i][j] != '?') {
					int k = j - 1;
					last = j;
					while (k >= 0 && mat[i][k] == '?') {
						k--;
					}
					int kk = i - 1;
					while (kk >= 0 && mat[kk][j] == '?') {
						kk--;
					}
					FOR(l, kk+1, i + 1) {
						FOR(r, k+1, j + 1) mat[l][r] = mat[i][j];
					}
				}
			}
			if (~last) {
				int kk = i;
				while (kk >= 0 && mat[kk][last] == mat[i][last]) {
					FOR(j, last, C) mat[kk][j] = mat[i][last];
					kk--;
				}
			}
		}
		FOR(i, 1, R) {
			FOR(j, 0, C) {
				if (mat[i][j] == '?') {
					mat[i][j] = mat[i - 1][j];
				}
			}
		}
		cout << "Case #" << caso++ << ": " << endl;
		FOR(i, 0, R) {
			FOR(j, 0, C) {
				cout << mat[i][j];
			}
			cout << endl;
		}
		cout << endl;
	}
	return 0;
}
