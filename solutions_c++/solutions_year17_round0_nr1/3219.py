#include <cstdio>
#include <string>
#include <vector>
#include <map>
using namespace std;

int solve(string &str, int K) {
	char opposite = '-';
	int flip = 0;
	for (int i = 0; i <= str.size() - K; ++i)
	{
		if (str[i] == '-')
		{
			++flip;
			for (int j = i; j < i + K; ++j)
			{
				if (str[j] == '-')
				{
					str[j] = '+';
				}
				else if (str[j] == '+')
				{
					str[j] = '-';
				}
			}
		}
	}
	int st = ((str.size() - K) < 0) ? 0 : str.size() - K;
	bool res = true;
	for (int i = st; i < str.size(); ++i)
	{
		if (str[i] == '-') {
			res = false;
			return -1;
		}
	}
	return flip;
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
		char str[1010];
		fscanf(fin, "%s", str);
		//	fin >> str;
		int k;
		fscanf(fin, "%d", &k);
		int res = solve(string(str), k);
		if (res != -1)
		{
			fprintf(fout, "Case #%d: %i\n", ti + 1, res);
		}
		else {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", ti + 1);
		}

	}
	fclose(fin);
	fclose(fout);
	return 0;
}