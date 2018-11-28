#include <bits/stdc++.h>
using namespace std;
int n,p,a[110],b[10];

void fuck()
{
	int i,j,res=0;
	memset(b,0,sizeof(b));
	scanf("%d%d",&n,&p);
	for(i=1;i<=n;i++) scanf("%d",&a[i]);
	for(i=1;i<=n;i++) b[a[i]%p]++;
	if(p==2){
		res=b[0]+(b[1]+1)/2;
	}
	else if(p==3){
		res=b[0]+min(b[1],b[2]);
		int tmp=abs(b[1]-b[2]);
		res+=tmp/3;
		if(tmp%3!=0)
			res++;
	}
	else{
		res=b[0];
		int t=0;
		int mn=min(b[1],b[3]);
		int mx=max(b[1],b[3]);
		int pp=mx-mn;
		res+=mn;
		for(i=0;i<=pp/4;i++){
			int tmp=i;
			int r3=pp-i*4;
			if(r3/2>b[2]){
				tmp += b[2];
				r3 -= b[2]*2;
				if(r3)
					tmp++;
			}
			else{
				tmp+=r3/2;
				int r2=b[2]-r3/2;
				tmp+=r2/2;
				r2%=2;r3%=2;
				if(r2!=0||r3!=0)
					tmp++;
			}
			t=max(t,tmp);
		}
		res+=t;
	}
	printf("%d\n",res);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		fuck();
	}
	return 0;
}

