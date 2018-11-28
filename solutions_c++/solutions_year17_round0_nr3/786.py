#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;



int main()
{
	int T; scanf("%d", &T);
	for(int cas=1; cas<=T; ++cas) {
		ll n, k; scanf("%lld %lld", &n, &k);

		ll sm = -1, la = n, sm_cnt = 0, la_cnt = 1, p = 1, mx, mn;

		while(k > p) {
			k = k - p;

			if(sm != -1) {
				if(sm % 2)
					sm /= 2, sm_cnt = sm_cnt * 2 + la_cnt;
				else
					sm = (sm - 1) / 2, la_cnt = la_cnt * 2 + sm_cnt;
			} else {
				if(la % 2)
					la_cnt *= 2;
				else
					sm = (la - 1) / 2, sm_cnt = la_cnt;
			}

			p *= 2, la /= 2;
		}

		if(k <= la_cnt)
			mx = la / 2, mn = (la - 1) / 2;
		else
			mx = sm / 2, mn = (sm - 1) / 2;
		printf("Case #%d: %lld %lld\n", cas, mx, mn);
	}
	return 0;
}





