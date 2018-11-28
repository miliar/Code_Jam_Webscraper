/*cf handle: visitR*/

#include <bits/stdc++.h>
using namespace std;

#define pi acos(-1)
#define inf (1 << 30)
#define linf (1llu << 60)

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vp;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;

int main() {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; ++t) {
		ll N, k;
		scanf("%lld%lld", &N, &k);
		ll o = 0, e = 0, co = 0, ce = 0;
		if (N % 2 == 0) {
			e = N;
			ce = 1;
		}
		else {
			o = N;
			co = 1;
		}
		while (1) {
			ll s = co + ce;
			if (k <= s) 
				break;
			k -= s;
			ll tempo = 0, tempe = 0, tempco = 0, tempce = 0;
			if (co > 0) {
				--o;
				if ((o/2) % 2 == 0) {
					tempce += 2*co;
					tempe = o/2;
				}
				else {
					tempco += 2*co;
					tempo = o/2;
				}
			}
			if (ce > 0) {
				--e;
				if ((e/2) % 2 == 0)  {
					tempe = e/2;
					tempo = e - e/2;
				}
				else {
					tempe = e - e/2;
					tempo = e/2;
				}
				tempce += ce;
				tempco += ce;
			}
			e = tempe, o = tempo;
			ce = tempce, co = tempco;
		}
		printf("Case #%d: ", t);
		if (o >= e) {
			if (k <= co) 
				printf("%lld %lld\n", (o-1)/2, (o-1)/2);
			else
				printf("%lld %lld\n", (e-1)-(e-1)/2, (e-1)/2);
		}
		else {
			if (k <= ce) 
				printf("%lld %lld\n", (e-1)-(e-1)/2, (e-1)/2);
			else
				printf("%lld %lld\n", (o-1)/2, (o-1)/2);
		}
	}
	return 0;
}
