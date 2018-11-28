#include <iostream>
#include <string>
#include <sstream>

using namespace std;

long long getNumber( string s ){
	long long ret;
	istringstream sin( s );
	sin >> ret;
	return ret;
}

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		string s;
		cin >> s;
		long long res = -1;
		string curRes = s;
		char lastChar = '1';
		for( int i = 0; i < s.length(); i++ ){
			for( char c = '9'; c >= lastChar; c-- ){
				for( int j = i; j < s.length(); j++ )
					curRes[j] = c;
				if( curRes <= s ){
					lastChar = c;
					res = 0;
					break;
				}
			}
		}
		if( res == -1 ){
			curRes = "";
			for( int i = 0; i < s.length() - 1; i++ )
				curRes += '9';
		}
		cout << "Case #" << T << ": ";
		cout << curRes << endl;
	}
	return 0;
}