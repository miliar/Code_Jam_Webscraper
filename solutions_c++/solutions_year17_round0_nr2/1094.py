#include <bits/stdc++.h>

#define pii pair<int, int>
#define pll pair<LL, LL>
#define F first
#define S second
#define B begin()
#define E end()
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

#define PI (4 * atan(1))

using namespace std;

int t, len, a[20];
LL val, ans, ten[20], input;
char s[20];

bool cal(int x, int l)
{
	for(int i = 9; i >= x; --i)
	{
		if(val + i * ten[len - l] <= input)
		{
			val += i * ten[len - l];
			if(l == len)
			{
				ans = val;
				return true;
			}
			if(cal(i, l + 1))
				return true;
			val -= i * ten[len - l];
		}

	}
}

int main()
{
	// freopen("B-large.in", "r", stdin);
	// freopen("B-large.out", "w", stdout);

	ten[0] = 1;
	for(int i = 1; i < 18; ++i)
		ten[i] = ten[i-1] * 10;

    scanf("%d", &t);
    for(int z = 1; z <= t; ++z)
    {
    	input = val = ans = 0;
    	scanf("%s", s);
    	len = strlen(s);
    	for(int i = 0; i < len; ++i)
		{
			a[i] = int(s[i] - '0');
		    input = 10 * input + a[i];
		}
		cal(0, -1);
    	printf("Case #%d: %lld\n", z, ans);
    }
    return 0;
}