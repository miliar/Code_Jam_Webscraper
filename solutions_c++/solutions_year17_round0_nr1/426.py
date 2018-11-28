#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <vector>

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

	for (int ti = 0; ti<t; ti++)
	{
		char str[1010];
		fscanf(fin, "%s", str);
	//	fin >> str;
		int k;
		fscanf(fin, "%d", &k);
		char opposite = '-';
		int len = strlen(str);
		int flip = 0;
		for (int i = 0; i <= len-k; ++i)
		{
			if (str[i] == '-')
			{
				++flip;
				for (int j = i; j < i + k; ++j)
				{
					if (str[j] == '-')
					{
						str[j] = '+';
					} else if (str[j] == '+')
					{
						str[j] = '-';
					}
				}
			}
		}
		int st = ((len - k) < 0) ? 0 : len - k;
		bool res = true;
		for (int i = st; i < len; ++i)
		{
			if (str[i] == '-') res = false;
		}
	//	for (int i = 0; i<n; ++i) fscanf(fin, "%lf", prob + i);

		if (res)
		{
			fprintf(fout, "Case #%d: %i\n", ti + 1, flip);
		}
		else {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", ti + 1, flip);
		}

	}
	fclose(fin);
	fclose(fout);
	return 0;
}