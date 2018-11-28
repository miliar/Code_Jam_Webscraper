#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stdlib.h>

using namespace std;

struct testcase_t
{
	vector<string> show;
};

int score( const vector<string>& show )
{
	int res = 0;
	for (auto& row : show )
		for ( auto& cell : row )
              res += cell == '.' ? 0 : cell == 'o' ? 2 : 1;
	return res;
}

int diff( const vector<string>& a, const vector<string>& b )
{
	int res = 0;
	auto n = a.size( );
	for ( size_t i = 0; i < n; ++i )
		for ( size_t j = 0; j < n; ++j )
			res += a[ i ][ j ] != b[ i ][ j ] ? 1 : 0;
	return res;
}

void set_rock(vector<string>& f, int col, int row)
{
	for (size_t i = 0; i < f.size(); ++i)
		f[i][row] = f[col][i] = '*';
	f[col][row] = 'R';
}

void set_bishop(vector<string>& f, int col, int row)
{
	f[col][row] = 'B';
	int dx = 1;
	int dy = 1;
	for (int k = 0; k < 4; ++k)
	{
		swap(dx, dy);
		dx *= -1;
		int c = col;
		int r = row;
		for (int i = 0; i < f.size(); ++i)
		{
			c += dx;
			r += dy;
			if (c < 0 || c >= f.size() || r < 0 || r >= f.size()) break;
			f[c][r] = '*';
		}
	}
}

void fill(vector<string>& show)
{
	const auto n = show.size();
	vector<string> bishops(n, string(n, '.'));
	vector<string> rocks(n, string(n, '.'));

	for (size_t c = 0; c < n; ++c)
		for (size_t r = 0; r < n; ++r)
		{
			const char ch = show[c][r];
			if (ch == 'x' || ch == 'o')
				set_rock(rocks, c, r);
			if (ch == '+' || ch == 'o')
				set_bishop(bishops, c, r);
		}

	for (size_t c = 0; c < n; ++c)
		for (size_t r = 0; r < n; ++r)
		{
			if (rocks[c][r] == '.')
				set_rock(rocks, c, r);
		}
	for (size_t c = 0; c < n; ++c)
	{
		if (bishops[c][0] == '.')
			set_bishop(bishops, c, 0);
		if (bishops[0][c] == '.')
			set_bishop(bishops, 0, c);
		if (bishops[c][n - 1] == '.')
			set_bishop(bishops, c, n - 1);
		if (bishops[n - 1][c] == '.')
			set_bishop(bishops, n - 1, c);
	}


	for (size_t c = 0; c < n; ++c)
		for (size_t r = 0; r < n; ++r)
		{
			bool rock = rocks[c][r] == 'R';
			bool bishop = bishops[c][r] == 'B';
			if (rock && bishop)
				show[c][r] = 'o';
			else if (rock)
				show[c][r] = 'x';
			else if (bishop)
				show[c][r] = '+';
		}
}

string solve( const testcase_t& test )
{
	stringstream out;
	auto show = test.show;

	fill( show );

	int points = score( show );
	int extra_modes = diff( show, test.show);
	out << points << " " << extra_modes << endl;

	auto n = show.size( );
	for ( size_t i = 0; i < n; ++i )
		for ( size_t j = 0; j < n; ++j )
			if ( show[ i ][ j ] != test.show[ i ][ j ] )
				out << show[ i ][ j ] << " " << ( i + 1 ) << " " << ( j + 1 ) << endl;

	return out.str( );
}

void process(istream &in, ostream &out, ostream &out2)
{
	int testcases_count;
	in >> testcases_count;
	vector<testcase_t> tests;
	for ( int i = 0; i < testcases_count; ++i )
	{
		int N, M;
		in >> N >> M;
		auto show = vector<string>( N, string( N, '.' ) );

		for ( int i = 0; i < M; ++i )
		{
			string ch;
			int x, y;
			in >> ch >> x >> y;
			show[ x - 1 ][ y - 1 ] = ch[ 0 ];
		}

		testcase_t tc;
		tc.show = show;
		tests.push_back( tc );
	}

	int id = 1;
	for ( auto test : tests )
	{
		const auto solution = solve( test );
		out << "Case #" << id << ": " << solution;
		out2 << "Case #" << id << ": " << solution;
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