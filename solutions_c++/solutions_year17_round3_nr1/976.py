#include<iostream>
#include<vector>
#include<utility>
using namespace std;

#define PI 3.141592653589793238462643

int N,K;
vector <pair <int,int> > v;
long long dp[1003][1003][2];
struct greater1
{
    template<class T>
    bool operator()(T const &a, T const &b) const { return a > b; }
};

long long rec(int pos,int rem, int prev){
	if(pos==N && rem==0 && prev==1)
		return 0;
	if(pos>=N)
		return -100000000000000000L;
	if(dp[pos][rem][prev]!=-1)
		return dp[pos][rem][prev];
	long long ans=0;
	long long r = v[pos].first;
	long long h = v[pos].second;
	// printf("%d %d %d\n",pos,r,h);
	if(prev == 0){
		ans = max(2*r*h + r*r + rec(pos+1,rem-1,1), rec(pos+1, rem, prev));
	}
	else{
		ans = max(2*r*h + rec(pos+1,rem-1,1), rec(pos+1, rem, prev));
	}
	dp[pos][rem][prev] = ans;
	return ans;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		memset(dp,-1,sizeof(dp));
		v.clear();

		scanf("%d %d",&N,&K);
		for(int i=0;i<N;++i){
			int h,r;
			scanf("%d %d",&r,&h);
			v.push_back(make_pair(r,h));
		}
		sort(v.begin(),v.end(), greater1());

		printf("Case #%d: ",t);
		printf("%.7lf\n",(double)rec(0,K,0) * PI);
	}
}