#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int tests,tc,i,j,k,n,m,a[41],ans,tmp;
int work(int a,int b,int c){
	int res=0,k;
	res=b/2;b%=2;k=min(a,c);res+=k;a-=k;c-=k;
	for (k=0;a+b+c>0;){
		if (!k) res++;
		if (b){
			k=(k+2)%4;b--;continue;
		}
		if (a){
			k=(k+1)%4;a--;
		}else{
			k=(k+3)%4;c--;
		}
	}
	return res;
}
int main(){
	for (scanf("%d",&tests),tc=1;tc<=tests;tc++){
		scanf("%d%d",&n,&m);memset(a,0,sizeof(a));
		for (i=1;i<=n;i++) scanf("%d",&k),a[k%m]++;
		ans=a[0];
		if (m==2){
			ans+=a[1]/2+a[1]%2;
		}
		if (m==3){
			k=min(a[1],a[2]);
			ans+=k;
			a[1]-=k;a[2]-=k;
			ans+=a[1]/3+(a[1]%3?1:0)+a[2]/3+(a[2]%3?1:0);
		}
		if (m==4){
			tmp=0;k=min(a[1],min(a[2],a[3]));
			for (i=0;i<=k;i+=2) tmp=max(tmp,i/2+work(a[1]-i,a[2]-i,a[3]-i));
			ans+=tmp;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
