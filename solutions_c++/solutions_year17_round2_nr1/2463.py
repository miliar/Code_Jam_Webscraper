#include<bits/stdc++.h> 
#define FN(i, b) for (int (i) = (0); (i) < (b) ; (i)++)
#define sc2(a, b) scanf("%d%d", &a, &b)
#define sc(a) scanf("%d", &a)
#define MAXN 2000006
#define endl "\n"
typedef long long LL;
typedef long double LD;
using namespace std;

int main() {
	int tc;
	sc(tc);

	FN(itc, tc) {
		int d, n;
		sc2(d, n);
		
		LD lastat = 0;
		int st = 0;
		FN (j, n) {
			int k, s;
			sc2(k, s);
			LD at = ((LD)d - k)/s;
			if (at > lastat) {
				lastat = at;
				st = k;
			}
		}
		
		
		printf("Case #%d: %.7f\n", itc + 1, (double)((LD)d/lastat) );
		//cout <<  << endl;
	}
}