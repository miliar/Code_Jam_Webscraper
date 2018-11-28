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
		int n, p;
		fscanf(in, "%d %d", &n, &p);
		vector<int> g(n);
		vector<int> mds(4, 0);
		for (int i = 0; i<n; ++i)
		{
			fscanf(in, "%d", &g[i]);
			++mds[g[i] % p];
		}

		int goods = 0;
		goods = mds[0];
		if (p == 2)
		{
			goods += mds[1] / 2;
			if (mds[1] % 2 == 1)
				++goods;
		}
		if (p == 3)
		{
			int min = std::min(mds[1], mds[2]);
			goods += min;
			mds[1] -= min;
			mds[2] -= min;
			if (mds[1] > 0)
			{
				goods += mds[1] / 3;
				if (mds[1] % 3 != 0)
					++goods;
			}
			if (mds[2] > 0)
			{
				goods += mds[2] / 3;
				if (mds[2] % 3 != 0)
					++goods;
			}
		}
		if (p == 4)
		{
			goods += mds[2] / 2;
			mds[2] = mds[2] % 2;

			int min = std::min(mds[1], mds[3]);
			goods += min;
			mds[1] -= min;
			mds[3] -= min;


			if (mds[3] > 0)
				mds[1] = mds[3];

			if (mds[2] == 1)
			{
				if (mds[1] >= 2)
				{
					++goods;
					mds[1] -= 2;
				}
				else
				{
					++goods;
					mds[1] = 0;
				}
			}

			if (mds[1] > 0)
			{
				goods += mds[1] / 4;
				if (mds[1] % 4 != 0)
					++goods;
			}
		}

		fprintf(out, "Case #%d: %d\n", t + 1, goods);
		cout << t << endl;
	}

	fclose(in);
	fclose(out);
	return 0;
}

