#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
int T,md,a[200];
LL ans=0,pw[200];
inline bool dfs(int d,int last,LL res,bool flag){
	if(d==-1){ans=res;return 1;}
	for(int i(flag?9:a[d]);i>=last;i--)
		if(dfs(d-1,i,res+i*pw[d],flag|(i<a[d])))
			return 1;
	return 0;
}
int main(){
	freopen("B-large.bin","r",stdin);
	freopen("B.out","w",stdout);
	cin>>T;
	pw[0]=1;
	for(int i(1);i<=20;i++)
		pw[i]=pw[i-1]*LL(10);
	for(int t(1);t<=T;t++){
		LL x;md=0;
		cin>>x;
		while(x){
			a[md++]=x%10;
			x/=10;
		}
		dfs(md-1,0,0,0);
		printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}
