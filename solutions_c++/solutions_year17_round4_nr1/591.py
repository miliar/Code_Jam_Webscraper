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

int cnt[5];

int main()
{
	int T; scanf("%d", &T);
	for(int cas=1; cas<=T; ++cas) {
		int N, P; scanf("%d%d", &N, &P);
		memset(cnt, 0, sizeof cnt);
		for(int i=1; i<=N; ++i) {
			int x; scanf("%d", &x);
			cnt[x%P]++;
		}
		int ans = cnt[0];
		if(P == 2) {
			ans += cnt[1] / 2;
			if(cnt[1] % 2) ans++;
		} else if(P == 3) {
			ans += min(cnt[1], cnt[2]);
			int tmp = min(cnt[1], cnt[2]);
			cnt[1] -= tmp, cnt[2] -= tmp;
			ans += max(cnt[1], cnt[2]) / 3;
			if(max(cnt[1], cnt[2]) % 3) ans++;
		} else if(P == 4) {
			ans += min(cnt[1], cnt[3]);
			ans += cnt[2] / 2;
			int tmp = min(cnt[1], cnt[3]);
			cnt[1] -= tmp, cnt[3] -= tmp;
			if(cnt[2] % 2) {
				if(cnt[1] >= 2)
					ans++, cnt[1] -= 2, cnt[2]=0;
				if(cnt[3] >= 2)
					ans++, cnt[3] -= 2, cnt[2]=0;
			}
			ans += max(cnt[1], cnt[3]) / 4;
			if(max(cnt[1], cnt[3]) % 4 || cnt[2] % 2) ans++;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}





