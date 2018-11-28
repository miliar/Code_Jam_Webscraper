#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
using namespace std;

typedef pair<long long,long long> pii;

int main () {
	int t;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++) {
		long long n, k;
		scanf ("%lld %lld", &n, &k);

		long long ans = -1;
		bool one = true;
		pii a[2];
		a[0] = pii(1,n);

		while (k) {
			if (k <= a[0].first) {
				ans = a[0].second;
				break;
			}
			k -= a[0].first;
			if (one) {
				//cout << a[0].first << " " << a[0].second << endl;
				if (a[0].second % 2LL) {
					a[0].first *= 2LL;
					a[0].second /= 2LL;
				} else {
					a[0].second /= 2LL;
					a[1].first = a[0].first;
					a[1].second = a[0].second - 1LL;
					one = false;
				}
			} else {
				//cout << a[0].first << " " << a[0].second << endl;
				//cout << a[1].first << " " << a[1].second << endl;
				if (k <= a[1].first) {
					ans = a[1].second;
					break;
				}
				k -= a[1].first;
				if (a[0].second % 2LL) {
					a[0].first = a[0].first*2LL + a[1].first;
					a[0].second /= 2LL;
					a[1].second = a[0].second - 1LL;
				} else {
					a[0].second /= 2LL;
					a[1].second = a[0].second - 1LL;
					a[1].first = a[1].first*2LL + a[0].first;
				}
			}
		}

		printf ("Case #%d: %lld %lld\n", tc, ans/2LL, (ans-1LL)/2LL);

	}

	return 0;
}
