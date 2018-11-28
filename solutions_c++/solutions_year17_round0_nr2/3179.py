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

long long tidy(long long n)
{

	long long nx = n / 10;
	long long res = n - 10 * nx;
	if (is_tidy(nx, res))
	{
		return n;
	}
	else {
		if (res < 9)
		{
			nx = tidy(nx - 1);
		}
		else {
			nx = tidy(nx);
		}
		
		return nx * 10 + 9;
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
		long long answ = tidy(n);
		fprintf(fout, "Case #%d: %lli\n", ti + 1, answ);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}