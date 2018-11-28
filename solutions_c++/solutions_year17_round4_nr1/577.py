#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

int cnt[5];

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1;kase<=t;kase++) {
		printf("Case #%d: ", kase);
		int n, p;
		scanf("%d%d", &n, &p);
		memset(cnt, 0, sizeof(cnt));
		for(int i=0; i<n; i++) {
			int tmp;
			scanf("%d", &tmp);
			cnt[tmp%p]++;
		}
		int ans=0;
		ans += cnt[0];
		if(p==2)
			ans += (cnt[1]+1)/2;
		else if(p==3) {
			int x = min(cnt[1], cnt[2]);
			int y = max(cnt[1], cnt[2])-x;
			ans += x;
			if(y>0)
				ans += (y-1)/3+1;
		} else {
			int x = min(cnt[1], cnt[3]);
			int y = max(cnt[1], cnt[3]) - x;
			ans += x;
			cnt[2] += y/2;
			y %= 2;
			ans += (cnt[2]+1)/2;
			if(y>0)
				if(cnt[2]%2==0)
					ans++;
		}
		printf("%d\n", ans);
		for(int i=0; i<p; i++)
			debug("%d ", cnt[i]);
		debug("\n");
	}
	return 0;
}
