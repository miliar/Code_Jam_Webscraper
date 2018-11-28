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

int n, p;
int g[110];

int solve() {
    int a[4];
    memset(a, 0, sizeof(a));
    if (p == 2) {
        for (int i = 0; i < n; i++) {
            a[g[i]%2]++;
        }
        return a[0] + a[1] / 2 + (a[1] % 2);
    } else {
        memset(a, 0, sizeof(a));
        for (int i = 0; i < n; i++) {
            a[g[i]%3]++;
        }
        if (a[1] > a[2]) swap(a[1], a[2]);
        int l = a[1];
        int v = a[2] - l;
        return a[0] + l + v / 3 + (int)(v % 3 != 0);
    }
}

void input() {
    cin >> n >> p;
    for (int i = 0; i < n; i++) cin >> g[i];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout << fixed << setprecision(15);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        input();
	cout << "Case #" << i << ": " << solve() << endl;
    }
}
