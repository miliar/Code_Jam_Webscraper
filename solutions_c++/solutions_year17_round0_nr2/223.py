#include<cstdio>
#include<cstring>
char a[32], b[32];
int n;
int main()
{
	int i, k;
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		scanf("%s", a);
		n = strlen(a);
		bool flag = false;
		for (i = 1; i < n; i++) { if (a[i - 1] > a[i]) { flag = true; break; } }
		printf("Case #%d: ", t);
		if (!flag)
		{
			printf("%s\n", a);
			continue;
		}
		for (k = n - 1; k >= 0; k--)
		{
			if (a[k] == '0') continue;
			bool flag = false;
			for (i = 1; i < k; i++) { if (a[i - 1] > a[i]) { flag = true; break; } }
			if (flag) continue;
			if (k > 0 && a[k - 1] > a[k] - 1) continue;
			strcpy(b, a);
			b[k]--;
			for (i = k + 1; i < n; i++) b[i] = '9';
			for (i = 0; b[i] == '0'; i++);
			printf("%s\n", &b[i]);
			break;
		}
	}
	return 0;
}
