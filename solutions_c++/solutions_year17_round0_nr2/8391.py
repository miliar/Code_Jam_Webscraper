//If you are trying to hack me I wish you can get it, Good Luck :D
#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf (stderr,args)
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const int INF = 0x3f3f3f3f;
const ll  MOD = 1000000007;

int main () {
    int t;
    ll n;
    cin >> t;
    for (int T = 1; T <= t; T++) {
	ll resp;
	bool ok = false;
	cin >> n;
	resp = n;
	while (!ok) {
	    string s = to_string(resp);
	    int tam = s.size();
	    //debug ("--> %lld %s\n", resp, s.c_str());

	    ok = true;
	    for (int i = 0; i < (tam - 1); i++) {
		if (s[i] > (s[i + 1])) {
		    ok = false;
		    break;
		}
	    }
	    if (ok) break;
	    resp--;
	}

	cout << "Case #" << T << ": " << resp << '\n';
    }
    return 0;
}

