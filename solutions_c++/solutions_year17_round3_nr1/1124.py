#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;
struct pancake
{
	double h;
	double r;
	double sa;
};
int main(int argc, char *argv[])
{
	FILE *fin, *fout;
	if (argc > 1)
	{
		char tname[200];
		fin = fopen(argv[1], "r");
		strncpy(tname, argv[1], 200);
		strncpy(strstr(tname, ".in"), ".out", 4);
		fout = fopen(tname, "w");
	}
	else {
		fin = fopen("A.in", "r");
		fout = fopen("A.out", "w");
	}


	int t;
	fscanf(fin, "%d", &t);
	pancake pks[1000];
	for (int ti = 0; ti<t; ti++)
	{
		int n, k;
		fscanf(fin, "%d", &n);
		fscanf(fin, "%d", &k);
		for (int i = 0; i < n; ++i)
		{
			double tr, th, tsa;
			fscanf(fin, "%lf", &tr);
			fscanf(fin, "%lf", &th);
			pks[i].r = tr;
			pks[i].h = th;
			pks[i].sa = 2*th*tr;
		}
		sort(pks, pks + n, [](pancake i, pancake j) {return i.sa > j.sa; });
		int i0 = n-1;
		double rm0 = 0;

		for (int i = 0; i < k; ++i)
		{
			if (pks[i].r > rm0)
			{
				rm0 = pks[i].r;
			}
		}
		for (int i = k; i < n; ++i)
		{
			if (pks[i].r > rm0)
			{

				if (pks[i].r*pks[i].r + pks[i].sa > rm0*rm0 + pks[k - 1].sa)
				{
					rm0 = pks[i].r;
					pks[k - 1] = pks[i];
				}
			}
		}
		double fsa = rm0*rm0;
		for (int i = 0; i < k; ++i) fsa += pks[i].sa;
		fprintf(fout, "Case #%d: %.8lf\n", ti + 1, fsa*3.1415926535897932384626433832795);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}