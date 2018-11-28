#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;
long long intv(long long stalls, long long men)
{
	long long p2 = 1;
	while ((1LL << p2) <= men) ++p2;
	--p2;
	long long div = ((stalls + 1LL) >> p2) - 1LL;
	long long rem = stalls + 1LL - ((div+1) << p2);
	long long menrem = men + 1 - (1LL << p2);
	if (rem >= menrem) return div+1LL;
	return div;
}
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

	for (int ti = 0; ti<t; ti++)
	{
		long long n, k;
		fscanf(fin, "%lli", &n);
		fscanf(fin, "%lli", &k);

		//	for (int i = 0; i<n; ++i) fscanf(fin, "%lf", prob + i);
		long long answ = intv(n,k) - 1;
		long long answ2 = answ >> 1;
		fprintf(fout, "Case #%d: %lli %lli\n", ti + 1, answ-answ2, answ2);

	}
	fclose(fin);
	fclose(fout);
	return 0;
}