#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <ctype.h>
#include <algorithm>
#include <iomanip>
#include <fstream>

using namespace std;

typedef long long ll;

ifstream in("in.in");
ofstream out("out.out");


struct P
{
	long double R;
	long double H;
};

P p[1000];

bool cmp(P a, P b)
{
	return a.H * a.R > b.H * b.R;
};

void func()
{
	int N, K;
	in >> N >> K;

	long double maxR = 0;

	for (int i = 0; i < N; i++)
	{
		in >> p[i].R >> p[i].H;
	}

	sort(p, p + N, cmp);

	long double total = 0;
	long double best_total = total;

	for (int i = 0; i < N; i++)
	{
		total = M_PI * 2.0 * p[i].H * p[i].R;
		maxR = p[i].R;
		int t = 1;
		for (int j = 0; t < K; j++)
		{
			if (j == i) continue;
			total += M_PI * 2.0 * p[j].H * p[j].R;
			if (p[j].R > maxR)
				maxR = p[j].R;
			t++;
		}

		total += M_PI * maxR * maxR;		
		if (total > best_total)
			best_total = total;
	}

	out << best_total;
}

int main()
{
	out << fixed << setprecision(10);
	ios_base::sync_with_stdio(false);
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i)
	{
		out << "Case #" << i << ": ";
		func();
		out << endl;
	}
	return 0;
}