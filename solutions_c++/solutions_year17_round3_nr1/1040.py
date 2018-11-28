/*************************************************************************
    > File Name: proa.cpp
    > Author: Yuchen Wang
    > Mail: wyc8094@gmail.com 
    > Created Time: Sun Apr 30 17:11:07 2017
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<utility>
using namespace std;

const int maxn = 1005;
#define R first
#define H second
#define PI 3.1415926535898

double dp[maxn][maxn];
pair<double,double>disk[maxn];
int T,N,K;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j;
	int ncase = 0;
	cin >> T;
	while(T--){
		printf("Case #%d: ",++ncase);
		memset(dp,0,sizeof(dp));
		cin >> N >> K;
		for(i=0;i<N;i++)
			scanf("%lf%lf",&disk[i].R,&disk[i].H);
		sort(disk,disk+N);

		for(i=N-1;i>=0;i--){
			dp[i][1] = max(dp[i+1][1],PI*disk[i].R*(disk[i].R+2*disk[i].H));
			for(j=2;j<=min(N-i,K);j++){
				dp[i][j] = max(dp[i+1][j],dp[i+1][j-1]+2*PI*disk[i].R*disk[i].H);
			}
		}
		printf("%.8f\n",dp[0][K]);
	}
}

