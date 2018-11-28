#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long int lli;

lli n, memo[20][11][2], memoi[20][11][2];
string S;

bool DP(lli idx, lli prev, lli chotta)
{
	if(idx == n) return 1;
	else if(memo[idx][prev][chotta] != -1) return memo[idx][prev][chotta];
	else
	{
		bool res = 0;
		lli resi = -1;
		for(lli dig = 9;dig >= prev;dig--)
		{
			if(chotta)
			{
				res = max(res, DP(idx+1, dig, 1));
				if(res)
				{
					resi = dig;
					break;
				}
			}
			else if(dig <= lli(S[idx]-'0'))
			{
				res = max(res, DP(idx+1, dig, bool(dig < lli(S[idx]-'0'))));
				if(res)
				{
					resi = dig;
					break;
				}
			}
			if(res) break;
		}
		memo[idx][prev][chotta] = res;
		memoi[idx][prev][chotta] = resi;
		return res;
	}
}

int main(void)
{
	lli t;
	scanf("%lld", &t);
	for(lli tst = 1;tst <= t;tst++) {
	printf("Case #%lld: ", tst);
	cin >> S;
	n = lli(S.size());
	bool done = 0;
	if(count(S.begin(), S.end(), '1')+count(S.begin(), S.end(), '0') == n && count(S.begin(), S.end(), '0'))
	{
		for(lli i = 1;i < n;i++) printf("9");
		printf("\n");
		done = 1;
		continue;
	}
	if(done) continue;
	lli idx = 0, prev = 1, chotta = 0;

	for(lli i = 0;i < 20;i++)
	{
		for(lli j = 0;j < 11;j++)
		{
			for(lli k = 0;k < 2;k++) memo[i][j][k] = memoi[i][j][k] = -1;
		}
	}
	DP(0, 1, 0);

	while(idx < n)
	{
		printf("%lld", memoi[idx][prev][chotta]);
		prev = memoi[idx][prev][chotta];
		chotta = max(chotta, lli(prev < lli(S[idx]-'0')));
		idx++;
	}
	printf("\n"); }
}