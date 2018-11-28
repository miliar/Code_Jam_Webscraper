#include <algorithm>
#include <iostream>
#include <cstdio>
#include <map>
#include <numeric>
#include <cmath>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <complex>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <iomanip>
#include <sys/time.h>
#include <tuple>
#include <random>
using namespace std;

#define endl '\n'
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define UNIQ(v) (v).erase(unique((v).begin(), (v).end()), (v).end())

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> P;
typedef complex<double> comp;
typedef vector< vector<ld> > matrix;
struct pairhash {
public:
    template<typename T, typename U>
    size_t operator()(const pair<T, U> &x) const {
	size_t seed = hash<T>()(x.first);
	return hash<U>()(x.second) + 0x9e3779b9 + (seed<<6) + (seed>>2);
    }
};
const int inf = 1e9 + 9;
const ll mod = 1e9 + 7;
const double eps = 1e-8;
const double pi = acos(-1);
const string yes = "YES", no = "NO";

ll n, k;

P calc(ll s) {
    if (s % 2 == 1) return make_pair(s / 2, s / 2);
    return make_pair(s / 2, s / 2 - 1);
}

P solve() {
    ll v = n, c = 0;
    ll a[2] = {1, 0};
    while (true) {
        if (c + a[0] >= k) {
            return calc(v);
        } else if (c + a[0] + a[1] >= k) {
            return calc(v-1);
        } else {
            c += a[0] + a[1];
            if (v % 2 == 1) {
                ll n0 = a[0] * 2 + a[1], n1 = a[1];
                a[0] = n0;
                a[1] = n1;
                v /= 2;
            } else {
                ll n0 = a[0], n1 = a[0] + a[1] * 2;
                a[0] = n0;
                a[1] = n1;
                v /= 2;
            }
        }
    }
}

void input() {
    cin >> n >> k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout << fixed << setprecision(15);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        input();
        P res = solve();
	cout << "Case #" << i << ": " << res.first << " " << res.second << endl;
    }
}
