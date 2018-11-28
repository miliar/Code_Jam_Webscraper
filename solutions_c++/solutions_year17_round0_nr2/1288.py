#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll addtostart(ll a, ll num)
{
	ll array[21];
	array[0] = 1;
	while (num)
	{
		array[array[0]++] = num%10;
		num/=10;
	}
	array[array[0]] = a;
	ll  ans = 0;
	for (ll i = array[0]; i > 0; i--)
	{
		ans*=10;
		ans+=array[i];
	}
	return ans;
}
ll t, n, number[25];
ll len;
ll memo[25][20][2][25];
bool done[25][20][2];
void recurse(ll upto, ll digit, bool belowx = false)
{
	if (upto == len) { memo[upto][digit][belowx][0] = digit; return; }
	if (done[upto][digit][belowx]) return;
	done[upto][digit][belowx] = true;
	if (!belowx)
	{
		recurse(upto+1, number[upto+1], false);
		if (number[upto+1] >= digit && memo[upto+1][number[upto+1]][false][0] != -1)
		{
			for (ll i = 0; i < len-upto; i++) memo[upto][digit][false][i+1] = memo[upto+1][number[upto+1]][false][i];
			memo[upto][digit][false][0] = digit;
			return;
		}
		for (int i = number[upto+1]-1; i >= digit; i--)
		{
			recurse(upto+1, i, true);
			if (memo[upto][digit][belowx][0] == -1) continue;
			
			for (ll j = 0; j < len-upto; j++) memo[upto][digit][false][j+1] = memo[upto+1][i][true][j];

			memo[upto][digit][false][0] = digit;
			return;
		}
		memo[upto][digit][belowx][0] = -1;
		//printf("%d %d %d\n", upto, digit, belowx);
		return;
	}
	recurse(upto+1, 9, true);
	for (ll i = 0; i < len-upto; i++) memo[upto][digit][true][i+1] = memo[upto+1][9][true][i];
	memo[upto][digit][true][0] = digit;
	return;
}
int main()
{
	scanf("%lld", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%lld", &n);
		number[0] = 0;
		int a = n;
		while (n)
		{
			number[++number[0]] = n%10;
			n/=10;
		}
		len = number[0];
		reverse(number+1, number+number[0]+1);
		for (int i = 0; i < 25; i++)
		{
			for (int j = 0; j < 20; j++) 
			{
				done[i][j][0] = false;
				done[i][j][1] = false;
				for (int k = 0; k < 25; k++) { memo[i][j][0][k] = 0; memo[i][j][1][k] = 0; }
			}
		}
		recurse(1, number[1], false);
		ll ans = 0;
		if (memo[1][number[1]][false][0] == -1)
		{
			//printf("hi\n");
			recurse(1, number[1]-1, true);
			for (int i = 0; i < len; i++)
			{
				ans*=10;
				ans+=memo[1][number[1]-1][true][i];
			}
		}
		else
		{
			for (int i = 0; i < len; i++)
			{
				//printf("%d\n", memo[1][number[1]][false][i]);
				ans*=10;
				ans+=memo[1][number[1]][false][i];
			}
		}
		printf("Case #%d: %lld\n", i, ans);
	}
}