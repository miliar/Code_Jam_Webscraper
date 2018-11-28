#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#include <sstream>
#include <cassert>
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define sz(x) ((int) x.size())
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
#define eps 1e-9
using namespace std;

typedef long long ll;

map < ll, ll, greater<ll> > D;

int main(void) {
    int t, i;
    cin >> t;
    fo(i,t) {
	D.clear();
	ll n, k, ans;
	cin >> n >> k;
	D[n] = 1;
	while(k > 0) {
	    ll cD = D.begin()->first, cC = D.begin()->second;
	    // cout << k << " " << cD << " " << cC << endl;
	    k -= cC;
	    ans = cD;
	    cD--;
	    if (cD % 2) {
		D[cD / 2] += cC;
		D[cD / 2 + 1] += cC;
	    } else {
		D[cD / 2] += 2 * cC;
	    }
	    D.erase(cD+1);
	}
	if (ans > 0) ans--;
	cout << "Case #" << i + 1 << ": " << ans / 2 + ans % 2 << " " << ans / 2 << endl;
    }
}
