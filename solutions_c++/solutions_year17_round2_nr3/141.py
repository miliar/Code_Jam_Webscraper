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
const double inf = 1e18 + 9;
const ll mod = 1e9 + 7;
const double eps = 1e-6;
const double pi = acos(-1);
const string yes = "YES", no = "NO";

int n, q;
double e[110], s[110];
double d[110][110];
int u[110], v[110];

double D[110][110];

void warshall_floyd() {
    for (int k = 0; k < n; k++)
	for (int i = 0; i < n; i++)
	    for (int j = 0; j < n; j++)
		d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
}

void warshall_floyd_D() {
    for (int k = 0; k < n; k++)
	for (int i = 0; i < n; i++)
	    for (int j = 0; j < n; j++)
		D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
}

void solve() {
    warshall_floyd();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (d[i][j] < e[i]+eps) {
                D[i][j] = d[i][j] / s[i];
            } else {
                D[i][j] = inf;
            }
        }
    }
    warshall_floyd_D();

    for (int i = 0; i < q; i++) {
        cout << D[u[i]][v[i]];
        if (i == q-1) cout << endl;
        else cout << " ";
    }
}

void input() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> e[i] >> s[i];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> d[i][j];
            if (d[i][j] < 0)
                d[i][j] = inf;
        }
        d[i][i] = 0;
    }
    for (int i = 0; i < q; i++) {
        cin >> u[i] >> v[i];
        u[i]--; v[i]--;
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
	cout << "Case #" << i << ": ";
        solve();
    }
}
