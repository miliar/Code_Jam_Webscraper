#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define maxn 1000005
using namespace std;

int T,n,k;

struct note{
	int dis,wz;
}a[2][maxn];

int tot1,tot2;

bool cmp(note i,note j){
	return i.dis>j.dis || i.dis==j.dis && i.wz<j.wz;
}

int main(){
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&T);
	fo(test,1,T) {
		tot1=tot2=0;
		scanf("%d%d",&n,&k);
		int now=0,las=1;
		tot1=1;
		a[now][tot1].dis=n;
		a[now][tot1].wz=0;
		int z1=0;
		fo(i,1,k) {
			z1++;
			if (z1>tot1) {
				swap(now,las);
				swap(tot1,tot2);
				sort(a[now]+1,a[now]+tot1+1,cmp);
				tot2=0;
				z1=1;
			}
			int nwz=a[now][z1].wz;
			int ndis=a[now][z1].dis;
			int nnwz=nwz+ndis+1;
			int newwz=nwz+(ndis+1) / 2;
			if (i==k) {
				int mn=min(newwz-nwz,nnwz-newwz);
				int mx=max(newwz-nwz,nnwz-newwz);
				printf("Case #%d: %d %d\n",test,mx-1,mn-1);
				break;
			}
			if (newwz-nwz>1) {
				++tot2;
				a[las][tot2].wz=nwz;
				a[las][tot2].dis=newwz-nwz-1;
			}
			if (nnwz-newwz>1) {
				++tot2;
				a[las][tot2].wz=newwz;
				a[las][tot2].dis=nnwz-newwz-1;
			}
		}
	}
	return 0;
}
