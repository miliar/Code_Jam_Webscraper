#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#define maxn 1009
using namespace std;
long long n, m, ans;

int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/C.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/C.out", "w", stdout);
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		scanf("%lld%lld", &n, &m);
		long long cura = n, curb = n;
		long long numa = 1, numb = 0;
		while(m > numa + numb){
			//cout << cura << " " << numa << endl;
			//cout << curb << " " << numb << endl;
			m -= numa + numb;
			long long na, nb, ca,cb;
			if(cura == curb){
				ca = (cura -1 + 1) / 2;
				cb = (cura - 1) / 2;
				na = numa + numb;
				nb = numa + numb;
			}
			else if(cura % 2 == 0){
				ca = (cura - 1 + 1) / 2;
				cb = (cura - 1) / 2;
				na = numa;
				nb = numa + 2 * numb;
			}
			else{
				ca = (curb - 1 + 1) / 2;
				cb = (curb - 1) / 2;
				na = 2 * numa + numb;
				nb = numb;
			}
			numa = na;
			numb = nb;
			cura = ca;
			curb = cb;
			//cout << cura << " " << numa << endl;
			//cout << curb << " " << numb << endl;
		}
		long long ans = 0;
		if(m <= numa)
			ans = cura;
		else
			ans = curb;
		printf("Case #%d: %lld %lld\n", cot++, ans / 2, (ans - 1) /2);
	}
	return 0;
}