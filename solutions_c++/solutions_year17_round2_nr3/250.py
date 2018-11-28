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
	string filename = "C-large";
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
		int n, q;
		fscanf(in, "%d %d", &n, &q);
		vector<int> e(n), s(n);
		for (int i = 0; i<n; ++i)
		{
			fscanf(in, "%d %d", &e[i], &s[i]);
		}
		vector< vector<int> > AdjMat(n, vector<int>(n));
		for (int i = 0; i<n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				fscanf(in, "%d", &AdjMat[i][j]);
			}	
		}
		vector<int> u(q), v(q);
		for (int i = 0; i<q; ++i)
		{
			fscanf(in, "%d %d", &u[i], &v[i]);
			--u[i];
			--v[i];
		}

		std::vector< std::vector<double> > DistMtx(n, std::vector<double>(n, 99999999999.0));
		for (int i = 0; i<n; ++i)
		{
			vector<bool> pr(n);
			DistMtx[i][i] = 0;
			while (true)
			{
				int chosen = -1;
				for (int j = 0; j < n; ++j)
				{
					if (!pr[j] && (chosen == -1 || DistMtx[i][j] < DistMtx[i][chosen]))
						chosen = j;
				}
				if (chosen == -1)
					break;
				pr[chosen] = true;
				for (int j = 0; j < n; ++j)
				{
					if (pr[j])
						continue;
					if (AdjMat[chosen][j] > -1 && DistMtx[i][chosen] + AdjMat[chosen][j] < DistMtx[i][j])
					{
						DistMtx[i][j] = DistMtx[i][chosen] + AdjMat[chosen][j];
					}
				}
			}
		}

		cout << t << endl;
		fprintf(out, "Case #%d: ", t + 1);

		for (int i = 0; i<q; ++i)
		{
			vector< double > time(n, 99999999999.0);
			vector< vector<double> > bestTime(n, vector<double>(n, 99999999999.0));
			vector< vector<double> > remain(n, vector<double>(n, 99999999999.0));
			vector<bool> proc(n, false);

			time[u[i]] = 0;
			bestTime[u[i]][u[i]] = 0;
			remain[u[i]][u[i]] = e[u[i]];
			while (true)
			{
				int chosen = -1;
				for (int j = 0; j < n; ++j)
				{
					if (!proc[j] && (chosen == -1 || time[j] < time[chosen]))
						chosen = j;
				}
				if (chosen < 0 || chosen == v[i])
					break;

				proc[chosen] = true;
				bestTime[chosen][chosen] = time[chosen];
				remain[chosen][chosen] = e[chosen];
				for (int j = 0; j < n; ++j)
				{
					if (proc[j])
						continue;

					if (DistMtx[chosen][j] > 99999999000.0)
						continue;

					for (int h = 0; h < n; ++h)
					{
						if (bestTime[chosen][h] > 99999999000.0)
							continue;

						if (bestTime[chosen][h] + DistMtx[chosen][j] / s[h] < bestTime[j][h]
							&& remain[chosen][h] >= DistMtx[chosen][j])
						{
							bestTime[j][h] = bestTime[chosen][h] + DistMtx[chosen][j] / s[h];
							remain[j][h] = remain[chosen][h] - DistMtx[chosen][j];
							if (time[j] > bestTime[j][h])
								time[j] = bestTime[j][h];
						}
					}
				}
			}
			fprintf(out, "%f ", time[v[i]]);
		}

		fprintf(out, "\n");
	}

	fclose(in);
	fclose(out);
	return 0;
}



