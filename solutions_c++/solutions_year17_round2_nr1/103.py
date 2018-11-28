#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#define DO long double
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T,n;
DO dist, ans;
DO p[1010];
DO v[1010];

int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ", T_T);
		ans=10000000000000000000.0;
		cin >> dist >> n;
		REP(i,n) {
			cin >> p[i] >> v[i];
			ans=min(ans, dist*v[i]/(dist-p[i]));
		}
		printf("%.10f\n",(double)ans);
	}

	return 0;
}