#include <bits/stdc++.h>

using namespace std;

int solver(char* s, int len, int k)
{
	int cnt = 0;
	for(int i = 0; i <= len - k; ++i)
	{
		if(s[i] == '-')
		{
			++cnt;
			for(int j = i; j != i + k; ++j)
				s[j] = (s[j] == '-') ? '+' : '-';
		}
	}
	for(int j = len - k; j != len; ++j)
		if(s[j] == '-') return -1;
	return cnt;
}

char buffer[1001];

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
	{
		int k;
		scanf("%s %d", buffer, &k);
		int res = solver(buffer, strlen(buffer), k);
		printf("Case #%d: ", i);
		if(res == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}
