#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool no_zero( const char c )
{
	return c != '0';
}

void print( const string& number )
{
	// ignore zeros
	string::const_iterator s_it = find_if( number.begin(), number.end(), no_zero );
	for( string::const_iterator it = s_it; it != number.end(); ++it )
	{
		cout << *it;
	}
}

bool is_tidy( const string& number )
{
	for( int i = 0; i < number.size() - 1; ++i )
	{
		if( number[i] > number[i + 1] )
		{
			return false;
		}
	}
	return true;
}

void minus1( string& s, int last )
{
	if( last < 0 )
	{
		return;
	}

	switch( s[last] )
	{
		case '9':
			s[last] = '8';
		break;
		case '8':
			s[last] = '7';
		break;
		case '7':
			s[last] = '6';
		break;
		case '6':
			s[last] = '5';
		break;
		case '5':
			s[last] = '4';
		break;
		case '4':
			s[last] = '3';
		break;
		case '3':
			s[last] = '2';
		break;
		case '2':
			s[last] = '1';
		break;
		case '1':
			s[last] = '0';
		break;
		default:
			s[last] = '9';
			minus1( s, --last );
		break;
	}	
}

bool equals( const string& s1, const string& s2  )
{
	// start from the end
	for( int i = s1.size() - 1; i >= 0; --i )
	{
		if( s1[i] != s2[i] )
		{
			return false;
		}
	}
	return true;
}

void solve1( string N, int t )
{
	string ZERO = string( N.size(), '0' );
	int n = N.size();
	int s = n - 1; 
	for( int i = s; i > 0; --i )
	{
		if( N[i] < N[ i - 1 ] )
		{
			minus1( N, i - 1 );
			for( int j = i; j != n; ++j  )
			{
				N[j] = '9';	
			}
		}
	}
	cout << "Case #" << t << ": "; 
	print( N );
	cout << '\n';

	/*
	while( !equals( N, ZERO ) )
	{
		cerr << N << '\n';
		if( is_tidy( N ) )
		{
			cout << "Case #" << t << ": "; 
			print( N );
			cout << '\n';
			return;	
		}
		else
		{
			minus1( N, s - 1 );
		}
	}
	*/
}


int main( int argc, const char* argv[] )
{
	int T = 0;
	string N;
	cin >> T;
	for( int i = 0; i != T; ++i )
	{
		cin >> N;
		solve1( N, i + 1 );
	}	

	return 0;
}
