#include<iostream>
#include<algorithm>
#include<map>
#include<stdio.h>
using namespace std;

typedef pair<long long,long long> P;

const double PI=3.14159265358979;
const int MAX_N=1e3+3;
long long dp[MAX_N][MAX_N];
P data[MAX_N];
int main(){
	int t;cin>>t;
	int cnt=0;
	while(cnt++<t){
		for(int i=0;i<MAX_N;i++)fill(dp[i],dp[i]+MAX_N,0);
		int k,n;
		cin>>n>>k;
		for(int i=0;i<n;i++)cin>>data[i].first>>data[i].second;
		sort(data,data+n);
		reverse(data,data+n);
		for(int i=0;i<n;i++){
			dp[i][1]=data[i].first*data[i].first+2*data[i].first*data[i].second;
			if(i>0)dp[i][1]=max(dp[i][1],dp[i-1][1]);
		}
		for(int i=1;i<n;i++){
			for(int j=2;j<=k;j++){
				dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2*data[i].first*data[i].second);
			}
		}
		printf("Case #%d: %.10f\n",cnt,PI*dp[n-1][k]);
	}
}
