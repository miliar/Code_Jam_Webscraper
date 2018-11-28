// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

struct horse
{
	double dist;
	int speed;
};

bool sort_func (horse i,horse j) { return (i.dist>j.dist); }

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("a.in");
	ofstream out("a.out");

	int t;
	in >> t;
	for (int i = 0; i < t; i++)
	{
		double d;
		int n;
		in >> d >> n;
		double result = 0;

		vector<horse> horses;
		for (int j = 0; j < n; j++)
		{
			double k;
			int s;
			in >> k >> s;
			horse h;
			h.dist = d-k;
			h.speed = s;
			horses.push_back(h);
		}

		if (horses.size() > 1)
			sort(horses.begin(), horses.end(), sort_func);
		
		for (int j = n - 1; j >= 0; j--)
		{
			double cur_time = horses[j].dist / horses[j].speed;
			if (cur_time > result)
				result = cur_time;
		}

		out << "Case #" << i+1 << ": " << fixed << setprecision(6) << d/result << endl;
	}

	in.close();
	out.close();

	return 0;
}

