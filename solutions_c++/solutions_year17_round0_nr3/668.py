#include <cstdio>
#include <deque>
#define LL long long
#define PLL pair<LL, LL>
#define FR first
#define SC second
#define MP make_pair
using namespace std;
deque<PLL> Q;
int main()
{
	int T;
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for (int _T = 1; _T <= T; _T++)
	{
		LL N, K, cnt = 0;
		scanf("%lld%lld", &N, &K);
		while (!Q.empty()) Q.pop_front();
		Q.push_back(MP(N, 1));
		while (1)
		{
			PLL A = Q.front();
			LL a = A.FR, b = A.SC;
			Q.pop_front();
			cnt += b;
			if (cnt >= K)
			{
				LL _l, _r;
				if (a % 2 == 0)
				{
					_l = a / 2;
					_r = a / 2 - 1;
				}
				else
				{
					_l = (a - 1) / 2;
					_r = (a - 1) / 2;
				}
				printf("Case #%d: %lld %lld\n", _T, _l, _r);
				break;
			}
			if (a % 2 == 0)
			{
				PLL B = Q.back();
				LL x = a / 2, y = b, z = B.FR, w = B.SC;
				if (x == z)
				{
					Q.pop_back();
					Q.push_back(MP(x, y + w));
				}
				else Q.push_back(MP(x, y));
				Q.push_back(MP(x - 1, y));
			}
			else
			{
				PLL B = Q.back();
				LL x = (a - 1) / 2, y = b * 2, z = B.FR, w = B.SC;
				if (x == z)
				{
					Q.pop_back();
					Q.push_back(MP(x, y + w));
				}
				else Q.push_back(MP(x, y));
			}
		}
	}
	return 0;
}
