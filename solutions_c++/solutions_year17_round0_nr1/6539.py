#include <stdio.h>

int change, leng, ans;
char inp[1005];

int main()
{
	FILE* fp, *fpfp;
	fp = fopen("A-large.in", "r");
	fpfp = fopen("answer", "w");

	int t;
	fscanf(fp, "%d", &t);

	for(int a = 1; a <= t; a++)
	{
		ans = 0;

		fscanf(fp, "%s", inp);
		fscanf(fp, "%d", &change);

		for (int i = 0; ; i++)
		{
			if (ans < 0)
				break;

			if (inp[i] == '+');
			else if (inp[i] == '-')
			{
				ans++;
				for (int j = i; j < i + change; j++)
				{
					if (inp[j] != '+' && inp[j] != '-')
					{
						ans = -10000;
						break;
					}
					if (inp[j] == '+')
						inp[j] = '-';
					else
						inp[j] = '+';
				}
			}
			else
				break;
		}

		fprintf(fpfp, "Case #%d: ", a);

		if (ans < 0)
			fprintf(fpfp, "IMPOSSIBLE\n");
		else
			fprintf(fpfp, "%d\n", ans);
	}

	fclose(fp);
	fclose(fpfp);
}