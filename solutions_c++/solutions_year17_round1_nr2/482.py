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

#define maxN 50

int a[maxN], p[maxN][maxN], l[maxN];

int main() {
	int T, caso=1;
	cin >> T;
	while (T--) {
		int N, P;
		cin >> N >> P;
		memset(l, 0, sizeof(l));
		FOR(i, 0, N) {
			cin >> a[i];
		}
		FOR(i, 0, N) {
			FOR(j, 0, P) {
				cin >> p[i][j];
			}
			sort(p[i], p[i] + P);
		}
		int ans = 0;
		FOR(i, 0, P) {
			double l1 = round(1.*p[0][i] / (0.9*a[0]));
			double r2 = round(1.*p[0][i] / (1.1*a[0]));
			FOR(r, max(1., r2), l1+1) {
				if (p[0][i] / 0.9 >= (r*a[0]) && p[0][i] / 1.1 <= (r*a[0])) {
					int v = 1;
					FOR(j, 1, N) {
						while (l[j] < P && p[j][l[j]]/0.9 <(r*a[j])) {
							l[j]++;
						}
						if (l[j] >= P || p[j][l[j]] / 1.1 > (r*a[j])) {
							v = 0;
						}
					}
					if (v) {
						FOR(j, 1, N) l[j]++;
						ans++;
						break;
					}
				}
			}
		}
		cerr << caso << endl;
		cout << "Case #" << caso++ << ": "<<ans;
		cout << endl;
	}
	return 0;
}
