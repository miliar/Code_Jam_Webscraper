#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#define ll long long int
using namespace std ;
int main()
{
	string s ;
	ll i , j , k , l , m , n ,t ;
	cin >> t ;
	int iter = 1 ;
	ofstream myfile;
  	myfile.open ("example.txt");
  	
  	for( ; iter <= t ; iter++ )
	{
		cin >> s >> k ;
		int ans = 0 ;
		n = s.length() ;
		for( i = 0 ; i <= n - k ; i++ )
		{
			if( s[i] == '+' )
			continue ;
			else
			{
				ans ++ ;
				for( j = i ; j < i + k ; j++ )
				if( s[j] == '+' )
				s[j] = '-' ;
				else
				s[j] = '+' ;
			}
		}
		for( ; i < n ; i++ )
		if( s[i] == '-' )
		break ;
		myfile << "Case #" << iter << ": ";
		if( i == n )
		myfile << ans << endl ;
		else
		myfile << "IMPOSSIBLE\n" ;
	}
	myfile.close();
}
