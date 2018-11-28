#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <ctime>

#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<ld, ld> point;

const int N = (int)(1e5) + 7;
const int M = (int)(32);
const ld eps = 1e-12;
const ll MOD = (ll)(1e9) + 7;
const ll INF = (ll)(1e9) + 7;

ld a[N], s[N];

void solve(int iii) {
    int n;
    ld d;
    cin >> d >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> s[i];
    }
    ld mx = 0.0;
    for (int i = 0; i < n; ++i) {
        mx = max(mx, (d - a[i]) / s[i]);
    }
    printf("Case #%d: %1.20lf\n", iii, (double)(d / mx));
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    //freopen("brackets.in", "r", stdin);
    //freopen("brackets.out", "w", stdout);
    int ttt;
    cin >> ttt;
    for (int i = 0; i < ttt; ++i) {
        solve(i + 1);
    }
    return 0;
}
