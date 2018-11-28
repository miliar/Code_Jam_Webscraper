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
typedef pair<int, int> P;
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

int n, m, k;
int c[2][1010];

P solve() {
    int tot[2];
    for (int i = 0; i < 2; i++) {
        tot[i] = 0;
        for (int j = 0; j < n; j++)
            tot[i] += c[i][j];
    }

    int h = max(tot[0], tot[1]);
    if (c[0][0] + c[1][0] >= h) {
        int d = c[0][0] + c[1][0] - h;
        return make_pair(h + d, 0);
    } else {
        for (int i = 1; i < n; i++) {
            if (c[0][i] + c[1][i] > h) {
                int d = c[0][i] + c[1][i] - h;
                return make_pair(h, d);
            }
        }
        return make_pair(h, 0);
    }
}

void input() {
    cin >> n >> k >> m;
    memset(c, 0, sizeof(c));
    int p, b;
    for (int i = 0; i < m; i++) {
        cin >> p >> b;
        c[b-1][p-1]++;
    }
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
