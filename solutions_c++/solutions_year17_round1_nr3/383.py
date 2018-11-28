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

int T;
int hd, ad, hk, ak, b, d;

int calc(int cntb, int cntd) {
    int curh = hd;
    int res = 0;
    int cur_ak = ak;
    int cur_ad = ad;
    int threshold = 200;
    int it = 0;
    while (it < threshold && cntd > 0) {
        it++;
        res++;
        if (max(0, cur_ak - d) >= curh) {
            curh = hd;
            curh -= cur_ak;
            if (curh <= 0) break;
        } else {
            cntd--;
            cur_ak = max(0, cur_ak - d);
            curh -= cur_ak;
        }
    }
    if (cntd > 0 || curh <= 0) return inf;
    it = 0;
    while (it < threshold && cntb > 0) {
        it++;
        res++;
        if (cur_ak >= curh) {
            curh = hd;
            curh -= cur_ak;
            if (curh <= 0) break;
        } else {
            cntb--;
            cur_ad += b;
            curh -= cur_ak;
        }
    }
    if (cntb > 0 || curh <= 0) return inf;
    int cur_hk = hk;
    it = 0;
    while (it < threshold) {
        it++;
        res++;
        if (cur_hk <= cur_ad) return res;
        if (cur_ak >= curh) {
            curh = hd;
            curh -= cur_ak;
            if (curh <= 0) return inf;
        } else {
            curh -= cur_ak;
            cur_hk -= cur_ad;
            if (cur_hk <= 0) return res;
        }
    }
    return inf;
}

void solve(int num) {
    cin >> hd >> ad >> hk >> ak >> b >> d;
    int ans = inf;
    for (int cntb = 0; cntb <= 100; cntb++) {
        for (int cntd = 0; cntd <= 100; cntd++) {
            ans = min(ans, calc(cntb, cntd));
        }
    }
    if (ans == inf) printf("Case #%d: IMPOSSIBLE\n", num);
    else printf("Case #%d: %d\n", num, ans);
}

int main(){

    cin >> T;

    for (int i = 1; i <= T; i++) {
        solve(i);
    }

    return 0;
}
