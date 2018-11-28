#include <stdio.h>
#include <string.h>
#include <vector>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS

int main()
{
	char S[1002];
	int k;
	int n;
	vector <char> ans[101];
	FILE *fp, *fpp;
	fpp = fopen("output.txt", "wt");

	fp = freopen("A-large.in", "rt", stdin);
	scanf("%d", &n);

	for(int T = 1; T <= n; T++)
	{
		scanf("%s %d", S, &k);
		int count = 0;
		for (int i = 0; i + k <= strlen(S); i++)
		{
			if (S[i] == '-')
			{
				count++;
				for (int j = i; j < i + k; j++)
				{
					if (S[j] == '-')
						S[j] = '+';
					else
						S[j] = '-';
				}
			}
		}
		int chk = 0;
		for (int i = 0; i < strlen(S); i++)
		{
			if (S[i] == '-')
			{
				chk = 1;
				break;
			}
		}
		if (chk)
			fprintf(fpp, "Case #%d: IMPOSSIBLE\n", T);
		else
			fprintf(fpp, "Case #%d: %d\n", T, count);
	}
	fclose(fpp);
	fclose(fp);
	return 0;
}