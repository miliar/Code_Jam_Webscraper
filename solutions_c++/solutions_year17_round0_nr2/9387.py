#include<bits/stdc++.h>
using namespace std ;
bool judge_tidy_number( long long int k )
{
	if( k >= 0 && k < 10 )
		return true ;
	int temp = k % 10 ;
	k/=10;
	while( k!= 0 )
	{
		if( k % 10 > temp )
			return false ;
		
		temp = k % 10 ;
		k/=10;
	}
	
	return true ; 
}
int main()
{
	int t ;
	cin >> t ;
	int kase = 0 ;
	while(t--)
	{
		printf("Case #%d: ",++kase);
		long long int n ;
		cin >> n ;
		long long int ans = 0 ;
		for( long long int i = n ; ; i--)
		{
			if( judge_tidy_number(i) )
			{
				cout << i << endl ;
				break ; 
			}
		}
	
	}
	return 0 ;
 } 
