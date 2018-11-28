// QuestionA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <bits\stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define LOCAL_TEST false

using namespace std;

string flip(string s, int start, int end)
{
	for (int i = start; i <= end; ++i)
	{
		s[i] = (s[i] == '+') ? '-' : '+';
	}
	return s;
}

int calculate(string s, int k)
{
	int count = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		if (s[i] == '-')
		{
			if (i + k - 1 < s.size())
			{
				s = flip(s, i, i + k - 1);
				++count;
			}
			else
			{
				return -1;
			}
		}
	}
	return count;
}

void solve()
{
	string s;
	int k;
	cin >> s;
	cin >> k;
	int result = calculate(s, k);
	if (result == -1)
	{
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << result << endl;
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
	ios::sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int ret = MAIN();
#if LOCAL_TEST
	//cout << "[Finished in " << clock() - start << " ms]" << endl;
#endif
	return ret;
}

