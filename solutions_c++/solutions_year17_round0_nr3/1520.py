#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
typedef long long LL;
LL n, k;
int main () {
	freopen("C-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int T;
	cin >> T;
	for (int ii = 1; ii <= T; ++ii) {
		scanf("%I64d%I64d", &n, &k);
		LL sumji = 0, sumou = 0;
		LL ji = 0, ou = 0;
		if (n & 1) {
			sumji = 1;
			ji = n;
		}
		else {
			sumou = 1;
			ou = n;
		}
		LL sum = 0;
		for (LL i = 1; true; i*=2) {
			sum += i;
			if(sum >= k) {
				sum -= i;
				printf("Case #%d: ", ii);
				if (ou > ji) {
					if (sum + sumou >= k) printf("%I64d %I64d\n", ou / 2, ou / 2 - 1);
					else printf("%I64d %I64d\n", ji / 2, ji / 2);
				}
				else {
					if (sum + sumji >= k) printf("%I64d %I64d\n", ji / 2, ji / 2);
					else printf("%I64d %I64d\n", ou / 2, ou / 2 - 1);
				}
				break;
			}
			LL tsumou = 0, tsumji = 0;
			LL tji = 0, tou = 0;
			if(sumou) {
				tsumou = sumou;
				tsumji = sumou;
				if((ou / 2) & 1) {
					tji = ou / 2;
					tou = ou / 2 - 1;
				}
				else {
					tji = ou / 2 - 1;
					tou = ou / 2;
				}
			}
			if(sumji) {
				if((ji / 2) & 1) {
					tji = ji / 2;
					tsumji += sumji * 2;
				}
				else {
					tou = ji / 2;
					tsumou += sumji * 2;
				}
			}
			sumji = tsumji;
			sumou = tsumou;
			ou = tou;
			ji = tji;
		}
	}
	return 0;
}