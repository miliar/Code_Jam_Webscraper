#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stdlib.h>

using namespace std;

struct testcase_t
{
	uint64_t N;
	uint64_t K;
};

uint64_t get_dist( string& s, uint64_t p, int dir )
{
	uint64_t p2 = p;
	while ( s[ p2 ] == '.' ) p2 += dir;
	if (p > p2) return p - p2 - 1;
	return p2 - p - 1;
}

string solve2( const testcase_t& test )
{
	string stalls(test.N + 2, '.');
	stalls[ 0 ] = '#';
	stalls[ test.N + 1 ] = '#';

	uint64_t a = 0;
	uint64_t b = 0;
	for ( uint64_t person = 0; person < test.K; ++person )
	{
		uint64_t best = 0;
		a = 0;
		b = 0;
		for ( uint64_t i = 1; i < test.N + 2; ++i )
		{
			if ( stalls[ i ] == '#' ) continue;
			auto l = get_dist( stalls, i, -1 );
			auto r = get_dist( stalls, i, 1 );
			auto near = min( l, r );
			auto far = max( l, r );
			if ( near > a || best == 0 )
			{
				a = near;
				b = far;
				best = i;
			}
			else if ( near == a && far > b )
			{
				b = far;
				best = i;
			}
		}
		stalls[ best ] = '#';
	}
	return to_string( b ) + " " + to_string( a );
}

string solve( const testcase_t& test )
{
	map<uint64_t, uint64_t > ranges;

	ranges[ test.N ] = 1;

	auto K = test.K;
	while ( K > 0 )
	{
		auto top = *ranges.rbegin( );
		const auto space = top.first;
		const auto count = top.second;
		const uint64_t a = space / 2;
		const uint64_t b = (space - 1) / 2;
		if ( K <= count )
		{
			return to_string( a ) + " " + to_string( b );
		}
		K -= count;
		ranges.erase( space );
		ranges[a] += count;
		ranges[b] += count;
	}

	return "Error";
}

void process(istream &in, ostream &out, ostream &out2)
{
	int testcases_count;
	in >> testcases_count;
	vector<testcase_t> tests;
	for ( int i = 0; i < testcases_count; ++i )
	{
		testcase_t tc;
		in >> tc.N >> tc.K;
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