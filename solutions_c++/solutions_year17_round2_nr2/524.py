#include<bits/stdc++.h>
using namespace std;

#define _swp(x,y) swap(a[x],a[0]),swap(a[y],a[3]),swap(cc[x],cc[0]),swap(cc[y],cc[3])

const char c[10]="ROYGBV";
char s[1005],cc[10];

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T,_,n,a[6],i,j,k,l,f;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%d",&n);f=0;
		for(i=0;i<6;i++) scanf("%d",&a[i]),cc[i]=c[i];
		f=!a[0]+!a[2]+!a[4];f=f>=2;
		if((a[1]>0&&a[1]-f>=a[4])||(a[3]>0&&a[3]-f>a[0])||(a[5]>0&&a[5]-f>=a[2])) {
			printf("Case #%d: IMPOSSIBLE\n",_),fprintf(stderr,"Case #%d: IMPOSSIBLE\n",_);
			continue;
		}
		a[0]-=a[3],a[2]-=a[5],a[4]-=a[1];
		if(a[2]>a[0]) _swp(2,5);
		if(a[4]>a[0]) _swp(4,1);
		if(a[0]>a[2]+a[4]) {
			printf("Case #%d: IMPOSSIBLE\n",_),fprintf(stderr,"Case #%d: IMPOSSIBLE\n",_);
			continue;
		}
		if(f) a[0]=a[3],a[2]=a[5],a[4]=a[1];
		for(i=0,l=-1;i<n;l=j) {
			for(j=0;j<6;j+=2) {
				if(j!=l&&(l==0||a[j]>=a[0])&&(l==2||a[j]>=a[2])&&(l==4||a[j]>=a[4])) {
					s[i++]=cc[j];a[j]--;
					for(k=(j+3)%6;a[k];a[k]--) s[i++]=cc[k],s[i++]=cc[j];
					break;
				}
			}
		}
		s[n]=0;
		printf("Case #%d: %s\n",_,s),fprintf(stderr,"Case #%d: %s\n",_,s);
	}
	return 0;
}
