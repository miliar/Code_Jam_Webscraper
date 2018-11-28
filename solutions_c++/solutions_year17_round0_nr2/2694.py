#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#define ll long long int
using namespace std ;
int a[20] ;
ll func( ll inp )
{
	ll i , j , k , l , m  ,t ;
	if( inp < 10 )
	return inp ;
	string s ;
	s.clear() ;
	ll temp = inp ;
	while( temp )
	{
		char ch = temp%10 + '0' ;
		s = s + ch ; 
		temp /= 10 ;
	}
	reverse(s.begin() , s.end());
//	cout << s << endl;
	int n = s.length() ;
		//cout << "Hi" ;
	for( i = 0 ; i < s.length() ; i++ )
	a[i] = s[i] - '0' ;
		
	for( i = 0 ; i < s.length() - 1 ; i++ )
	if( a[i+1] < a[i] )
	break ;
	ll num = 0 ;
		
	for( j = 0 ; j <= i ; j++ )
	num = num*10 + a[j] ;
	
	if( i != n -1  )
	num = num - 1 ;
	else
	return num ;
	num = func(num) ;
		
	for( j = i+1 ; j < n  ; j++ )
	num = num*10 + 9 ;
	return num ;
}
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
		//cout << "Hi" ;
		cin >> inp ;
		ll num = func(inp) ; 
		myfile << "Case #" << iter << ": " << num << endl ;
	}
	myfile.close();
}
