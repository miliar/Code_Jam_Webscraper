#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<map>
#define ll long long int
#define N 1000001
using namespace std ;
ll a[1000001] ;
map < ll , ll > mp ;
int main()
{
	string s ;
	ll i , j , k , l , m , n ,t ,inp ;
	cin >> t ;
	int iter = 1 ;
	ofstream myfile;
  	myfile.open ("example.txt");
  	
  	for( ; iter <= t ; iter++ )
	{
		cin >> n >> k ;
		ll cnt = 0 ;	
		mp[n] = 1 ;
		for( i = n ; i >= 0 ;  )
		{
			ll r1 = (i - 1)/2 , r2 = i - 1 - r1   ;
			mp[r1] += mp[i] ;
			mp[r2] += mp[i] ;
			cnt += mp[i] ;
			if( cnt >= k )
			break ;
			mp.erase(i) ;
			i = mp.rbegin()->first;
			//cout << i << endl ;
		}
		//cout << i << endl ;
		ll r1 = (i - 1)/2 , r2 = i - 1 - r1   ;
		myfile << "Case #" << iter << ": " << max(r1,r2) << " " << min(r1,r2) << endl ;
		mp.clear() ;
	}
	myfile.close();
}
