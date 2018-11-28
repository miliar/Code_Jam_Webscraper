#include <cstdio>

using namespace std;

int t;
long long less;
long long more;
long long n;
long long k;
long long lessCnt;
long long moreCnt;
long long ans;

int main() {

	scanf("%d", &t);
	for(int testcase=1; testcase<=t; testcase++) {
		scanf("%lld %lld", &n, &k);

		if(n%2) {
			less=n/2;
			more=n/2;
			moreCnt=2;
			lessCnt=0;
		} else {
			less=n/2-1;
			more=n/2;
			lessCnt=moreCnt=1;
		}

		if(k==1)
			printf("Case #%d: %lld %lld\n", testcase, more, less);
		else {
			k--;
			while(true) {
				long long tmpLessCnt=0;
				long long tmpMoreCnt=0;
				long long nextLess;
				long long nextMore;
				k-=moreCnt;
				if(k<=0) {
					ans=more;
					break;
				}
				k-=lessCnt;
				if(k<=0) {
					ans=less;
					break;
				}

				if(less==more) {
					if(less%2) {
						nextLess=nextMore=less/2;
						tmpMoreCnt+=(moreCnt*2);
					} else {
						nextLess=less/2-1;
						nextMore=more/2;
						tmpMoreCnt+=moreCnt;
						tmpLessCnt+=moreCnt;
					}
				} else {
					if(less%2==0) {
						nextLess=less/2-1;
						nextMore=less/2;
						tmpLessCnt+=lessCnt;
						tmpMoreCnt+=lessCnt;

						if(more/2==nextLess)
							tmpLessCnt+=(moreCnt*2);
						else
							tmpMoreCnt+=(moreCnt*2);
					} else {
						nextLess=more/2-1;
						nextMore=more/2;
						tmpLessCnt+=moreCnt;
						tmpMoreCnt+=moreCnt;

						if(less/2==nextLess)
							tmpLessCnt+=(lessCnt*2);
						else
							tmpMoreCnt+=(lessCnt*2);
					}
				}

				less=nextLess;
				more=nextMore;
				lessCnt=tmpLessCnt;
				moreCnt=tmpMoreCnt;
			}

			long long ansMore, ansLess;
			if(ans%2) {
				ansMore=ans/2;
				ansLess=ans/2;
			} else {
				ansMore=ans/2;
				ansLess=ans/2-1;
			}
			printf("Case #%d: %lld %lld\n", testcase, ansMore, ansLess);
		}
	}

	return 0;
}