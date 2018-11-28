#include <set>
#include <iostream>
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

ll tidy(ll x) {
    string num = to_string(x);
    int n = num.size(), i;
    ll ans = 0, ld = 0;
    bool fill = false;
    fo(i,n) {
	if (fill) {
	    ans = ans * 10 + 9;
	} else if (num[i] - '0' >= ld) {
	    ld = num[i] - '0';
	    ans = ans * 10 + ld;
	} else {
	    ans = ans - 1;
	    fill = true;
	}
    }
    if (fill) ans = ans*10 +9;
    return ans;
}

int main(void) {
    int n, i;
    cin >> n;
    fo(i,n) {
	ll x;
	cin >> x;
	while(tidy(x) != x) {
	    x = tidy(x);
	}
	cout << "Case #" << i + 1 << ": ";
	cout << x << endl;
    }
}
