#include <bits/stdc++.h>

#define pii pair<int, int>
#define pll pair<LL, LL>
#define F first
#define S second
#define B begin()
#define E end()
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

#define PI (4 * atan(1))

using namespace std;

int t;
LL n, k;
map<LL, LL> mmap;

int main()
{
	// freopen("C-large.in", "r", stdin);
	// freopen("C-large.out", "w", stdout);

    scanf("%d", &t);
    for(int z = 1; z <= t; ++z)
	{
		mmap.clear();

		scanf("%lld %lld", &n, &k);
		mmap[-n] = 1;
		k -= 1;
		while(k != 0)
		{
			if(k >= mmap.begin() -> S)
			{
				k -= mmap.begin() -> S;
				if((mmap.begin() -> F + 1) % 2 == 0)
					mmap[(mmap.begin() -> F + 1) / 2] += 2 * mmap.begin() -> S;
				else
				{
					mmap[(mmap.begin() -> F + 1) / 2] += mmap.begin() -> S;
					mmap[(mmap.begin() -> F + 1) / 2 - 1] += mmap.begin() -> S;
				}
				mmap.erase(mmap.begin());
			}
			else
				break;
		}
		if((mmap.begin() -> F + 1) % 2 == 0)
			printf("Case #%d: %lld %lld\n", z, -(mmap.begin() -> F + 1) / 2, -(mmap.begin() -> F + 1) / 2);
		else
			printf("Case #%d: %lld %lld\n", z, -(mmap.begin() -> F + 1) / 2 + 1, -(mmap.begin() -> F + 1) / 2);
	}
    return 0;
}