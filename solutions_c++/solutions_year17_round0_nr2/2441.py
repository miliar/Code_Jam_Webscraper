#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool canDecrease( const vector<int>& digits, int pos )
{
	return pos == 0 ? true : ( digits[pos - 1] < digits[pos] );
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
		in >> s;

		vector<int> digits;
		for( int i = 0; i < s.length(); i++ ) {
			digits.push_back( s[i] - '0' );
		}

		int wrongPos = 0;
		while( ( wrongPos < digits.size() - 1 )  && digits[wrongPos] <= digits[wrongPos + 1] ) {
			wrongPos++;
		}

		if( wrongPos < digits.size() - 1 ) {
			while( !canDecrease( digits, wrongPos ) ) {
				wrongPos--;
			}
			digits[wrongPos]--;
			for( int i = wrongPos + 1; i < digits.size(); i++ ) {
				digits[i] = 9;
			}
		}

		out << "Case #" << c << ": ";
		for( int i = ( digits[0] == 0 ? 1 : 0 ); i < digits.size(); i++ ) {
			out << digits[i];
		}
		out << endl;
	}

	return 0;
}