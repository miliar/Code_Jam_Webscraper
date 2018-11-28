#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

LL solve(LL depth, LL l_num, LL r_cnt, LL k)
{
	LL ulim = (1LL<<depth);
	if (k <= ulim)
	{
		if (k <= r_cnt)
			return l_num + 1;
		else
			return l_num;
	}
	LL sum = ulim * l_num + r_cnt - ulim;
	k -= ulim;
	ulim *= 2;
	l_num = (l_num - 1) / 2;
	r_cnt = sum - l_num * ulim;
	return solve(depth + 1, l_num, r_cnt, k);
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tcase = 1; tcase <= T; ++tcase)
	{
		printf("Case #%d: ", tcase);
		LL N, K;
		cin >> N >> K;
		LL ans = solve(0, N, 0, K);
		--ans;
		LL a, b;
		if (ans&1)
		{
			a = ans/2;
			b = a + 1;
		}
		else
		{
			a = b = ans/2;
		}
		cout << b << ' ' << a << endl;
	}

	return 0;
}
