// sof_paper_solution.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>

#include <fstream>
#include <iostream>
#include <string>

#include <vector>


using namespace std;
typedef long long int64;

vector<int64> digits(int64 num)
{
	vector<int64> dgs;
	while (num)
	{
		dgs.push_back(num % 10);
		num /= 10;
	}
	return dgs;
}

int64 untidiness_pos(int64 num)
{
	auto dgs = digits(num);

	int64 prev = dgs[0];
	int64 pos = -1;
	for (int64 i = 0; i < dgs.size(); ++i)
	{
		if (dgs[i] > prev)
		{
			pos = i;
		}

		prev = dgs[i];
	}

	return pos;
}

int64 last_tidy_try(int64 num)
{
	int untpos = untidiness_pos(num);

	if (untpos == -1) return num;

	int64 fc = pow(10, untpos);

	return num - num % fc - 1;

}

int64 last_tidy(int64 num)
{
	int64 prev_res = last_tidy_try(num);
	while (1)
	{
		int64 next_res = last_tidy_try(prev_res);
		if (next_res == prev_res)
		{
			return next_res;
		}
		prev_res = next_res;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream file("B-large.in");

	int64 nsamples;
	file >> nsamples;

	vector <int64> numbers;
	int64 number;
	while (file >> number)
	{
		numbers.push_back(number);	
	}

	ofstream out;
	out.open("B-large.out");

	for (int i = 0; i < numbers.size(); ++i)
	{
		int64 res = last_tidy(numbers[i]);

		string header = "Case #" + to_string(i + 1) + ": ";
		out << header << res << endl;
	}
	out.close();

	return 0;
}
