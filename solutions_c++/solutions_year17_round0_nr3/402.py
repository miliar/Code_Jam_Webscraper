#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

long long n, m;

void doit(long long a, long long b, long long n, long long m)
{
	if (m <= a+b)
	{
		if (m <= b)
			cout << n/2 << " " << (n-1)/2 << endl;
		else
			cout << (n-1)/2 << " " << n/2-1 << endl;
		return;
	}
	m -= (a+b);
	if (n % 2 == 0)
		doit(a+a+b,b,n/2,m);
	else
		doit(a,a+b+b,n/2,m);
}

void solve()
{
	cin >> n >> m;
	doit(0, 1, n, m);
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}