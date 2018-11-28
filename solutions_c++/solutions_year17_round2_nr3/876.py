#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <list>
#include <queue>

#include <math.h>
#include <set>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long
#define ull unsigned long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;
int k[1000];
int s[1000];

double dp[200][200];
int g[200][200];

int n;
int q;

double solve_small() {
	for(int i = 0; i < n; ++i) {
		for(int j = 0; j <=i; ++j) {
			dp[i][j] = -1;
		}
	}

	dp[0][0]=0;
	for(int i = 1; i < n; ++i) {
		int dis = 0;
		for(int j = 0; j < i; ++j) {
			dis += g[j][j+1];
		}
		double min_time = -1;
		for(int j = 0; j <i;++j) {
			if(dp[i-1][j]>=0) {
				if(dis<=k[j]) {
					double cost = dp[i-1][j]+((double)g[i-1][i]/s[j]);
					//printf("cost = %lf g = %d s = %d\n",cost,g[i-1][i],s[j]);
					dp[i][j]= dp[i][j]<0? cost: min(dp[i][j],cost);
					min_time = min_time<0? dp[i][j]:min(dp[i][j],min_time);
					//printf("i = %d j = %d dp = %lf\n",i,j,dp[i][j]);
				}
			}
			dis -= g[j][j+1];
		}
		dp[i][i]=min_time;
	}
	return dp[n-1][n-1];
}

int main()
{
	int T;
	cin>>T;
	fr(ca,0,T) {
		cin>>n>>q;
		for(int i = 0; i < n; ++i) {
			cin>>k[i]>>s[i];
		}
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n; ++j ) {
				cin>>g[i][j];
			}
		}
		while(q--){
			int u,v;
			cin>>u>>v;
			printf("Case #%d: %.7lf\n",ca+1,solve_small());
		}
	}
}
