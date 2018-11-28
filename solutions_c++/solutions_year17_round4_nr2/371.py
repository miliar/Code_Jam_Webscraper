#define _CRT_SECURE_NO_DEPRECATE 1
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int ans[101][101];

pair<int, int> solve(int n, int c, int* ndeg, int* cdeg)
{
	int min = 0;
	for (int i = 0; i < c; i++)
		if (cdeg[i] > min)
			min = cdeg[i];

	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum += ndeg[i];
		if ((sum + i) / (i + 1) > min)
			min = (sum + i) / (i + 1);
	}

	int move = 0;
	for (int i = 0; i < n; i++)
		if (ndeg[i] > min)
			move += ndeg[i] - min;

	return pair<int, int>(min, move);
}

void solve(int tn)
{
	int n, c, m;
	int cdeg[1100], ndeg[1100];
	cin >> n >> c >> m;
	memset(cdeg, 0, sizeof(cdeg));
	memset(ndeg, 0, sizeof(ndeg));

	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		ndeg[a - 1]++;
		cdeg[b - 1]++;
	}

	pair<int, int> ans = solve(n, c, ndeg, cdeg);
	cout << "Case #" << tn << ": " << ans.first << " " << ans.second << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf_s("%d", &t);
	for (int it = 0; it < t; it++)
		solve(it + 1);
	return 0;
}
