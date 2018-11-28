
#include <stdio.h>
#include <string.h>

void tidy_calc(char *a, int start, int end)
{
	if (start < 0)
	{
		return;
	}

	for (int i = start; i <= end; i++)
	{
		if (a[i] > a[i+1] && i+1 <= end)
		{
			a[i] = a[i]-1;
			for (int j = i+1; j <= end; j++)
			{
				a[j] = '9';
			}

			tidy_calc(a, i-1, i);
			break;
		}

	}
}

int main()
{
	char a[1000+1];
	int T = 0;
	scanf("%d", &T);
	int len = 0;
	for (int k = 0; k < T; k++)
	{
		scanf("%s", a);
		/* Strip of the leading zeros */
		tidy_calc(a,0,strlen(a)-1);
		printf("Case #%d: ", k+1);
		
		for(int i = 0; i < strlen(a); i++)
		{
			if (a[i] != '0')
			{
				printf("%c", a[i]);
			}
		}
		printf("\n");
	}
}
