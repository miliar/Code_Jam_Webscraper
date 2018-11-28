// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>

const double M_PI = 3.14159265358979323846;

using namespace std;

struct pancake
{
	int r;
	int h;
	double s;
};

bool sort_func2(pancake i, pancake j)
{
	return i.r > j.r;
}

bool sort_func3(pancake i, pancake j)
{
	return i.s > j.s;
}

double _s(int r1, int r2)
{
	return M_PI * (double)(r1-r2) * (double)(r1+r2);
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("a.in");
	ofstream out("a.out");

	int t;
	in >> t;
	for (int i = 0; i < t; i++)
	{
		int n,k;
		in >> n >> k;
		vector<pancake> p;
		int maxr = 0;
		int maxr_h = 0;
		for (int j = 0; j < n; j++)
		{
			pancake p1;
			in >> p1.r >> p1.h;
			p1.s = (double)2 * M_PI * (double)p1.r * (double)p1.h;
			p.push_back(p1);
		}
		sort(p.begin(), p.end(), sort_func3);

		vector<pancake> pp1;
		for (int j = 0; j < k; j++)
		{
			pp1.push_back(p[j]);
		}
		sort(pp1.begin(), pp1.end(), sort_func2);

		vector<pancake> pp2;
		for (int j = k; j < n; j++)
		{
			pp2.push_back(p[j]);
		}
		sort(pp2.begin(), pp2.end(), sort_func2);

		if (pp2.size() > 0)
		{
		double s1 = M_PI*(double)pp2[0].r*(double)pp2[0].r;
		double s2 = M_PI*(double)pp1[0].r*(double)pp1[0].r;

		if (s1 - s2 > p[k-1].s - pp2[0].s)
		{
			sort(pp1.begin(), pp1.end(), sort_func3);
			pp1[k-1].r = pp2[0].r;
			pp1[k-1].h = pp2[0].h;
			pp1[k-1].s = pp2[0].s;
			sort(pp1.begin(), pp1.end(), sort_func2);
		}
		}

		unsigned long long int_res = 0;
		long double result = 0;
		for (int j = 0; j < k-1; j++)
		{
			result += pp1[j].s + _s(pp1[j].r, pp1[j+1].r);
			unsigned long long r = result;
			result = result - r;
			int_res += r;
		}
		result += pp1[k-1].s + _s(pp1[k-1].r, 0);
		unsigned long long r = result;
			result = result - r;
			int_res += r;

		char str[64];
		sprintf(str, "%0.9lf", result);

		char str2[64];
		strcpy(str2, str+2);

		out << "Case #" << i+1 << ": " << int_res << "." << str2 << endl;
	}

	in.close();
	out.close();

	return 0;
}
