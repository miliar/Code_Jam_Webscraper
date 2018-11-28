#include<bits/stdc++.h>

using namespace std;

string str;
long long cache[19][10][2];
long long ten[19];

long long f(int idx, int prev, bool minus)
{
	if(idx == -1)
	{
		if(minus)	return -1e18-7;
		return 0;
	}

	long long& result = cache[idx][prev][minus];
	if(result != -1)	return result;

	int t_idx = str.size()-1-idx;
	result = 0;
	if(minus)
	{
		if(str[idx] == '0')
		{
			int cur = min(prev, 9);
			result = f(idx-1, cur, true) + cur*ten[t_idx];
		}
		else
		{
			int cur = min(prev, (int)(str[idx]-'0')-1);
			result = f(idx-1, cur, false) + cur*ten[t_idx];
			if(cur < prev)
				result = max(result, f(idx-1, prev, true)+prev*ten[t_idx]);
		}
	}
	else
	{
		int cur = min(prev, (int)(str[idx]-'0'));
		result = f(idx-1, cur, false) + cur*ten[t_idx];
		if(cur < prev)
			result = max(result, f(idx-1, prev, true)+prev*ten[t_idx]);
	}

	return result;
}

int main()
{
	ten[0] = 1;
	for(int i = 1; i < 19; i++)
		ten[i] = ten[i-1]*10;

	int tcc;
	scanf("%d", &tcc);
	for(int tc = 1; tc <= tcc; tc++)
	{
		cin >> str;
		memset(cache, -1, sizeof(cache));
		if(str == "1000000000000000000")
			str = "999999999999999999";
		
		printf("Case #%d: ", tc);
		printf("%lld\n", f(str.size()-1, 9, false));
	}
	return 0;
}
