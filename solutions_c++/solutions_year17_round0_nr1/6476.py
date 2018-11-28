#include <bits/stdc++.h>
using namespace std;
int T, K;
int main()
{
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		int ans =0;
		char pancakes[2000];
		scanf(" %s ", pancakes);
		scanf(" %d ", &K);
		for(int i=0; i<= strlen(pancakes)-K; i++)
		{
			if(pancakes[i] == '-')
			{
				ans++;
				for(int k=0; k<K; k++)
				{
					if(pancakes[i+k]=='-') pancakes[i+k] = '+';
					else pancakes[i+k] = '-';
				}
			}
		}
		bool passed = true;
		for(int k=1; k<=K; k++)
		{
			if(pancakes[strlen(pancakes)-k] == '-') passed = false;
		}
		if(passed)printf("Case #%d: %d\n", t, ans);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
}