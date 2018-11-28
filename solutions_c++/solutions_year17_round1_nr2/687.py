#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sqr(x) ((x)*(x))
#define mp make_pair
#define ones(x) __builtin_popcount(x)
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0);
#define debug(x) cout << #x << ": " << x << endl;
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(auto it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
#define sz(v) int(v.size())

typedef pair<int,int> ii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair< ii, int > tri;
typedef unsigned int uint;

const double PI = acos(-1);
const int  INF = 2e9;
const ll LINF = 1e18 + 5;
const ll MOD = 1e9 + 7;
const int MAXN =  1e5 + 5;
const int MN = 1e6 + 2;



int r[55];
int q[55][55];
ii t[55][55];
int l[55];
int tochange[55]; 


ii get(int f, int a){
	int hi = 10 * a;
	hi /= (9 * r[f]);
	int lo = 10 * a;
	if(lo % (11 * r[f]) == 0) lo /= (11 * r[f]);
	else lo = (lo/(11 * r[f])) + 1;
	return mp(lo, hi);
}


int main(){
	fast_io();
	int tc; cin >> tc;
	for(int tt = 1; tt <= tc; ++tt){
		int n, p; cin >> n >> p;
		for(int i = 0; i < n; ++i) cin >> r[i];
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < p; ++j){
				cin >> q[i][j];
			}
		}

		for(int i = 0; i < n; ++i){
			for(int j = 0; j < p; ++j){
				t[i][j] = get(i, q[i][j]); 
			}
		}		

		for(int i = 0; i < n; ++i){
			sort(t[i], t[i] + p);
		}
		

//		for(int i = 0; i < n; ++i){
//			for(int j = 0; j < p; ++j){
//				cout << "(" << t[i][j].fst << ", " << t[i][j].snd << ") ";
				
//			}
//			cout << endl; 
//		}

		int ans = 0;

		for(int i = 0; i < n; ++i) l[i] = -1;
		vector< int > v;
		v.clear();
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < p; ++j) v.pb(t[i][j].fst), v.pb(t[i][j].snd);
		}

		sort(all(v));
		
		bool end = 0;
		for(int rt = 0; rt < sz(v); ++rt){
			int valor = v[rt];
			int add = 0;
			for(int i = 0; i < n; ++i){
				for(int fu = l[i] + 1; fu < p; ++fu){
					if(t[i][fu].fst <= valor && t[i][fu].snd >= valor){
						add ++; 
						tochange[i] = fu;
						break; 
					}	
				}
				
			}
			if(add == n){
				ans ++;
				for(int i = 0; i < n; ++i){
					l[i] = tochange[i]; 
				}	
			}
			for(int i = 0; i < n; ++i) 
				if(l[i] == (p - 1)) end = 1;
			if(end) break; 
		}

		

		
 		cout << "Case #" << tt << ": " << ans << endl; 

	}

	return 0;
}




























