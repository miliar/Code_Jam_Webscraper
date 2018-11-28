#include <bits/stdc++.h>
using namespace std;

void sol(int c)
{
	long long n;
	int num[25], cnt(0), lst;
	cin >> n;
	while (n)
	{
		num[cnt++] = n % 10;
		n /= 10;
	}
	num[cnt] = 0;
	lst = cnt;
	for (;lst > 0 && num[lst - 1] >= num[lst]; lst--);
	if (lst > 0)
	{
		while (num[lst] == num[lst + 1]) lst++;
		num[lst]--;
		for (int i = lst - 1; i >= 0; i--) num[i] = 9;
	}
	long long ans = 0;
	for (int i = cnt; i >= 0; i--) ans = ans * 10 + num[i];
	for (int i = cnt; i >= 0; i--) cerr << num[i] << ' ';
	cerr << endl;
	printf("Case #%d: %lld\n", c, ans);
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) sol(i);
	return 0;
}
