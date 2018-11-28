/*
  /\     /\
  | ).|.( |
  |  >-<  |
  =========
It's AdilkhanKo miaaaaaau
*/
#include<bits/stdc++.h>

#define ll long long
#define pb push_back
#define endl "\n"
#define foreach(it, S) for(__typeof (S.begin()) it = S.begin(); it != S.end(); it++)
#define mp make_pair
#define f first
#define s second
#define name ""
#define _ ios_base::sync_with_stdio(false);cin.tie(0);

using namespace std;

const int MaxN = int (2e6) + 256;
const ll INF = (ll)(1e18);
const int mod = 10056;
const double pi = 3.1415926535897932384626433832795;
ll n, m, ans, a[MaxN], b[MaxN];

int main () { 
	#ifdef ONLINE_JUDGE
//		freopen (name".in","r",stdin);
//		freopen (name".out","w",stdout);
	#else
		freopen (".in","r",stdin);
		freopen (".out","w",stdout);
	#endif
	int t; cin >> t;
	for(int T = 1; T <= t; T++){
		string s; cin >> s;
		int k; cin >> k;
		bool ok = 0;
		int mn = 0;
		for(int i = 0; i < s.size(); i++){
			if(s[i] == '-'){
				mn++;
				if(i + k - 1 <= s.size() - 1){
					for(int j = i; j <= i + k - 1; j++){
						if(s[j] == '-')s[j] = '+';
						else s[j] = '-';	
					}
				}else{
					ok = 1;
				}
			}
		}	
		cout << "Case #"  << T << ": ";
		if(ok)cout << "IMPOSSIBLE";
		else cout << mn;
		cout << endl;
	}	
return 0;
}                   	