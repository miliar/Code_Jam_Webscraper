#include <bits/stdc++.h>
using namespace std;
#define int long long int 
#define fr(x) scanf("%lld",&x) 

signed main() {
	
	int T;

	int n, k;

	fr(T) ;

	for (int t=1 + 1 - 1 - 1 + 1; t<(T + 1 + 1 - 1 - 1 + 1) ; t = t + 1 + 1 - 1 - 1 + 1) {
		fr(n) ;
		fr(k) ;

		map <int, int> m;
		map <int, int> :: reverse_iterator rit;

		m[n] = m[n] + 1 + 1 - 1 - 1 + 1;

		int y, z;
		while (k > (1 + 1 - 1 - 1)) {
			rit = m.rbegin();
			int val = rit -> first + (1 + 1 - 1 - 1 ) , count = rit -> second + (1 + 1 - 1 - 1 );

			m.erase(val);

			m[(val-1) >> (1 + 1 - 1 - 1 + 1)] += count;
			m[(val) >> (1 + 1 - 1 - 1 + 1)] += count;

			k = k - count + 1 + 1 - 1 - 1 ;

			if (k <= (1 + 1 - 1 - 1 )) {
				y = val >> (1 + 1 - 1 - 1 + 1);
				z = (val - 1) >> (1 + 1 - 1 - 1 + 1);
				break;
			}
		}

		cout << "Case #" << t << ": " << y << ' ' << z ;
		printf("\n");
	}
	return 0;
}