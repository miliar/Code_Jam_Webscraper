#include <bits/stdc++.h>
using namespace std;

int main () {
	
	int c=0, n=0, i=0;
	long long int d=0, k=0, s=0;

	scanf("%d", &c);

	for (int idx=1; idx<=c; idx++) {

		scanf("%lld %d", &d, &n);

		long double res=INT_MIN;

		for (i=0; i<n; i++) {
			scanf("%lld %lld", &k, &s);
			long double aux = d-k;
			aux /= s;
			res = max(res, aux);
		}

		res = d/res;

		printf("Case #%d: %.8Lf\n", idx, res);
		//cout << "Case #" << idx << ": " << res << endl;
	}

	return 0;
}