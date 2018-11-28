#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
	int t, tt = 0;
	scanf("%d", &t);

	while(t--){
		ll n, k, total = 0, now;

		scanf("%lld %lld", &n, &k);

		map <ll, ll> mep;
		
		set <ll> myset;
		set <ll> :: iterator it;

		// printf("%lld\n", mep[n]);

		mep[n] = 1;
		myset.insert(n);
		it = myset.upper_bound(n);

		while(total < k){
			it--;

			ll temp = *it;
			ll tmp = mep[temp];

			myset.insert(temp/2);
			myset.insert((temp-1)/2);

			mep[temp/2] += tmp;
			mep[(temp-1)/2] += tmp;

			total += tmp;
			now = temp;

			// printf("total : %lld\n", total);
			// printf("now : %lld\n", now);
		}

		printf("Case #%d: %lld %lld\n", ++tt, max(now/2, (now-1)/2), min(now/2, (now-1)/2));
	}
}