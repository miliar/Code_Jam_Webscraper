#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

struct testcase_t
{
	string num;
};

string solve( const testcase_t& test )
{
	if ( test.num == "0" )
		return "0";

	auto result = test.num;
	for ( size_t i = 1; i < result.size( ); ++i )
	{
		if ( i < 1 ) break;
		char& prev = result[ i - 1 ];
		char& cur = result[ i ];
		if ( prev > cur )
		{
			prev -= 1;
			for (size_t j=i; j < result.size( ); ++j )
			{
				result[ j ] = '9';
			}
			i -= 2;
		}
	}

	auto offset = result.find_first_not_of( '0', 0 );

	return result.substr( offset );
}

void process(istream &in, ostream &out, ostream &out2)
{
	int testcases_count;
	in >> testcases_count;
	vector<testcase_t> tests;
	for ( int i = 0; i < testcases_count; ++i )
	{
		testcase_t tc;
		in >> tc.num;
		tests.push_back( tc );
	}

	int id = 1;
	for ( auto test : tests )
	{
		const auto solution = solve( test );
		out << "Case #" << id << ": " << solution << endl;
		out2 << "Case #" << id << ": " << solution << endl;
		id++;
	}
}

int main( )
{
	//*
	process( ifstream( "1.in" ), cout, ofstream( "out.txt" )  );
	/*/
	process( ifstream( "sample.txt" ), cout, ofstream( "sample_out.txt" )  );
	//*/
}