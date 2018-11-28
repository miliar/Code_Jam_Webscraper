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

ll n, k;

ll get(ll n, ll k) {
    map<ll, ll> cnt;
    cnt[n] = 1;
    while (true) {
        __typeof(cnt.begin()) it = cnt.end();
        it--;
        ll val = it->f;
        ll curcnt = it->s;
        cnt.erase(it);
        if (curcnt >= k) return val;
        k -= curcnt;
        if (val % 2 == 0) {
            cnt[val / 2] += curcnt;
            cnt[val / 2 - 1] += curcnt;
        } else {
            cnt[val / 2] += 2 * curcnt;
        }
    }
    return -1;
}

void solve(int case_num) {
    cin >> n >> k;
    ll ans = get(n, k);
    printf("Case #%d: %lld %lld\n", case_num, ans / 2, (ans - 1) / 2);
}

int main(){

    int T;

    cin >> T;

    for (int i = 1; i <= T; i++) solve(i);

    return 0;
}
