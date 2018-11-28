#include<cstdio>

using namespace std;

char num[25];

int T;

int main()
{
	scanf("%d",&T);
	for (int t = 1; t <= T; t ++)
	{
		scanf("%s",num);
		int len = 0;
		while (num[len]) len ++;
		int last = '9';
		for (int i = len - 1; i >= 0; i --)
		{
			if (num[i] <= last)
				last = num[i];
			else 
			{
				num[i] --;
				for (int j = i + 1; j <= len - 1; j ++)
					num[j] = '9';
				last = num[i];
			}
		}
		while (num[0] == '0')
		{
			for (int i = 0; i <= len - 1; i ++)
				num[i] = num[i + 1];
			len --;
		}
		printf("Case #%d: %s\n",t,num);
	}
	return 0;
}