#include <bits/stdc++.h>
using namespace std;
char input[3000];
int k;
void flip(char& c)
{
	if(c == '+')
		c = '-';
	else
		c = '+';
}
void solve()
{
	scanf("%s%d", input, &k);
	int leng = strlen(input);
	int res = 0;
	for(int i = 0; i + k <= leng; ++i)
		if(input[i] == '-')
		{
			for(int j = 0; j < k; ++j)
				flip(input[i+j]);
			++res;
		}
	for(int i = 0; i < leng; ++i)
		if(input[i] == '-')
		{
			puts("IMPOSSIBLE");
			return;
		}
	printf("%d\n", res);
	
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	
	return 0;
}
