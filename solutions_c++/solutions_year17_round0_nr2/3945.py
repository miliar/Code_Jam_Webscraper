#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define DEBUG	0
#define toDigit(c) (c-'0')

int T;
string N;
int nums[20];

int regroup(int index)
{
	if (nums[index - 1] > nums[index])
	{
		nums[index - 1]--;
		for (int i = index; i < N.length(); i++)
		{
			nums[i] = 9;
		}
		
		return 1;
	}

	return 0;
}


void solve()
{
	int cntRegroup;

	for (int i = 0; i < N.length(); i++)
	{
		nums[i] = toDigit(N[i]);
	}

	do
	{
		cntRegroup = 0;
		for (int i = N.length() - 1; i > 0; i--)
		{
			cntRegroup += regroup(i);
		}
	} while (cntRegroup > 0);

	bool isFirstZero = (nums[0] == 0);
	for (int i = 0; i < N.length(); i++)
	{
		if (nums[i] != 0)
			isFirstZero = false;

		if (!isFirstZero)
			cout << nums[i];
	}
}


int main()
{
	if (DEBUG) freopen("B-large.in", "r", stdin);
	if (DEBUG) freopen("B-large.out", "w", stdout);

	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> N;

		cout << "Case #" << t + 1 << ": ";

		solve();

		cout << endl;
	}

	return 0;
}
