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
ll T, N, K, curr, t;
ll pows, powc;
set<pll> areas;

void adda(ll sz, ll cnt) {
	auto f = areas.lower_bound(mp(sz, 0));
	if (f != areas.end() && f->first == sz) {
		cnt += f->second;
		areas.erase(f);
	}
	areas.insert(mp(sz, cnt));
}
void dela(ll sz) {
	auto f = areas.lower_bound(mp(sz, 0));
	if (f != areas.end() && f->first == sz) {
		areas.erase(f);
	}
}
pll getl() {
	auto f = areas.end(); --f;
	return *f;
}
int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> T;
    upi(1, T+1) {
        cin >> N >> K;
        adda(N, 1);
        ll L, R = N;
        pows = 0;
        ll cnt = 0;
        while (1) {
        	++cnt;
        	pll mx = getl();
        	L = (mx.ff-1)/2, R = mx.ff/2;
        	pows += mx.ss;
        	if (pows >= K) {
        	    break;
        	}
        	dela(mx.ff);
        	adda(L, mx.ss);
        	adda(R, mx.ss);
        }
        cout << "Case #" << i << ": " << max(L, R) << ' ' << min(L, R) << el;
        areas.clear();
    }
    return 0;
}