#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <stack>
#include <list>
#include <forward_list>
#include <algorithm> // max...
#include <utility> // pair
#include <complex>
#include <climits> // int, ll...
#include <limits> // double...
#include <cmath> // abs, atan...
#include <cstring> // memset
#include <string>
#include <functional> // greater, less...
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, double> id;
typedef pair<double, int> di;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> dd;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef vector<dd> vdd;
typedef vector<id> vid;
typedef vector<vi> vvi;
typedef map<int, int> mii;
typedef map<int, ll> mil;
typedef map<ll, ll> mll;

#define ONLINE_JUDGE

vector<ll> pot2;

ll solm(ll N, ll K) {
    ll d = (ll) log2(K);
    ll x = pot2[d+1];
    ll m = (N-K+1) / x;
    if ((N-K+1) % x == 0) m--;
    return m;
}

ll solM(ll N, ll K) {
    ll d = (ll) log2(K);
    ll x = pot2[d+1];
    ll y = x / 2;
    if (N-K+1-y <= 0) return 0;
    ll M = (N-K+1-y) / x;
    if ((N-K+1-y) % x != 0) M++;
    return M;
}

int main() {
#ifdef ONLINE_JUDGE
    freopen("C-small-2-attempt0.in", "r", stdin);
        freopen("C-small-2-attempt0.out", "w", stdout);
        //freopen("X-large-practice.in", "r", stdin);
        //freopen("X-large-practice.out", "w", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    //freopen("output.out", "w", stdout);
#endif

    ll p = 1;
    pot2.push_back(p);
    for (int i = 1; i <= 60; i++) {
        p *= 2;
        pot2.push_back(p);
    }

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        ll N, K;
        cin >> N >> K;

        ll d = (ll) log2(K);
        ll x = pot2[d+1];
        ll y = pot2[d];

        ll m = (N-K+1) / x;
        if ((N-K+1) % x == 0) m--;

        ll M = 0;
        if (N-K+1-y > 0) {
            M = (N-K+1-y) / x;
            if ((N-K+1-y) % x != 0) M++;
        }

        printf("Case #%d: %lld %lld\n", t, M, m);
    }

    return 0;
}