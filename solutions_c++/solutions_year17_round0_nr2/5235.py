// QuestionB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <bits\stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define LOCAL_TEST true

using namespace std;

long long calculate(long long n)
{
	long long result = n;
	int count = 0;
	int i = 0;
	while (result >= 10)
	{
		int units = result % 10;
		result /= 10;
		int tens = result % 10;
		++i;
		if (units < tens)
		{
			--result;
			count = i;
			n = result;
		}
	}
	if (count == 0)
	{
		return n;
	}
	// Build number
	while (count)
	{
		n *= 10;
		n += 9;
		--count;
	}
	return n;
}

void solve()
{
	long long n;
	cin >> n;
	if (n < 10)
	{
		cout << n << endl;
	}
	else
	{
		cout << calculate(n) << endl;
	}
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for (int caseID = 1; caseID <= TestCase; caseID++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
#if LOCAL_TEST
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	cout << fixed << setprecision(16);
	int ret = MAIN();
#if LOCAL_TEST
	//cout << "[Finished in " << clock() - start << " ms]" << endl;
#endif
	return ret;
}
