#include <stdio.h>

int main()
{
	FILE* fp, *ans;
	fp = fopen("B-large.in", "r");
	ans = fopen("answer", "w");

	int t;
	fscanf(fp, "%d", &t);

	for(int a = 1; a <= t; a++)
	{
		char num[20] = { '\0', };
		fscanf(fp, "%s", num);

		int pre = 0;

		for (int i = 1; num[i] != '\0'; i++)
		{
			if (num[i] == num[pre])
				continue;
			else if (num[pre] < num[i])
				pre = i;
			else
			{
				num[pre] -= 1;
				for (i = pre + 1; num[i] != '\0'; i++)
					num[i] = '9';
			}
		}
		
		fprintf(ans, "Case #%d: ", a);
		if ('1' <= num[0] && num[0] <= '9')
			fprintf(ans, "%c", num[0]);
		fprintf(ans, "%s\n", num + 1);
	}

	fclose(fp);
	fclose(ans);
}