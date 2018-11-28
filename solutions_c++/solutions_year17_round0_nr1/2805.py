#include "bits/stdc++.h"

using namespace std;

int T, testCase;

void solve()
{
	string s;
	int K;
	cin >> s >> K;
	int cnt = 0;
	for(int i = 0 ; i <= s.size() - K ; i++)
	{
		if(s[i] == '+')
			continue;
		cnt++;
		for(int j = i ; j < i + K ; j++)
		{
			if(s[j] == '+')
				s[j] = '-';
			else
				s[j] = '+';
		}
	}
	for(int i = 0 ; i < s.size() ; i++)
		if(s[i] == '-')
		{
			printf("Case #%d: IMPOSSIBLE\n",testCase - T);
			return;
		}
	printf("Case #%d: %d\n",testCase - T, cnt);
}

int main()
{
	
	scanf("%d",&T);
	testCase = T;
	while(T--)
	{
		solve();
	}
}