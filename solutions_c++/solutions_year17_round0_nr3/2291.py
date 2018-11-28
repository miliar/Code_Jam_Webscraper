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
ll n, m, ans, a[MaxN], b[MaxN], k;

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
		cout << "Case #" << T << ": ";
		map<ll, ll> M;
		cin >> n >> k;
		ll K = 1;
		ll L = n / 2, R = (n + 1) / 2 - 1;
		M[L]++;
		M[R]++;
		if(k == 1){
			cout << L << " " << R << endl;
			continue;
		}
		ll p = 2;
		while(K < k){
			if(K + p >= k){
				if(K + M[L] >= k){
					cout << L / 2 << " " << (L + 1) / 2 - 1 << endl;				
				}else{
					cout << R / 2 << " " << (R + 1) / 2 - 1 << endl;
				}				
				break;
			}else{
				K += p;
				ll L2, R2;
				ll L1 = (L) / 2, R1 = (L + 1) / 2 - 1;
				L2 = L1;
				ll M_L = M[L];
				ll M_R = M[R];
				M[L1] += M_L;
				M[R1] += M_L;
				L1 = (R / 2);
				R1 = (R + 1) / 2 - 1;
				R2 = R1;
				if(L != R){
					M[L1] += M_R;
					M[R1] += M_R;
				}
				L = L2;
				R = R2;
				p *= 2;
			}						
		}
	}
return 0;
}                   	