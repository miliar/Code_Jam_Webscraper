#include <bits/stdc++.h>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it)
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define READ(a) int a; 0 == scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(_i,n){ 0 == scanf("%d", &v[_i]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
const double PI = std::atan(1.0)*4;
#define cpx complex<double>
#define MOD 1000000007ll
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define MAXN 1000005

int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		READ(n); READ(p);
		READV(r, n)
		vector<vpii> pack;
		FOR(i, n){
			READV(v, p)
			sort(all(v));
			vpii w;
			FOR(j, sz(v)){
				double x = v[j];
				int s = 0;
				pii pi=mp(-1, -1);
				FOR(k, MAXN){
					if( 0.9*s <= x && x<= 1.1*s){
						if(pi.ff==-1) pi.ff = s/r[i];
						pi.ss = s/r[i];
					}
					s += r[i];
					if(x < 0.9*s) break;
				}
				if(pi.ff!=-1){
					// cout<<pi.ff<<" "<<pi.ss<<endl;
					w.pb(pi);
				}
			}
			pack.pb(w);
		}
		ll res =0;

		int m = -1;
		FOR(i,n){
			if(pack[i].empty()){
				cout<<"Case #"<<(t+1)<<": "<<0<<endl;
				goto next;
			}

			gmax(m, pack[i].back().ss);
		}
		while(true){
			// cout<<m<<endl;
			bool ok = true;
			FOR(i,n){
				while(!pack[i].empty() && pack[i].back().ff > m) pack[i].pop_back();
				if(pack[i].empty()){ ok = false; break; }

				if(pack[i].back().ff <= m && m <= pack[i].back().ss){

				}else{
					ok = false;
				}
			}
			if(ok){
				FOR(i, n){
					pack[i].pop_back();
				}
				res++;
			}else{
				m--;
				if(m==0) break;
			}

		}

		cout<<"Case #"<<(t+1)<<": "<<res<<endl;
		next: continue;
	}
	return 0;
}