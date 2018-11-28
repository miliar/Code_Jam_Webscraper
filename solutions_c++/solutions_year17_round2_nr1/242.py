#include "stdafx.h"
#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string.h>
#include <algorithm>

typedef long long int LL;

using namespace std;

int main()
{
	FILE* in, *out;
	string filename = "A-large";
	string infilename = filename, outfilename = filename;
	infilename += ".in";
	outfilename += ".out";
	if ((in = fopen(infilename.c_str(), "rt")) == NULL)
	{
		cout << "Input file not found." << endl;
		getchar();
		return 1;
	}
	if ((out = fopen(outfilename.c_str(), "wt")) == NULL)
	{
		cout << "Cannot create output file." << endl;
		getchar();
		return 2;
	}

	int T;
	fscanf(in, "%d", &T);

	for (int t = 0; t != T; ++t)
	{
		int d, n;
		fscanf(in, "%d %d", &d, &n);
		vector<int> sp(n), pos(n);
		for (int i = 0; i<n; ++i)
		{
			fscanf(in, "%d %d", &pos[i], &sp[i]);
		}

		double bestArrival = -1.0;
		for (int i = 0; i<n; ++i)
		{
			double arrival = ((double)d - (double)pos[i]) / (double) sp[i];
			if (bestArrival<0 || arrival > bestArrival)
			{
				bestArrival = arrival;
			}
		}
		double speed = (double)d / bestArrival;

		fprintf(out, "Case #%d: %lf\n", t+1, speed);
	}

	fclose(in);
	fclose(out);
	return 0;
}

