#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int n;
int k;
char s[2000];
int x[2000];

int main(int argc, char *argv[])
{
	if (argc == 1)
	{
		freopen("in", "r", stdin);
		freopen("out","w",stdout);
	}
	else
	{
		if (freopen(argv[1], "r",stdin) == NULL)
		{
			cerr << "open file failed" << endl;
			return 0;
		}
		freopen("ans","w",stdout);
	}
	scanf("%d", &n);
	for (int T = 1;T <= n;++ T)
	{
		scanf("%s", s);
		scanf("%d", &k);
		int len = strlen(s);
		for (int i = 0;i < len;++ i)
			x[i] = (s[i]=='+')?1:0;
		int ans = 0;
		cerr << len-k << endl;
		for (int i = 0;i <= len - k;++ i)
		{
			if (!x[i])
			{
				++ ans;
				for (int j = i;j < i + k;++ j)
					x[j] ^= 1;
			}
		}
		bool ok = 1;
		for (int i = 0;i < len;++ i)
			if (!x[i])
			{
				ok = 0;
				break;
			}

		printf("Case #%d: ", T);
		if (ok)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
