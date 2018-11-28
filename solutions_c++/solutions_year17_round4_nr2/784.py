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
	string filename = "B-small-attempt0";
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
		int n, c, m;
		fscanf(in, "%d %d %d", &n, &c, &m);
		vector<int> p(m), b(m), at(n, 0), ctick(c, 0);
		for (int i = 0; i<m; ++i)
		{
			fscanf(in, "%d", &p[i]);
			fscanf(in, "%d", &b[i]);
			--p[i]; --b[i];
			++at[p[i]];
			++ctick[b[i]];
		}
		int rides = 0, proms = 0;
		int R = 0;
		for (int i = 0; i < c; ++i)
		{
			R = std::max(R, ctick[i]);		
		}
		for (int i = 0; i < n; ++i)
		{
			rides = std::max(rides, at[i]);
		}
		R = std::max(R, at[0]);
		rides = std::max(rides, R);
		vector<int> orAt = at;

		bool ending = false;
		for (; rides > R; --rides)
		{
			int free = n - 1;
			for (; free >= 0; --free)
			{
				if (at[free] < rides)
					break;
			}
			for (int i = n - 1; i >= 0; --i)
			{
				if (at[i] > rides)
				{
					int surp = at[i] - rides;
					at[i] = rides;

					if (free > i)
					{
						free = i - 1;
						for (; free >= 0; --free)
						{
							if (at[free] < rides)
								break;
						}
					}
					if (free == -1)
					{
						ending = true;
						break;
					}
					while (surp > 0)
					{
						if (rides - at[free] > surp)
						{
							at[free] += surp;
							surp = 0;
						}
						else if (rides - at[free] == surp)
						{
							at[free] += surp;
							surp = 0;
							for (; free >= 0; --free)
							{
								if (at[free] < rides)
									break;
							}
						}
						else
						{
							surp -= rides - at[free];
							at[free] = rides;
							for (; free >= 0; --free)
							{
								if (at[free] < rides)
									break;
							}
							if (free == -1)
							{
								ending = true;
								break;
							}
						}
					}
					if (ending)
					{
						break;
					}
				}
			}
			if (ending)
			{
				break;
			}
		}
		if (ending)
			++rides;

		if (rides < R)
			rides = R;

		for (int i = 0; i < n; ++i)
		{
			if (orAt[i] > rides)
			{
				proms += orAt[i] - rides;
			}
		}

		fprintf(out, "Case #%d: %d %d\n", t + 1, rides, proms);
		cout << t << endl;
	}

	fclose(in);
	fclose(out);
	return 0;
}

