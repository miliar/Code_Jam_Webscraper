#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <deque>
#include <set>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>

#define pb push_back
#define mp make_pair
#define F first
#define S second

#ifndef LOCAL
#define cerr if(0)cerr
#endif

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long double ld;

const int INF = 2 * int(1e9);
const ll INFll = 1ll * int(1e9) * int(1e9);
const int MOD = 1000000007;

template<typename T, typename Q>
ostream& operator<<(ostream& out, pair<T, Q>& a) {
    out << a.F << " " << a.S;
    return out;
}

template<typename T, typename Q>
istream& operator>>(istream& in, pair<T, Q>& a) {
    in >> a.F >> a.S;
    return in;
}

template<typename T>
istream& operator>>(istream& in, vector<T>& a) {
    for (int i = 0; i < a.size(); ++i)
        in >> a[i];
    return in;
}

template<typename T>
ostream& operator<<(ostream& out, vector<T> a) {
    for (int i = 0; i < a.size(); ++i)
        if (i == a.size() - 1)
            out << a[i];
        else
            out << a[i] << " ";
    return out;
}

void solve() {
	int n, m, c;
	cin >> n >> c >> m;
	int l = 1, r = m;
	vi p(m), b(m);
	for (int i = 0; i < m; ++i)
		cin >> p[i] >> b[i], p[i]--, b[i]--;
	vi order;
	for (int i = 0; i < m; ++i)
		order.pb(i);
	vi k(c);
	for (int buyer : b)
		k[buyer]++;
	pii ans = mp(INF, INF);
	while (l <= r) {
		int mid = (l + r) / 2;
		pii ans_ = mp(INF, INF);
		for (int it = 0; it < 200; ++it) {
			vector<vi> used(mid, vi(n));
			vector<vi> usedb(mid, vi(c));
			bool valid = 1;
			int res = 0;
			random_shuffle(order.begin(), order.end());
			for (int i : order) { 
				bool found = 0;
				for (int j = 0; j < mid; ++j)
					if (!usedb[j][b[i]] && !used[j][p[i]]) {
						used[j][p[i]] = 1;
						usedb[j][b[i]] = 1;
						found = 1;
						break;
					}
				if (!found)
					for (int pos = p[i] - 1; pos >= 0; --pos) 
						if (!found)
							for (int j = 0; j < mid; ++j)
								if (!usedb[j][b[i]] && !used[j][pos]) {
									res++;
									used[j][pos] = 1;
									usedb[j][b[i]] = 1;
									found = 1;
									break;
								}
				if (!found) {
					valid = 0;
					break;
				}
			}
			if (valid)
				ans_ = min(ans_, mp(mid, res));
		}
		if (ans_.F != INF)
			ans = min(ans, ans_), r = mid - 1;
		else
			l = mid + 1;
	}
	cout << ans.F << " " << ans.S << endl;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test)
    	cout << "Case #" << test << ": ", solve(), cerr << test << " done\n";
    cerr << fixed << setprecision(0) << "TIME = " << clock() / (ld)CLOCKS_PER_SEC * 1000 << "\n";
    return 0;
}
