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
							string N ;
							cin >> N ;
							while(1){
								int flag = 0 ;
								rep(j,N.length() - 1){
									if( N[j] > N[j+1]) {
												N[j] = N[j] - 1 ;
												for( int k = j + 1 ; k < N.length() ; k++){
													N[k] = '9' ;
												}
												flag = 1 ;
									break ;
									}
								}
								if( flag == 0 ) break ;
							}
						 cout << "Case #" << i+1 << ": " ;
						 rep(j,N.length()){
						 	if( N[j] == '0') continue ;
						 	cout << N[j] ;
						 }
						 cout << endl ;
						}
		return 0 ;
	}

