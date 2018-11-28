#include <iostream>
#include <limits.h>
#include <algorithm>
#include <utility>
#include <stdio.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		long long d;
		long long n;
		cin >> d >> n;
		long double k[n+1];
		long double s[n+1];
		s[0] = -1;
		k[0] = 0;
		for (int i = 1; i < n+1; i++) {
			cin >> k[i] >> s[i];
		}
		pair< long double, long double > pairs[ n + 1 ];

		for (int i = 0; i < n+1; i++)
			pairs[i] = make_pair(k[i],s[i]);

		sort( pairs , pairs + n + 1 );

		for ( int i = 0; i < n+1; i++ ) {
			k[i] = pairs[i].first;
			s[i] = pairs[i].second;
		}
		for (int i = n - 1; i >= 0; i--) {
			if (s[i+1] > s[i] && i != 0)
				continue;
			else {
				long double temp = (s[i+1]*(d-k[i]))/(d-k[i+1]);
				if (temp < s[i] || i == 0) {
					s[i] = temp;
				}
			}
		}
		printf("Case #%d: %.6f\n", c+1, (float)s[0]);
	}
	return 0;
}
