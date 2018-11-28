/*input
1
105 103
*/
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
#define sp ' '
#define endl '\n'
#define fi first
#define se second
#define mp make_pair
#define int long long
#define N

int n, k;
map<int, int> a;
map<int, int>::iterator it;

void makeans(int x, int CT) {
	int t1 = (x - 1) / 2;
	int t2 = x - 1 - t1;
	cout << "Case #" << CT << ": " << max(t1, t2) << sp << min(t1, t2) << endl;
}

signed main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("1test.inp", "r", stdin);
	freopen("1test.out", "w", stdout);
	int T; cin >> T;
	int CT = 0;
	while (T--) {
		a.clear();
		CT++;
		cin >> n >> k;
		if (k == 1) {
			makeans(n, CT);
			goto out;
		}
		a[n]++;
		k--;
		while (1) {
			map<int, int> b;
			for (it = a.begin(); it != a.end(); it++) {
				int t1 = (it->fi - 1) / 2;
				int t2 = (it->fi - 1) - t1;
				b[t1] += it->se;
				b[t2] += it->se;
			}
			a.clear(); a = b;
			for (it = (--b.end()); it != b.begin(); it--) {
				k -= it->se;
				if (k <= 0) {
					makeans(it->fi, CT);
					goto out;
				}
			}
			k -= b.begin()->se;
			if (k <= 0) {
				makeans(b.begin()->fi, CT);
				goto out;
			}
		}
out:;
	}

}