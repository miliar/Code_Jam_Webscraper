// sof_paper_solution.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "opencv\cv.h"
#include "opencv\highgui.h"

#include <iostream>
#include <bitset>

#include <fstream>
#include <iostream>
#include <string>


using namespace std;

int sum(vector<int> const& vec)
{
	int sum = 0;
	for (auto el : vec)
		sum += el;
	return sum;
}

int num_plus(vector<int> const& vec)
{
	return sum(vec);
}

int num_minus(vector<int> const& vec)
{
	return vec.size() - sum(vec);
}

struct Case
{
	vector<int> data;
	int flen; // flipper length
};

static const int Impossible = -1;

int analyze_case(Case const& c)
{
	// Simple cases
	// all + : solution           0
	// count(-) % len != 0        IMPOSSSIBLE

	auto npanc = c.data.size();
	
	if (num_plus(c.data) == npanc)
	{
		return 0;
	}

	// we can always flip the first pancake correctly
	// if 0, flip.
	// move so that start is at second pancake
	
	auto pancakes = c.data;
	auto len = c.flen;
	

	int n = npanc - c.flen;
	
	int count = 0;
	for (int i = 0; i <= n; ++i)
	{
		if (pancakes[i]) continue;

		for (int j = i; j < i + len; ++j)
		{
			pancakes[j] = !(pancakes[j]);
		}

		++count;
	}

	if (num_plus(pancakes) == pancakes.size())
	{
		return count;
	}
	else
	{
		return Impossible;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;

	fstream file("A-large.in");

	string line;
	getline(file, line);

	int ncases = stoi(line);

	vector <Case> cases;
	while (getline(file, line))
	{
		istringstream line_stream(line);

		string pancks;
		line_stream >> pancks;

		int len;
		line_stream >> len;

		istringstream panck_data_stream(pancks);
		
		char c;
		vector<int> data;
		while (panck_data_stream >> c)
		{
			data.push_back(c == '+' ? 1 : 0);
		}

		cases.push_back({ data, len });
	}

	ofstream out;
	out.open("A-large.out");

	for (int i = 0; i < cases.size(); ++i)
	{
		int res = analyze_case(cases[i]);


		string header = "Case #" + to_string(i + 1) + ": ";
		out << header;

		if (res >= 0)
			out << res;
		else
			out << string("IMPOSSIBLE");
		
		out << endl;
	}
	out.close();

	return 0;
}
