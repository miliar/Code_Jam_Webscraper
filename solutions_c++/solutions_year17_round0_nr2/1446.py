#include <cstdio>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstringt.h>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

vector <int> arr;

bool check(ll N)
{
	arr.clear();

	while (N)
	{
		arr.push_back(N % 10);
		N = N / 10;
	}

	for (int i = 0; i + 1 < arr.size(); ++i)
	{
		if (arr[i] >= arr[i+1])
		{
			continue;
		}
		else
		{
			return false;
		}
	}
	return true;
}

ll brute_force(ll N)
{

	for (ll i = N; i >= 1; --i)
	{
		if (check(i))
		{
			return i;
		}
	}
	return -1;
}

int ans[100];

bool dfs(int curPos, int val, bool flag)
{
	ans[curPos] = val;
	if (curPos + 1 == arr.size())
	{
		if (!flag)	return true;

		if (val <= arr[curPos]) {
			return true;
		} else {
			return false;
		}
	}

	bool ok = false;

	if (!flag) 
		ok = true;
	else
	{
		if (val <= arr[curPos])	ok = true;
		else ok = false;
	}

	if (!ok)	return false;

	bool nextflag = false;

	if (flag)
	{
		if (val == arr[curPos])
			nextflag = true;
	}

	for (int i = 9; i >= val; --i)
	{
		if (dfs(curPos+1, i, nextflag))	return true;
	}
	return false;
}

ll solve(ll N)
{
	arr.clear();

	while (N)
	{
		arr.push_back(N % 10);
		N = N / 10;
	}

	reverse(arr.begin(), arr.end());

	bool res = dfs(0, arr[0], true);

	ll ret = 0;

	if (res)
	{
		for (int i = 0; i < arr.size(); ++i)
		{
			ret = ret * 10 + ans[i];
		}
	}
	else
	{
		ret = arr[0] - 1;
		for (int i = 0; i < arr.size() - 1; ++i)
		{
			ret = ret * 10 + 9;
		}
	}

	return ret;
}

void domain()
{
	
	ll N;
	cin >> N;
	cout << solve(N) << endl;
}

int main()
{
	int T;
	//cin.sync_with_stdio(false);
	scanf("%d\n", &T);

	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		domain();
	}

	return 0;
}