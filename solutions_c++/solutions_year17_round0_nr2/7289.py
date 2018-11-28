#include <bits/stdc++.h>
using namespace std;
char s[1010];
bool op[1010];

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; t++)
	{
	ll n;
	scanf("%lld", &n);
	vector<int> cifre;
	while(n)
	{
		cifre.push_back(n % 10);
		n /= 10;
	}
	reverse(cifre.begin(), cifre.end());
	int pos = -1;
	for(int i = 0; i < cifre.size() - 1; i++)
	{
		if(cifre[i] > cifre[i + 1])
		{
			pos = i;
			break;
		}
	}
	if(pos != -1)
	{
		for(int i = pos + 1; i < cifre.size(); i++) cifre[i] = 9;
		cifre[pos]--;
		for(int i = pos; i >= 1; i--)
		{
			if(cifre[i] < cifre[i - 1])
			{
				cifre[i] = 9;
				cifre[i - 1]--;
			}
			else break;
		}
	}
	printf("Case #%d: ",tt);
	for(auto x:cifre) printf("%d ",x);
	printf("\n");
	}
	return 0;
}
