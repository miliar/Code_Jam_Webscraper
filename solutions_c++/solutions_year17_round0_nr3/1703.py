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
				for( int i = 0 ; i < T ; i++)
						{
						 ll n , k ;
						 cin >> n >> k ;
						 vl v ;
						 ll dk = k ;
						 while( dk > 1){
						 	v.pb(dk) ;
						 	dk /= 2 ;
						 }

						ll level = v.size() ;
						ll p2 = pow(2,level) ;
						ll cn = n - p2 + 1 ;
						ll cval = cn/p2 ;
						ll rem = cn % p2 ;
						ll ck = k - p2 + 1 ;
						ll ans = 0 ;
						if( ck > rem ){ ans = cval ;}
						else ans = cval + 1 ; 

						ll lval , rval ;
						lval = rval = (ans-1)/2 ;
						if( ans % 2 == 0) {lval++ ; }
						cout << "Case #" << i+1 << ": " ;
						cout << lval << " " << rval << endl ;
						}

		return 0 ;
	}

