#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

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
	double ppi[50];
	for (int ti = 0; ti<t; ti++)
	{
		int n, k;
		fscanf(fin, "%d", &n);
		fscanf(fin, "%d", &k);
		double u;
		fscanf(fin, "%lf", &u);
		for (int i = 0; i < n; ++i)
		{
			fscanf(fin, "%lf", ppi+i);
		}
		sort(ppi, ppi + n);
		int nt = 0;
		double avp = u + ppi[0];
		
		for (int i = 1; i < n; ++i)
		{
			double navp = (i*avp + ppi[i])/(i+1);
			if (ppi[i] > navp ) break;
			avp = navp;
		}
		for (int i = 0; i<n && ppi[i] < avp; ++i) ppi[i] = avp;
		
		double totprob = 1;
		if (avp < 1)
		{
			for (int i = 0; i < n; ++i) totprob *= ppi[i];
		}

		
		fprintf(fout, "Case #%d: %le\n", ti + 1, totprob);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}