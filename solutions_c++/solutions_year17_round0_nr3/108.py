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

int main() {
	int T, caso=1;
	cin >> T;
	while (T--) {
		ll N, K, lo, hi;
		cin >> N >> K;
		map<ll, ll> m;
		m[N] = 1;
		while (K>0) {
			ll ok = m.rbegin()->second, f=m.rbegin()->first;
			K -= ok;
			lo = f - 1 >> 1, hi = f >> 1;
			m[lo] += ok, m[hi] += ok;
			m.erase(f);
		}
		cout << "Case #" << caso++ << ": " << hi << " " << lo;
		cout << endl;
	}
	return 0;
}
