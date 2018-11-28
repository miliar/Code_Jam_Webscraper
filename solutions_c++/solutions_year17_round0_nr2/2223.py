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
		for(int i = s.size() - 2; i >= 0; i--){
			if(s[i] > s[i + 1]){
				if(s[i] == '0'){
					s[i] = '9';
				}else{
					s[i]--;
				}
				for(int j = i + 1; j < s.size(); j++) s[j] = '9';
			}
		} 
		cout << "Case #" << T << ": ";
		bool ok = 0;
		for(int i = 0; i < s.size(); i++){
			if(s[i] > '0'){
				cout << s[i];
				ok = 1;
			}else{
				if(ok)cout << 0;
			}
		}
		cout << endl;
	}
return 0;
}                   	