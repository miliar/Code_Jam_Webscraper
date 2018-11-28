#include <vector>
#include <map>
#include <set>
#include <complex>
#include <ctime>
#include <iostream>
#include <cmath>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cassert>
#include <sstream>

const long double PI(acosl(-1.0));
const long double E = 2.71828182845904;
long double eps = 1e-10;

#define pb push_back
#define mp(a,b) make_pair(a,b)
#define all(x) x.begin(), x.end()
#define sqr(x) ((x)*(x))
#define F first
#define S second
#define inf (int)(1e9+7)
#define infll (ll)(1e18+3)
#define sz(x) ((int)x.size())
#define bits(x) __builtin_popcount(x)
#define bitsl(x) __builtin_popcountll(x)

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef vector <ll > vll;
typedef vector<int> vi;
typedef pair < ll, ll > pll;
typedef pair < int, int > pii;
typedef vector<vi> vii;
typedef int huint;

using namespace std;

const int N = 1050;
ld matr[N][N];

void solve() {
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;
    vector<ld> pp(n);
    for (int i = 0; i < n; i++)
        cin >> pp[i];

    sort(all(pp));
    double ans = 0.0;
    for (int i = n - k; i < n; i++) {
        if (u < eps)
            break;
        double qw = 0;
        for (int j = n - k; j < i; j++)
            qw += pp[i] - pp[j];
        double add = min(u / (i - (n - k)), qw / (i - (n - k)));
        for (int j = n - k; j < i; j++) {
            pp[j] += add;
            u -= add;
        }
    }


    if (u > eps) {
        double add = u / (k);
        for (int i = n - k; i < n; i++) {
            pp[i] += add;
        }
    }


    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            matr[i][j] = 0;
        }
    }

    matr[0][0] = 1;
    for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                if (j != k) {
                    matr[i + 1][j] += matr[i][j] * (1 - pp[i]);
                    matr[i + 1][j + 1] += matr[i][j] * pp[i];
                } else {
                    matr[i + 1][j] += matr[i][j];
                }
            }
        }

    cout.precision(10);
    matr[n][k] = min((ld) 1.0, matr[n][k]);
    cout << fixed << matr[n][k] << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for(int tt(0);tt<test;tt++) {


        cout << "Case #" << tt + 1 << ": ";
        solve();
    }
}
