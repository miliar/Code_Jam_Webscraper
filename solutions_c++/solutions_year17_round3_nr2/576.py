#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
typedef pair<int,int> ii;
#define fi first
#define se second
#define maxn 410
#define inf 1000000000
ii a[maxn];
int f[maxn][1450][2];
void  upd(int &x,int y) {
	x=min(x,y);
}
int main(){
	freopen("1.in","r",stdin);
//	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	int l =0;
	for (int _=1;_<=T;_++) {
		int n,m;
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++) {
			int x,y;
			scanf("%d%d",&x,&y);
			a[++l]=ii(x,0);
			a[++l]=ii(y,2);
		}
		for (int i=1;i<=m;i++) {
			int x,y;
			scanf("%d%d",&x,&y);
			a[++l]=ii(x,1);
			a[++l]=ii(x,2);
		}
		sort(a+1,a+1+l);
		a[0]=ii(0,2);
		if (a[l].fi!=1440) a[++l]=ii(1440,2);
		for (int i=0;i<=l;i++)
			for (int j=0;j<=720;j++)
				for (int k =0;k<=1;k++) f[i][j][k]=inf;
		f[0][0][0]=f[0][0][1]=0;
		for (int i=0;i<l;i++) {
			for (int j=0;j<=720;j++) 
				for (int k=0;k<=1;k++) {
					if (f[i][j][k]==inf) continue;
					int le[2]={a[i].fi-j,j};
					int len = a[i+1].fi-a[i].fi;
					if (a[i].se<2) {
						int p = a[i].se^1;
						if (len > 720-le[p]) continue;
						upd(f[i+1][j+p*len][p],f[i][j][k]+(k!=p));
						continue;
					}
					for (int l=0;l<=1;l++) {
						if (len<720-le[l])
							upd(f[i+1][j+l*len][l],f[i][j][k]+(k!=l));
					}
					for (int l=a[i].fi+1;l<a[i+1].fi;l++) {
						int l1=l-a[i].fi,l2=a[i+1].fi-l;
						if (l1<=720-le[k]&&l2<=720-le[k^1])
							upd(f[i+1][j+k*l1+(k^1)*l2][k^1],f[i][j][k]+1);
						if (l1<=720-le[k^1]&&l2<=720-le[k]) 
							upd(f[i+1][j+k*l2+(k^1)*l1][k],f[i][j][k]+2);
					}
				}
		}
		printf("Case #%d: %d\n",_,min(f[l][720][0],f[l][720][1]));
	}
	return 0;
}

