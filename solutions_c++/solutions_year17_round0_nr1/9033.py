#include<bits/stdc++.h>
using namespace std ;
bool a[100];
void fanzhuan( int qidian , int k )
{
	for( int i = qidian ; i < ( k + qidian ) ; i++  ) 
		a[i] = !a[i] ;
	return ; 
}


int main()
{
	int t ;
	cin >> t ;
	int kase = 0 ;
	while( t-- )
	{
		printf("Case #%d: ",++kase);
		string s ;
		cin >> s ;
		int k ;
		cin >> k ;
		int n = s.size() ; 
		for( int i = 0 ; i < s.size() ; i++)
			a[i+1] = ( (s[i] == '+') ? 1 : 0 ) ; 
		int cnt = 0 ; 
		for( int i = 1 ; i <= n ; i++ )
		{
			if( a[i] == 0  && i <= ( n - k + 1 ) )
			{
				fanzhuan(i,k);
				cnt++;
			}
		}
		int flag = true ; 
		for( int i = 1 ; i <= n ; i++)
		{
			if( a[i] == 0 )
			{
				flag = false ;
				break ; 
			}
		}

		if( flag )
			cout << cnt << endl ;
		else
			cout << "IMPOSSIBLE" << endl ;
	}
	return 0  ; 
}


