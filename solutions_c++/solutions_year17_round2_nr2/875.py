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
	int N;
	int R, O, Y, G, B, V;
};

string pair_color(char C1, char C2, int& n1, int& n2)
{
	string c;
	if (n1 > 0)
	{
		c.push_back(C2);
		n2--;
	}
	while (n1 > 0)
	{
		c.push_back(C1);
		c.push_back(C2);
		n1--;
		n2--;
	}
	return c;
}

bool test(int a, int b, int N)
{
	return a == b && (a + b) == N;
}

string repeate(int n, string s)
{
	string r;
	for (int i = 0; i < n; ++i)
		r += s;
	return r;
}

string solve( testcase_t t )
{
	// red, yellow, blue
	// orange = red + yellow
	// green = yelow+ blue
	// violet = red + blue
	if (test(t.O, t.B, t.N)) return repeate(t.O, "OB");
	if (test(t.G, t.R, t.N)) return repeate(t.G, "GR");
	if (test(t.V, t.Y, t.N)) return repeate(t.V, "VY");
	string orange = pair_color('O', 'B', t.O, t.B);
	string green = pair_color('G', 'R', t.G, t.R);
	string violet = pair_color('V', 'Y', t.V, t.Y);
	if (t.B < 0 || t.R < 0 || t.Y<0)
		return "IMPOSSIBLE";

	int r = t.R + !green.empty();
	int y = t.Y + !violet.empty();
	int b = t.B + !orange.empty();

	int max_color = max(r, max(y, b));
	int sum = r + y + b;
	if (max_color > sum / 2)
		return "IMPOSSIBLE";

	r = t.R;
	y = t.Y;
	b = t.B;

	vector<vector<string>> colors;
	colors.emplace_back(r, "R");
	colors.emplace_back(y, "Y");
	colors.emplace_back(b, "B");
	if (!green.empty())
		colors[0].push_back(green);
	if (!violet.empty())
		colors[1].push_back(violet);
	if (!orange.empty())
		colors[2].push_back(orange);

	sort(colors.begin(), colors.end(), [](const vector<string>& a, const vector<string>& b)
		{return a.size() > b.size(); });

	string result;

	char last_color = 'X';
	for (;;)
	{
		vector<string>* best = nullptr;
		size_t best_size = 0;
		for (auto& c : colors)
		{
			if (c.size() > best_size && c[0][0] != last_color)
			{
				best = &c;
				best_size = c.size();
			}
		}
		if (best != nullptr)
		{
			last_color = best->back()[0];
			result += best->back();
			best->pop_back();
			continue;
		}
		if (result.size()!= t.N)
			return "IMPOSSIBLE";
		if (result.front() == result.back())
			return "IMPOSSIBLE";
		break;
	}
	return result;
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
		in >> tc.N >> tc.R >> tc.O >> tc.Y >> tc.G >> tc.B >> tc.V;
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