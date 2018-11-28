#include <iostream>
#include <fstream>
#include<string>
using namespace std;
bool checkIfSorted ( string s ) {
		for ( int i = 0; i < s.size ( ) - 1; i++ ) {
			if ( s [ i ]>s [ i + 1 ] )
				return false;
		}
		return true;
	}
int main ( ) {
	string s;
	int t;
	fstream in , out;
	in.open ( "B-large.in" , ios::in );
	out.open ( "ans.out",ios::out );
	in >> t;
	int j = 0;
	while ( t-- ) {
		in >> s;
		while ( !checkIfSorted ( s ) ) {
			bool f = true;
			for ( int i = 1; i < s.length ( ); i++ ) {
				if ( s [ i ] < s [ i - 1 ] && f ) {
					s [ i ] = '9';
					s [ i - 1 ]--;
					f = false;
				}
				else if ( !f )
					s [ i ] = '9';
			}
		}
		if ( t )
		out <<"Case #"<<++j<<": "<< stoll (s)  << endl;
		else 
			out << "Case #" << ++j << ": " << stoll ( s );
	}
	out.close ( );
		in.close();
}