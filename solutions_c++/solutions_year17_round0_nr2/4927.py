#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>

#define ll long long
#define ff first
#define ss second
#define dd double
#define upi(init, n) for(ll i = init; i < n; ++i)
#define upj(init, n) for(ll j = init; j < n; ++j)
#define upk(init, n) for(ll k = init; k < n; ++k)
#define upl(init, n) for(ll l = init; l < n; ++l)
#define downi(init, n) for(ll i = init; i > n; --i)
#define downj(init, n) for(ll j = init; j > n; --j)
#define pb push_back
#define mp make_pair
#define pll pair<ll, ll>
#define el '\n'
#define mod 1000000007

using namespace std;
ll T, N;
set<ll> ans;

void rec(ll a, ll mx) {
    ans.insert(a);
    if (a * 10 >= 1000000000000000000) {
        return;
    }
    downi(9, mx-1) {
        rec(a*10+i, i);
    }
}

int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    rec(0, 1);
    cin >> T;
    upi(1, T+1) {
        cin >> N;
        auto t = ans.upper_bound(N); --t;
        cout << "Case #" << i << ": " << *t << el;
    }
    return 0;
}
