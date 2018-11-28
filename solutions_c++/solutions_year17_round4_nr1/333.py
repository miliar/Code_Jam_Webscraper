#include <bits/stdc++.h>
using namespace std;

int T,n,i,j,k,l,p;
int a[1111],x[5];

int f[5][111][111][111];

int get(int t){
	//printf("%d\n",t);
	
	if(x[1]==0&&x[2]==0&&x[3]==0)
		return 0;

	int&now = f[t][x[1]][x[2]][x[3]];

	if(now!=-1)
		return now;

	now = -int(1e9);
	for(int i=1;i<p;i++){
		if(x[i]>0){
			x[i]--;
			int tmp=get(((t-i)%p+p)%p);
			if(t==0)tmp++;
			//printf("%d %d %d:%d,%d\n",x[1],x[2],x[3],now,i);

			now=max(now,tmp);
			x[i]++;
		}
	}
	
	return now;
}
int main(){
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++){
		scanf("%d%d",&n,&p);
		int ans=0;
		memset(x,0,sizeof(x));
		for(int i=1;i<=n;i++){
			scanf("%d",&a[i]),a[i]%=p;
			x[a[i]]++;
		}
		memset(f,-1,sizeof(f));
		int zz = get(0);

		printf("Case #%d: %d\n",ca,x[0]+zz);
	}

	return 0;
}
