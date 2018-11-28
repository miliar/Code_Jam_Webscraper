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

vector<int> s[1003];
int cnt[1003], N, C, M;

int check(int now) {
	int left = 0;
	for(int i=1; i<=N; ++i) {
		if(s[i].size() > now) {
			left -= (s[i].size() - now);
			if(left<0) return false;
		} else {
			left += now - s[i].size();
		}
	}
	return true;
}

int main()
{
	int T; scanf("%d", &T);
	for(int cas=1; cas<=T; ++cas) {
		scanf("%d%d%d", &N, &C, &M);
		for(int i=1;i<=1000;i++)
			s[i].clear();
		memset(cnt, 0, sizeof cnt);

		for(int i=1; i<=M; ++i) {
			int p, b; scanf("%d%d", &p, &b);
			s[p].PB(b);
			++cnt[b];
		}
		int ans_s = 0, ans_p = 0;
		
		for(int i=1; i<=C; ++i)
			ans_s = max(ans_s, cnt[i]);
		ans_s = max(ans_s, (int)s[1].size());
		ans_s = max(ans_s, (M+N-1) / N);
		int l = ans_s, r = M;
		while(l < r) {
			int mid = (l+r)/2;
			if(check(mid)) r = mid;
			else l = mid+1;
		}
		ans_s = l;
		for(int i=2; i<=N; ++i)
			if(s[i].size() > ans_s)
				ans_p += s[i].size() - ans_s;
		printf("Case #%d: %d %d\n", cas, ans_s, ans_p);
	}
	return 0;
}





