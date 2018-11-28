#include <stdio.h>
#include <string.h>
using namespace std;

char change(int tmp)
{
	if (tmp == -1)
		return 'a';
	else
		return tmp + '0';
}

char a[ 20 ];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, mark, k, w;
	while (~scanf("%d", &n))
	{
		k = 0;
		for (int i = 0; i < n; i++)
		{
			k++;
			mark = 0;
			scanf("%s", a);
			int m = strlen(a);
			for (int j = 1; j < m; j++)
			{
				if (mark == 1)
					a[j] = '9';
				else if (a[j - 1] - '0' > a[j] - '0')
				{
					w = j;
					mark = 1;
					int tmp = a[j - 1] - '0' - 1;
					a[j - 1] = change(tmp);
					a[j] = '9';
				}	
			}
			mark = 0;
			for (int j = w - 1; j > 0; j--)
			{
				//if (mark == 1)
				//	a[j] = '9';
				if (a[j - 1] - '0' > a[j] - '0')
				{
					mark = 1;
					int tmp = a[j - 1] - '0' - 1;
					a[j - 1] = change(tmp);
					a[j] = '9';
				}	
			}
			//printf("%d\n", w); 
			printf("Case #%d: ", k);
			if (a[0] == '0')
			{
				for (int j = 1; j < m; j++)
				{
					printf("%c", a[j]);	
				}
				printf("\n");
			}
			else
				printf("%s\n", a); 
		}
	}
}
