#include <bits/stdc++.h>

#define lli long long int
#define pb push_back
#define pii pair <int, int>
#define pll pair <lli, lli>
#define _F first
#define _S second
#define mset(x) memset(x, 0, sizeof(x))
#define fastio() ios_base::sync_with_stdio(0)

using namespace std;

int valid(int);

int main()
{
	int _t;
	cin >> _t;

	for(int t=1; t <= _t; t++)
	{
		int n;
		cin >> n;

		while(not valid(n))
			n--;

		printf("Case #%d: %d\n", t, n);
	}

	return (0-0);	
}

int valid(int n)
{
	int ret = 1;

	while(n / 10)
	{
		ret *= (n % 10 >= ((n / 10) % 10));
		n /= 10;
	}

	return ret;
}