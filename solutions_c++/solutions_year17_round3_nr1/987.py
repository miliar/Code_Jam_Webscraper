#include <stdio.h>
#include <string.h>
#include <math.h>

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

const double pi = 2.*acos(0.);
vector<pii> pancakes;
int N, K;
double dp[1005][1005];
bool seen[1005][1005];

double sideArea(int i) {
	return 2.*pi*pancakes[i].first*pancakes[i].second;
}

double F(int at, int taken) {
	if (taken > K) return -1.0;
	if (taken == K) return 0.0;
	if (at >= N) {
		return -1.0;
	}

	if (seen[at][taken])return dp[at][taken];
	seen[at][taken]=true;
	dp[at][taken]=-1.0;

	double tmp=F(at+1, taken+1);
	if (tmp > -1.0) {
		dp[at][taken] = max(dp[at][taken], sideArea(at) + tmp);
	}
	tmp = F(at+1, taken);
	if (tmp > -1.0) {
		dp[at][taken] = max(dp[at][taken], tmp);
	}
	return dp[at][taken];
}

int main() {
	int T=INT();
	for (int t=1;t<=T;++t) {
		N=INT();K=INT();
		pancakes.clear();
		FOR(i,N) {
			int r=INT();
			int h=INT();
			pancakes.push_back(pii(r,h));
		}

		sort(pancakes.begin(), pancakes.end());
		reverse(pancakes.begin(), pancakes.end());

		CLR(seen,0);
		double ans = 0.0;

		FOR(i,N) {
			double area = pi*pancakes[i].first*pancakes[i].first;
			area += sideArea(i);
			double tmp=F(i+1, 1);
			if (tmp>-1.0){
				ans=max(ans, area + tmp);
			}
		}
		printf("Case #%d: %.8lf\n", t, ans);
	}
	return 0;
}
