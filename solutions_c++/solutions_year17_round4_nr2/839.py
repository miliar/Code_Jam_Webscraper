#include<bits/stdc++.h>
using namespace std;

int a[5][1005];

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T,_,n,m,p,x,y,i,s1,s2;
	for(scanf("%d",&T),_=1;_<=T;_++) {
		memset(a,0,sizeof(a));
		scanf("%d%d%d",&n,&m,&p);
		for(i=0;i<p;i++) {
			scanf("%d%d",&x,&y);
			a[y-1][x]++;a[y-1][0]+=x>1;
		}
		s1=s2=0;
		a[1][0]-=min(a[0][1],a[1][0]);
		a[0][0]-=min(a[1][1],a[0][0]);
		s1+=max(a[0][0],a[1][0]);
		//printf("%d %d %d\n",s1,a[0][1],a[1][1]);
		if(a[0][0]>0&&a[1][0]>0) {
			if(a[0][0]<a[1][0]) for(i=0;i<=n;i++) swap(a[0][i],a[1][i]);
			a[0][0]+=a[1][1];a[1][0]+=a[0][1];
			a[0][0]+=a[0][1];a[1][0]+=a[1][1];
			for(i=2;i<=n;i++) s2+=max(0,a[1][i]+a[0][i]-a[0][0]);
		}
		s1+=a[0][1]+a[1][1];
		printf("Case #%d: %d %d\n",_,s1,s2),fprintf(stderr,"Case #%d: %d %d\n",_,s1,s2);
	}
	return 0;
}
