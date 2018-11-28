#include<bits/stdc++.h>
using namespace std;
int T,x,a[10],s,t,n,p,i,ans;
int main(){
	//freopen("B.in","r",stdin);
	//freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		memset(a,0,sizeof(a));
		scanf("%d%d",&n,&p);
		for(i=1;i<=n;i++)scanf("%d",&x),a[x%p]++;
		printf("Case #%d: ",_);
		if(p==2)printf("%d\n",n-(a[1]>>1));
		if(p==3){
			t=min(a[1],a[2]);
			s=max(a[1],a[2])-t;
			printf("%d\n",n-(t+s-(s+2)/3));
		}
		if(p==4){
			t=min(a[1],a[3]);
			s=max(a[1],a[3])-t;
			ans=a[0]+t;
			if(a[2]*2>s)ans+=s/2,a[2]-=s/2,s=s&1;
			else ans+=a[2],s-=a[2]*2,a[2]=0;
			ans+=(s+3)/4+(a[2]+1)/2;
			if(s&&(a[2]&1))ans--;
			printf("%d\n",ans);
		}
	}
}
