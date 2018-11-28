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
			char val[] = {'R' , 'O' , 'Y' , 'G' , 'B' , 'V'} ;
			int T ;
			cin >> T ;
			rep(i,T)
					{
					 ll n  ;
					 ll ar[6] ;
					 cin >> n ;
					 rep(j,6){
					 	cin >> ar[j] ;
					 }

					 int flag = 0 ;
					 int epos = 0 ;
					 rep(j,6){
					 	if(ar[j] > n/2) { flag = 1 ; break ;}
					 }



					 char col[n] = {0} ;
					 cout << "Case #" << i+1 << ": " ;
					 if(flag == 1) {cout << "IMPOSSIBLE" << endl ;continue ; }
					 int pos[] = {0,2,4} ;
					 int cnt = 0 ;
					 while(cnt < n){
					 	int maxi = 0 ;
					 	int maxpos = 0 ;
					 	rep(j,3){
					 		if(ar[pos[j]] > maxi) { 
					 								if(cnt > 0 && val[pos[j]] == col[cnt-1]) continue ;
					 								maxi = ar[pos[j]] ;
					 								maxpos = pos[j] ;
					 							  }
					 	}
					 	col[cnt] = val[maxpos] ;
					 	ar[maxpos]-- ;
					 	cnt++ ;
					 }

					if(col[n-1] == col[0]) {
 											char c = col[n-1] ;
											 col[n-1] = col[n-2] ;
											 col[n-2] = c ;
											}
					rep(j,n) cout << col[j] ;
					cout << endl ; 
					}
		return 0 ;
	}

