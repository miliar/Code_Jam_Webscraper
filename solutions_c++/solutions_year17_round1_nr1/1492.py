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
char c[33][33];
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
		cout << "Case #" << T << ":" << endl;
		cin >> n >> m;
		char q = '.';
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= m; j++){
				cin >> c[i][j];				
			}
		}
		for(int i = 1; i <= n; i++){
			char last = '?';
			for(int j = 1; j <= m; j++){
				if(c[i][j] != '?'){
					last = c[i][j];
					continue;
				}
				if(last != '?'){
					c[i][j] = last;
				}
			}
			last = '?';
			for(int j = m; j >= 1; j--){
				if(c[i][j] != '?'){
					last = c[i][j];
					continue;
				}
				if(last != '?'){
					c[i][j] = last;
				}			
			}
		}
		vector<int> v;
		v.pb(0);
		for(int i = 1; i <= n; i++){
			if(c[i][1] != '?') v.pb(i);
		}
		v.pb(n + 1);
		for(int i = 1; i < v.size(); i++){
			for(int j = v[i - 1] + 1; j < v[i]; j++){
				for(int k = 1; k <= m; k++){
					if(i != v.size() - 1)
						c[j][k] = c[v[i]][k];
					else c[j][k] = c[v[i - 1]][k];
				}
			}
		}
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= m; j++){
				cout << c[i][j];
			}
			cout << endl;
		}
	} 
return 0;
}                   	