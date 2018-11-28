#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

bool is_tidy(long long n, long long lastd)
{
	if (n < 10) return n <= lastd;
	long long nn = n / 10;
	long long res = n - 10 * nn;
	if (res > lastd) return false;
	return is_tidy(nn, res);
}

long long make_tidy(long long n)
{
	
	long long nn = n / 10;
	long long res = n - 10 * nn;
	if (is_tidy(nn, res))
	{
		return n;
	}
	else {
		nn = make_tidy(nn - 1);
		return nn * 10 + 9;
	}
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
		long long n;
		fscanf(fin, "%lli", &n);
		long long answ = make_tidy(n);
		fprintf(fout, "Case #%d: %lli\n", ti + 1, answ);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}