#include <bits/stdc++.h>
using namespace std;
const int N = 2010;
typedef long long ll;
int mod = 1000000007;
char s[N];
void run()
{
	int k, n, cnt = 0;
	scanf("%s%d", s, &k);
	n = strlen(s);
	for (int i = 0; i <= n - k; i++)
		if (s[i] == '-')
		{
			cnt++;
			for (int j = 0; j < k; j++)
				if (s[j + i] == '-')
					s[j + i] = '+';
				else if (s[j + i] == '+')
					s[j + i] = '-';
		}
	bool flag = true;
	for (int i = n - k + 1; i < n; i++)
	{	
		if (s[i] == '-')
		{
			flag = false;
			break;
		}
	}
	if (flag)
		printf("%d\n", cnt);
	else
		puts("IMPOSSIBLE");
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 1;
	scanf("%d", &T);
	while (T--)
	{ 
		printf("Case #%d: ", cas++);
		run();
	}
    return 0;
}