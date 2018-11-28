#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
	ifstream in( "C:\\YandexDisk\\Programming\\VsProjects\\in.txt" );
	//istream& in = cin;
	ofstream out( "C:\\YandexDisk\\Programming\\VsProjects\\out.txt" );
	//ofstream& out = cout;

	int count;
	in >> count;

	for( int c = 1; c <= count; c++ ) {
		__int64 n, k;
		in >> n >> k;

		map<__int64, __int64> index;
		index.insert( pair<__int64, __int64>( n, 1 ) );

		__int64 counter = 0;
		while( true ) {
			auto it = --index.end();
			__int64 length = it->first;
			__int64 count = it->second;

			__int64 lLength = ( length - 1 ) / 2;
			__int64 rLength = ( length % 2 == 0 ) ? ( lLength + 1 ) : lLength;

			counter += count;
			if( counter >= k ) {
				out << "Case #" << c << ": " << rLength << " " << lLength << endl;
				break;
			}

			index.erase( it );
			if( lLength > 0 ) {
				index[lLength] += count;
			}
			if( rLength > 0 ) {
				index[rLength] += count;
			}
		}
	}

	return 0;
}