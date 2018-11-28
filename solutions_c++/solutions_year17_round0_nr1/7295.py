#include <bits/stdc++.h>
using namespace std;
char s[1010];
bool op[1010];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; t++)
	{
		int k;
	scanf("%s%d", s, &k);
	for(int i = 0; i < 1001; i++)
		op[i] = false;
	bool O = true;
	int ans = 0;
	int n = strlen(s);
	for(int i = 0; i + k - 1 < n; i++)
	{
		bool vall = s[i] == '+';
		O ^= op[i];
		if(O != vall)
		{
			O = !O;
			ans++;
			op[i + k] = true;
		}
	}
	bool allRight = true;
	for(int i = n-k+1; i <= n-1; i++)
	{
		O ^= op[i];
		bool vall = s[i] == '+';
		if(O != vall)
			allRight = false;
	}
	printf("Case #%d: ", caseNumber);
	if(allRight) printf("%d\n", answer);
	else printf("IMPOSSIBLE\n");
	}
	return 0;
}
