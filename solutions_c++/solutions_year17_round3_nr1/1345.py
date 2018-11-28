#include<bits/stdc++.h>
using namespace std;
const double pi=3.14159265358979323846;
double _Dp[1005][1005];
struct Cake{
	int r,h;
};
Cake _C[1005];
bool cmp(Cake &a,Cake &b){
	return a.r>b.r;
}
int _n,_k;
double dfs(int i,int j){
	if(j==0||i==0)	return 0;
	if(_Dp[i][j]>0)	return _Dp[i][j];
	double ans=0;
	for(int k=j-1;k<i;k++)
		ans=max(dfs(k,j-1),ans);
	ans+=2*pi*_C[i].r*_C[i].h;
	if(j==1)	ans+=pi*_C[i].r*_C[i].r;
	ans=max(ans,dfs(i-1,j));
	_Dp[i][j]=ans;
	return ans;
}
int main(){
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		memset(_Dp,0,sizeof(_Dp));
		scanf("%d%d",&_n,&_k);
		for(int i=1;i<=_n;i++)	scanf("%d%d",&_C[i].r,&_C[i].h);
		sort(_C+1,_C+_n+1,cmp);
		printf("Case #%d: %.9lf\n",T,dfs(_n,_k));
	}
}
