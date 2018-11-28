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

int t, n, a[100100], p;
int dp2[2][111][111];
int dp3[2][111][111][111];

int calc(int rest, int a, int b) {
    if (a < 0 || b < 0) return -inf;
    if (a + b == 0) return 0;
    int &res = dp2[rest][a][b];
    if (res != -1) return res;
    res = (rest == 0) + calc(rest, a - 1, b);
    res = max(res, (rest == 0) + calc(rest^1, a, b - 1));
    return res;
}

int calc(int rest, int a, int b, int c) {
    if (a < 0 || b < 0 || c < 0) return -inf;
    if (a + b + c == 0) return 0;
    int &res = dp3[rest][a][b][c];
    if (res != -1) return res;
    res = -inf;
    if (a) res = (rest == 0) + calc(rest, a - 1, b, c);
    if (b) res = max(res, (rest == 0) + calc((rest + 1) % 3, a, b - 1, c));
    if (c) res = max(res, (rest == 0) + calc((rest + 2) % 3, a, b, c - 1));
    return res;
}

void solve2(int case_num) {
    memset(dp2, -1, sizeof dp2);
    int k[2] = {0, 0};
    for (int i = 0; i < n; i++) {
        k[a[i] % p]++;
    }
    int ans = k[0] + (k[1] + 1) / 2;
    printf("Case #%d: %d\n", case_num, ans);
}

void solve3(int case_num) {
    memset(dp3, -1, sizeof dp3);
    int k[3] = {0, 0, 0};
    for (int i = 0; i < n; i++) {
        k[a[i] % p]++;
    }
    int ans = k[0];
    int mn = min(k[1], k[2]);
    ans += mn;
    k[1] -= mn;
    k[2] -= mn;
    ans += (k[1] + k[2] + 2) / 3;

    printf("Case #%d: %d\n", case_num, ans);
}

void solve(int case_num) {
    scanf("%d%d", &n, &p);
    for (int i = 0; i < n; i++) {
        scanf("%d", a + i);
    }
    if (p == 2) solve2(case_num);
    else if (p == 3) solve3(case_num);
    else assert(false);
}

int main(){

    scanf("%d", &t);
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}
