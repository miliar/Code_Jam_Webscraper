#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int undefined = -1;

void flip( string& s, int k, int pos )
{
	for( int i = 0; i < k; i++ ) {
		char& c = s[pos + i];
		c = ( c == '+' ) ? '-' : '+';
	}
}

int main()
{
	ifstream in( "C:\\YandexDisk\\Programming\\VsProjects\\in.txt" );
	//istream& in = cin;
	ofstream out( "C:\\YandexDisk\\Programming\\VsProjects\\out.txt" );
	//ofstream& out = cout;

	int count;
	in >> count;

	for( int c = 1; c <= count; c++ ) {
		string s;
		int k;
		in >> s >> k;

		int result = 0;
		for( int i = 0; i < s.length() - k + 1; i++ ) {
			if( s[i] == '-' ) {
				flip( s, k, i );
				result++;
			}
		}

		bool impossible = false;
		for( int i = s.length() - k + 1; i < s.length(); i++ ) {
			if( s[i] == '-' ) {
				impossible = true;
				break;
			}
		}

		out << "Case #" << c << ": ";
		if( impossible ) {
			out << "IMPOSSIBLE";
		} else {
			out << result;
		}
		out << endl;
	}

	return 0;
}