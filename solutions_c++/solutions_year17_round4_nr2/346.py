#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int pd[1100][1100],m,n,C,num[1100],A[1100],rem[1100],bo[1100][1100];
struct atom{
	int where,w;
}x[1100];
int compare(atom k1,atom k2){
	return k1.where<k2.where;
}
void solve(){
	scanf("%d%d%d",&n,&C,&m);
	memset(num,0x00,sizeof num);
	memset(A,0x00,sizeof A);
	for (int i=1;i<=m;i++){
		int k1,k2; scanf("%d%d",&k1,&k2);
		x[i]=(atom){k1,k2}; num[k2]++; A[k1]++;
	}
	int lim=0;
	for (int i=1;i<=C;i++) lim=max(lim,num[i]);
	sort(x+1,x+m+1,compare); int pre=0; int ans=0; //cout<<lim<<endl;
	for (int i=1;i<=m;i++){
		pre++;
		lim=max(lim,(pre-1)/x[i].where+1);
	}
	for (int i=1;i<=n;i++) ans+=max(0,A[i]-lim);
//	cout<<A[1]<<" "<<A[2]<<" "<<lim<<" "<<ans<<" "<<num[1]<<" "<<num[2]<<endl;
	printf("%d %d\n",lim,ans);
}
int main(){
	freopen("Bl.in","r",stdin);
	freopen("Bl.out","w",stdout);
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i); solve();
	}
	return 0;
}
