#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

struct testcase_t
{
	string s;
	size_t size;
};

void flip( string& s, size_t pos, size_t size )
{
	for ( size_t i = 0; i < size; ++i )
		s[ pos + i ] ^= '+'^'-';
}

string solve( const testcase_t& test )
{
	set<string> postions;
	postions.insert( test.s );

	const string target( test.s.size( ), '+' );
	vector<string> in, out;

	in.push_back( test.s );

	int steps = 0;
	while ( !in.empty( ) )
	{
		for ( auto& s : in )
		{
			if ( s == target )
				return to_string( steps );
			string s2;
			for ( size_t i = 0; i <= s.size( ) - test.size; ++i )
			{
				s2 = s;
				flip( s2, i, test.size );

				if ( postions.count( s2 ) == 0 )
				{
					out.push_back( s2 );
					postions.insert( s2 );
				}
			}
		}

		steps += 1;
		swap( in, out );
		out.clear( );
	}

	return "IMPOSSIBLE";
}

void process(istream &in, ostream &out, ostream &out2)
{
	int testcases_count;
	in >> testcases_count;
	vector<testcase_t> tests;
	for ( int i = 0; i < testcases_count; ++i )
	{
		testcase_t tc;
		in >> tc.s >> tc.size;
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
	process( ifstream( "input.txt" ), cout, ofstream( "out.txt" )  );
//	process( ifstream( "sample.txt" ), cout, ofstream( "sample_out.txt" )  );
}