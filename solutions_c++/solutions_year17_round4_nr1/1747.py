#include <iostream>
#include <cstdio>
#define int long long
using namespace std;

signed main(){
	int t;
	cin >> t;
	for(int test = 0;test < t;test++){
		int n,p,cnt[4] = {},ans = 0;
		cin >> n >> p;
		for(int i = 0;i < n;i++){
			int a;
			cin >> a;
			cnt[a % p]++;
		}
		ans += cnt[0];
		if(p == 2) ans += (cnt[1] + 1) / 2;
		else if(p == 3) {
			ans += min(cnt[1],cnt[2]);
			int d = max(cnt[1],cnt[2]) - min(cnt[1],cnt[2]);
			ans += (d + 2) / 3;
		}
		printf("Case #%d: %d\n",test + 1,ans);
	}
	return 0;
}