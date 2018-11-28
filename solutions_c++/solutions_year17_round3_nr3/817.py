#include <stdio.h>
#include <string.h>
#include <assert.h>

#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(A,x) memset(A,(x),sizeof(A))

typedef long long LL;
typedef pair<int,int> pii;
int INT(){int x;scanf("%d",&x);return x;}

int main() {
	int T=INT();
	for (int t=1;t<=T;++t) {
		int N=INT();int K=INT();
		double U;
		const int hmm = 1000000;
		scanf("%lf",&U);

		vector<double> P;
		FOR(i,N){
			double x;scanf("%lf",&x);
			P.push_back(x);
		}
		sort(P.begin(),P.end());
		const double eps = 0.00000001;
		while (U > eps) {
			int i=0;
			for (i=1;i<N;++i)if(P[i]>P[i-1]+eps)break;
			double perhead=0.;
			if (i == N){
				perhead = U/N;
				U=0.0;
			} else {
				perhead = min((P[i]-P[i-1]), U/i);
				U-=i*perhead;
			}
			FOR(j,i)P[j]+=perhead;
		}
		
		double ans=1.0;
		FOR(i,N){
			ans *= P[i];
		}

		printf("Case #%d: %.8lf\n", t, ans);
	}
	return 0;
}
