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
#define PI 3.141592653589793238462

template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }

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

bool mysort(pair<ll,ll> a , pair<ll,ll> b){
	if(a.fi != b.fi) { return a.fi < b.fi ;}
	else return a.se < b.se ;
}


int main()
	{
			int T ;
			cin >> T ;
			rep(i,T)
					{
					 ll n , k ;
					 cin >> n >> k ;
					 vector<pair<double long,double long> > v ;
					 rep(j,n){
					 	double long a , b ;
					 	cin >> a >> b ;
					 	v.pb(mp(a,b)) ;
					 }
					 sort(v.begin(),v.end(),mysort) ;
					 double long maxi = 0 ;

					 ll pos = 0 ;
					 for(pos = k - 1 ; pos < n ; pos++){
					 
					 	double long a = v[pos].fi * v[pos].fi + 2 * v[pos].se * v[pos].fi ;

					 double long ans = a ;
					 int cnt = 1 ;
					 vector<double long > v2 ;
					 for(int j = pos - 1 ; j >= 0 ; j--)
					 		{
					 			v2.pb(2*v[j].fi*v[j].se) ;	

					 		}

					 sort(v2.begin(),v2.end()) ;
					 rrep(j,v2.size()){
					 	if(cnt==k) break ;
					 	ans += v2[j] ;
					 	cnt++ ;
					 }

					 if( ans > maxi) maxi = ans ;
					}

					 double long ans2 =  PI * maxi ;
					 cout << "Case #" << i+1 << ": " ;
					 cout << setprecision(30) << ans2 << endl ;
					}
		return 0 ;
	}

