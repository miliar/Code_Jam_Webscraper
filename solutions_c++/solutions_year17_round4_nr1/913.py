#include<bits/stdc++.h>
using namespace std;

int c[5];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,_,n,m,s,i,x;
	for(scanf("%d",&T),_=1;_<=T;_++) {
		s=c[0]=c[1]=c[2]=c[3]=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++) {
			scanf("%d",&x);
			c[x%m]++;
		}
		switch(m) {
		case 2: s=c[0]+(c[1]+1)/2;break;
		case 3: s=c[0]+min(c[1],c[2])+(max(c[1],c[2])-min(c[1],c[2])+2)/3;break;
		case 4:
			s=c[0];
			x=min(c[1],c[3]);s+=x;c[1]-=x,c[3]-=x;
			c[2]+=c[1]/2+c[3]/2;s+=c[2]/2;
			s+=c[1]&1||c[2]&1||c[3]&1;
		}
		printf("Case #%d: %d\n",_,s),fprintf(stderr,"Case #%d: %d\n",_,s);
	}
	return 0;
}
