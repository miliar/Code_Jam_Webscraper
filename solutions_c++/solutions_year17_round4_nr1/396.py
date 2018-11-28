#define _CRT_SECURE_NO_DEPRECATE 1
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int ans[101][101];

int solve(int n, int p, int* arr)
{
	int mod[4];
	for (int i = 0; i < 4; i++)
		mod[i] = 0;

	for (int i = 0; i < n; i++)
		mod[arr[i] % p]++;

	if (p == 2)
		return mod[0] + (mod[1] + 1) / 2;

	if (p == 3)
	{
		int min1 = min(mod[1], mod[2]);
		int max1 = max(mod[1], mod[2]);
		return mod[0] + min1 + (max1 - min1 + 2) / 3;
	}

	if (p == 4)
	{
		int min1 = min(mod[1], mod[3]);
		int max1 = max(mod[1], mod[3]);
		int ans = mod[0] + min1 + mod[2] / 2 + (max1 - min1) / 4;
		if (mod[2] % 2 + (max1 - min1) % 4 == 0)
			return ans;
		if (mod[2] % 2 == 1 && (max1 - min1) % 4 == 3)
			return ans + 2;
		return ans + 1;
	}

	return -1;
}

void solve(int tn)
{
	int n, p;
	int arr[110];
	cin >> n >> p;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	cout << "Case #" << tn << ": " << solve(n, p, arr) << endl;
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
