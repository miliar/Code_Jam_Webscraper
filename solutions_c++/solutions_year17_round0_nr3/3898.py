#include<bits/stdc++.h>
using namespace std;
priority_queue<long long>que;
map<long long, long long>mp;
int main() {
	#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int T, cas = 0;
	long long n, k;
	scanf("%d", &T);
	while (T--) {
		scanf("%lld %lld", &n, &k);
		que.push(n);
		mp.clear();
		mp[n] = 1;
		long long left=0, right=0;
		while (k) {
			long long now = que.top();
			long long num = mp[now];
			mp[now] = 0;
			now--;
			que.pop();
			if (k>num) {
				if (now % 2 == 0) {
					if (mp.find(now / 2) == mp.end())
						mp[now / 2] = 2 * num;
					else
						mp[now / 2] += 2 * num;
					que.push(now / 2);
				}
				else {
					if (mp.find((now - 1) / 2) == mp.end())
						mp[(now - 1) / 2] = num;
					else
						mp[(now - 1) / 2] += num;
					if (mp.find((now + 1) / 2) == mp.end())
						mp[(now + 1) / 2] = num;
					else
						mp[(now + 1) / 2] += num;
					que.push((now - 1) / 2);
					que.push((now + 1) / 2);
				}
				k -= num;
			}
			else {
				k = 0;
				if (now % 2 == 0) {
					left = right = now / 2;
				}
				else {
					left = (now + 1) / 2;
					right = (now - 1) / 2;
				}
			}
		}
		printf("Case #%d: %lld %lld\n", ++cas, left, right);
	}
	return 0;
}
