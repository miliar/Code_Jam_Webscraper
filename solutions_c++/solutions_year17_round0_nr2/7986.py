#include <bits/stdc++.h>
using namespace std;

#define MEM(arr,val)memset((arr),(val), sizeof (arr))
#define PI (acos(0)*2.0)
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define ALL(v)v.begin(),v.end()
#define PB(v)push_back(v)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll gcd(ll a,ll b){return b == 0 ? a : gcd(b,a%b);}
ll lcm(ll a,ll b){return a*(b/gcd(a,b));}

/**
 * __builtin_popcount(int d) // count bits
 * __builtin_popcountll(long long d)
 * strtol(s, &end, base); // convert base number
 */
//----------------------------------------------------------------------//

bool is_tidy(string s){
	for (int i = 0; i < s.size()-1; ++i) {
		if(s[i] > s[i+1])return false;
	}
	return true;
}

ll toint(string s){
	ll l = 0;

	for (int i = 0; i < s.size(); ++i) {
		l *= 10;
		l += s[i] - '0';
	}
	return l;
}

int main(){
	FASTER;
	int t;
	cin>> t;
	int Case = 1;
	while(t--){
		string s;
		cin >> s;

		ll ans = 0;

		if(is_tidy(s)){
			ans = max(ans, toint(s));
		}

		for (int i = 0; i < s.size(); ++i) {

			string y = s;

			if(y[i] > '0')
				y[i]--;

			for (int j = i+1; j < y.size(); ++j) {
				y[j] = '9';
			}

			if(is_tidy(y)){
				ans = max(ans, toint(y));
			}

		}
		cout << "Case #" << (Case++) << ": ";
		cout << ans << endl;

	}

	return 0;
}
