#include <iostream>
#include <algorithm>

using namespace std;

const int Max = 111;
int n, k;
int sum;
int m[Max];

int read()
{
	int a, b;
	char ch;
	cin >> a >> ch >> b;
	return (a * 10000 + b);
}

void solve(int num)
{
	cin >> n >> k;
	sum = read();
	for (int i = 1; i <= n; i++)
	{
		m[i] = read();
	}
	for (int i = 1; i <= sum; i++)
	{
		sort(m + 1, m + n + 1);
		m[1]++;
	}
	cout << "Case #" << num << ": ";
	double answer = 1.0;
	for (int i = 1; i <= n; i++)
	{
		double res = m[i] / 10000.0;
		answer *= res;
	}
	cout.precision(7);
	cout << fixed << answer << endl;
	return;
}

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}