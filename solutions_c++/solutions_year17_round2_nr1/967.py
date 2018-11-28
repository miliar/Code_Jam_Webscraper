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
	int D;
	vector<pair<int,int>> n;
};

string solve( const testcase_t& test )
{
	double result = 1e99;

	for (auto& h : test.n)
	{
		double time = (double)(test.D - h.first) / h.second;
		double speed = test.D / time;
		if (speed < result)
			result = speed;
	}

	return to_string(result);
}

string no_endl(string s)
{
	if (!s.empty() && s.back() == '\n')
		s.pop_back();
	return move(s);
}

void process(istream &in, ostream &out)
{
	int testcases_count;
	in >> testcases_count;
	vector<testcase_t> tests;
	for ( int i = 0; i < testcases_count; ++i )
	{
		testcase_t tc;
		int N;
		in >> tc.D >> N;
		for (int i = 0; i < N; ++i)
		{
			int K, S;
			in >> K >> S;
			tc.n.emplace_back(K, S);
		}
		tests.push_back( tc );
	}

	int id = 1;
	for (auto test : tests)
	{
		const auto solution = no_endl(solve(test));
		out << "Case #" << id << ": " << solution << endl;
		id++;
	}
}

int main( )
{
	//*
	process( ifstream( "sample.txt" ), cout );
	process( ifstream( "1.in" ), ofstream( "out.txt" )  );
	/*/
	//*/
}