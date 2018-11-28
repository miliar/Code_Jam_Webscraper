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
	double pos[1000];
	double speed[1000];
	double arrive[1000];
	for (int ti = 0; ti<t; ti++)
	{
		double dest;
		int n;
		fscanf(fin, "%lf", &dest);
		fscanf(fin, "%d", &n);
		for (int i = 0; i < n; ++i)
		{
			fscanf(fin, "%lf", pos + i);
			fscanf(fin, "%lf", speed + i);
			arrive[i] = (dest - pos[i]) / speed[i];
		}
		sort(arrive, arrive + n);

		fprintf(fout, "Case #%d: %.6lf\n", ti + 1, dest / arrive[n - 1]);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}