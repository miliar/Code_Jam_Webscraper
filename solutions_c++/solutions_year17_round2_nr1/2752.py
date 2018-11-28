#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <limits>

using namespace std;

const int undefined = -1;

int main()
{
	ifstream in( "C:\\YandexDisk\\Programming\\VsProjects\\in.txt" );
	//istream& in = cin;
	ofstream out( "C:\\YandexDisk\\Programming\\VsProjects\\out.txt" );
	//ostream& out = cout;

	out.precision(std::numeric_limits< double >::max_digits10);

	int testCount;
	in >> testCount;

	for( int test = 1; test <= testCount; test++ ) {
		int d, n;
		in >> d >> n;
		double tMax = 0.;
		for( int i = 0; i < n; i++ ) {
			int k, s;
			in >> k >> s;
			double t = (d - k) * 1. / s;
			if( t > tMax ) {
				tMax = t;
			}
		}
		double vMax = d / tMax;
		out << "Case #" << test << ": " << vMax << endl;
	}

	return 0;
}