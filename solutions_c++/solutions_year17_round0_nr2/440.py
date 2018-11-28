#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LLong;

bool tidy_check(LLong num)
{
	while (num >= 10)
	{
		LLong rhs = num % 10;
		num /= 10;
		LLong lhs = num % 10;
		if (lhs > rhs)
			return false;
	}
	return true;
}

LLong solve(LLong num)
{
	if (tidy_check(num))
		return num;
	LLong dig = num % 10;
	num -= (dig + 1);
	num /= 10;
	return solve(num) * 10 + 9;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tcase = 1; tcase <= T; ++tcase)
	{
		printf("Case #%d: ", tcase);

		LLong num;
		cin >> num;
		cout << solve(num) << endl;
	}

	return 0;
}
