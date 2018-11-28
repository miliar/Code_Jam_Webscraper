#include <cstdio>
#include <vector>
#include <map>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for (int cs = 1; cs <= t; ++cs)
	{
		long long n;
		long long k;
		scanf("%lld%lld",&n,&k);
		long long cnt = 0;
		vector<long long> v;
		map<long long, long long> mp;

		v.push_back(n);
		mp[n] = 1;
		int i=0;

		while (cnt < k) {
			if (v[i] & 1) {
				if (mp.count(v[i] >> 1) > 0) {
					mp[v[i] >> 1] += mp[v[i]];
					mp[v[i] >> 1] += mp[v[i]];
				} else {
					mp[v[i] >> 1] = mp[v[i]] + mp[v[i]];
					v.push_back(v[i] >> 1);
				}
				
			} else {
				if (mp.count(v[i] >> 1) > 0) {
					mp[v[i] >> 1] += mp[v[i]];
				} else {
					mp[v[i] >> 1] = mp[v[i]];
					v.push_back(v[i] >> 1);
				}
				if (mp.count((v[i] >> 1) - 1) > 0) {
					mp[(v[i] >> 1) - 1] += mp[v[i]];
				} else {
					mp[(v[i] >> 1) - 1] = mp[v[i]];
					v.push_back((v[i] >> 1) - 1);
				}
			}

			cnt += mp[v[i]];
			i++;
		}
		long long ans = v[i-1];
		long long ans1,ans2;
		if (ans & 1) {
			ans1 = ans >> 1;
			ans2 = ans >> 1;
		} else {
			ans1 = ans >> 1;
			ans2 = (ans >> 1) - 1;
		}

		printf("Case #%d: %lld %lld\n", cs, ans1, ans2);
	}
	return 0;
}