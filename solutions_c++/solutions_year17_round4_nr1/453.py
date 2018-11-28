#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int f[110][110][110];
void upd(int &x,int y) {x=max(x,y);}
int check(int x,int y,int z) {
	return (x+y*2+z*3)%4==0;
}
int a[5];
int main(){
	int T,n,p,x;
	freopen("1.in","r",stdin);
//	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		scanf("%d%d",&n,&p);
		memset(a,0,sizeof(a));
		for (int i=1;i<=n;i++) {
			scanf("%d",&x);
			a[x%p]++;
		}
		printf("%d %d %d %d\n",a[0],a[1],a[2],a[3]);
		int ans =0;
		if (p==2) ans=a[0]+((a[1]-1)/2+bool(a[1]));
		else if (p==3) ans=a[0]+min(a[1],a[2])+(abs(a[1]-a[2])-1)/3+bool(abs(a[1]-a[2]));
		else {
			for (int i=0;i<=a[1];i++)
				for (int j=0;j<=a[2];j++) 
					for (int k=0;k<=a[3];k++) {
						f[i][j][k]=0;
						if (i>0) upd(f[i][j][k],f[i-1][j][k]+check(i-1,j,k));
						if (j>0) upd(f[i][j][k],f[i][j-1][k]+check(i,j-1,k));
						if (k>0) upd(f[i][j][k],f[i][j][k-1]+check(i,j,k-1));
					}
			ans=f[a[1]][a[2]][a[3]]+a[0];
		}
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
