// BathroomStalls.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <list>
#include <map>

typedef unsigned long long ullong;

using namespace std;

ullong PowerOf2(ullong nr)
{
	ullong ret = 1;
	
	while (ret < nr)
	{
		ret <<= 1;
	}

	if (ret == nr)
	{
		return ret;
	}

	return (ret / 2);
}

struct Pair
{
	Pair(ullong v1, ullong v2)
	{
		if (v1 > v2)
		{
			max = v1;
			min = v2;
		}
		else
		{
			max = v2;
			min = v1;
		}
	}

	ullong min, max;
};

int main()
{
	FILE *fin, *fout;
	int T;
	ullong N, K, L, I, pow;

	int startingIndex;

	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");

	if (!fin || !fout)
	{
		return 1;
	}

	fscanf(fin, "%d", &T);

	for (int i = 1; i <= T; ++i)
	{
		fscanf(fin, "%llu %llu", &N, &K);

		pow = PowerOf2(K);
		I = pow + ((N - pow + 1) % pow);
		if (K < I || I == pow)
		{
			L = N / pow;
		}
		else
		{
			L = N / pow - 1;
		}

		I = (L - 1) / 2;

		Pair p(I, L - I - 1);

		fprintf(fout, "Case #%d: %llu %llu\n", i, p.max, p.min);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}

