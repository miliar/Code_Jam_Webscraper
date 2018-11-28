#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

vector<int> v;
int dp[2][10][20];
ll n;

int can(int eq, int last, int ind) {
    if (ind == v.size()) return true;
    int &res = dp[eq][last][ind];
    if (res != -1) return res;
    res = 0;
    int st = last;
    int en = 9;
    if (eq) en = v[ind];
    for (int i = st; i <= en; i++) {
        res |= can(eq&(i == v[ind]), i, ind + 1);
    }
    return res;
}

void rec(int eq, int last, int ind, ll &ans) {
    if (ind == v.size()) return;
    int st = last;
    int en = 9;
    if (eq) en = v[ind];
    for (int i = en; i >= st; i--) {
        if (can(eq&(i == v[ind]), i, ind + 1)) {
            ans = 10ll * ans + i;
            rec(eq&(i == v[ind]), i, ind + 1, ans);
            return;
        }
    }
}

void solve(int case_num) {
    v.clear();
    cin >> n;
    while (n) {
        v.pb(n % 10);
        n /= 10;
    }
    reverse(all(v));
    memset(dp, -1, sizeof dp);
    ll ans = 0;
    rec(1, 0, 0, ans);
    printf("Case #%d: %lld\n", case_num, ans);
}

int main(){

    int T;

    cin >> T;

    for (int i = 1; i <= T; i++) {
        solve(i);
    }

    return 0;
}
