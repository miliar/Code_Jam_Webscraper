/*Jeevan Surya Maddu 
  MJS1997
*/  		
#include <bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb(x) push_back(x)
#define fi first
#define se second
#define vi vector<int> 
#define vl vector<ll>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define dbg(x) cerr << "here " << x << endl;
#define rep(i,n) for(int i = 0 ; i < n ; i++)
#define rrep(i,n) for(int i = n - 1 ; i >= 0 ; i--)
#define mp(a,b) make_pair(a,b)

using namespace std ;

ll binpow( ll a , ll m)
		{
		  ll product = 1 ;
		  ll mult = a ;
		  while( m > 0)
		  		{
		  		if( m % 2 == 1) { product = (product%mod * mult%mod)%mod ;
		  		 				}
		  		m = m / 2 ;
		  		mult = (mult%mod * mult%mod) % mod ;
		  		}
		  product = product % mod ;
		  return product ;		
		}



int main()
	{
			int T ;
			cin >> T ;
			rep(i,T)
					{
					 ll d , n ;
					 cin >> d >> n ;
					 vector<pair<ll,ll> > v ;
					 rep(j,n){
					 	ll a , b ;
					 	cin >> a >> b ;
					 	v.pb(mp(a,b)) ;
					 }
					 sort(v.begin(), v.end()) ;
					 ll mini = v[v.size()-1].se ;
					 ll pos = v[v.size()-1].fi ;
					 rrep(j,n){
					 	if(v[j].se <= mini) {mini = v[j].se ;
					 						 pos = v[j].fi ;
					 						 continue ;}
					 	double long ti = pos - v[j].fi ;
					 	ti /= (v[j].se - mini) ;
					 	double long dd = ti * v[j].se + v[j].fi ;
					 	if( dd < d) continue ;
					 	else { mini = v[j].se ;
					 	 	   pos = v[j].fi ;
					 	 	 }
					 }

					 double long t = d - pos ;
					 t /= mini ;
					 double long ans = d / t ;
					 cout << "Case #" << i+1 << ": " ;
					 cout << setprecision(15) << ans << endl ;		
					}
		return 0 ;
	}

