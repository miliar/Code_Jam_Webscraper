#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l;

string h = "ROYGBV";
int cnt[1000], ans[1000];

int main() {
    //freopen("x.in", "r", stdin);

	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
		cerr << tt << endl;
		cin >> n; F0(i, 6) cin >> cnt[i];

		printf("Case #%d: ", tt);

		// special
		int special = -1;
		for (int i = 0; i < 6; i += 2) if (n % 2 == 0 && cnt[i] == n / 2 && cnt[(i + 3) % 6] == n / 2) {
			special = i;
			break;
		}

		if (special != -1) {
			F0(i, n / 2) cout << h[special] << h[(special + 3) % 6];
			cout << endl;
			continue;
		}

		int bad = 0;

		for (int i = 0; i < 6; i += 2) {
			int w = cnt[(i + 3) % 6];
			if (w && cnt[i] <= w) { bad = 1; break; }
			cnt[i] -= w;
			n -= 2 * w;
		}

		if (bad || cnt[0] + cnt[2] < cnt[4] || cnt[0] + cnt[4] < cnt[2] || cnt[2] + cnt[4] < cnt[0]) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			F0(i, n) {
				int best = -1, k = -1;
				F0(j, 3) {
					if (!cnt[2 * j] || (i > 0 && ans[i - 1] == 2 * j)) continue;
					int score = 2 * cnt[2 * j];
					if (i > 0 && ans[0] == 2 * j) score++;
					if (score > best) { best = score; k = 2 * j; }
				}
				ans[i] = k;
				cnt[k]--;
			}
			F0(i, n) {
				cout << h[ans[i]];
				int w = (ans[i] + 3) % 6;
				while (cnt[w] > 0) {
					cnt[w]--;
					cout << h[w] << h[ans[i]];
				}
			}
			cout << endl;
		}
	
	}
	return 0;
}
