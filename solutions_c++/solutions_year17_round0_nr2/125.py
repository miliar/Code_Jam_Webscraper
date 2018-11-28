#include<stdio.h>
int n, m;
char a[100009];
int main()
{
//	freopen("B-small-attempt0.in", "rt", stdin);
//	freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	
	int t, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%s", a);
		for (n = 0; a[n]; n++);
		j = 0;
		for (i = 0; i + 1 < n; i++)
			if (a[i] > a[i + 1])
				break;
		if (i + 1 < n)
		{
			//NOTE : a[i] cannot be zero.
			for (j = i; j >= 0; j--)if (a[j] != a[i])break;
			a[j + 1]--;
			for (j = j + 2; j < n; j++)
				a[j] = '9';
		}
		j = 0;
		while (j < n && a[j] == '0')j++;
		printf("Case #%d: %s\n", ++tv, &a[j]);
	}
}