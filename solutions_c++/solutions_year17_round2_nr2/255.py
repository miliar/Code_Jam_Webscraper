#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;

const int maxn=1005;

int n,R,O,Y,G,B,V,a[5];
int bz[maxn];

int T;
int main()
{
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%d",&n);
		scanf("%d %d %d %d %d %d",&a[1],&O,&a[2],&G,&a[3],&V);
		
		int f1=(a[1]<a[2]) ?1 :2 ; if (a[3]<a[f1]) f1=3;
		int f3=(a[1]>a[2]) ?1 :2 ; if (a[3]>a[f3]) f3=3;
		if (f1==f3)
			fo(i,1,3) if (a[f1]==a[f3] && i!=f1) {f3=i; break;}
		int f2=6-f1-f3;
		
		memset(bz,0,sizeof(bz));
		fo(i,1,n) if (a[f3] && (i&1)) bz[i]=f3, a[f3]--;
		if (a[f3]) {printf("IMPOSSIBLE\n"); continue;}
		
		int last=(a[f1]>0) ?f1 :f2 ;
		bool pd=0, asv=1;
		fd(i,n,1) if (!bz[i])
		{
			if (a[last]<=0 && pd) last=(last==f1) ?f2 :f1 ;
			if (a[last]<=0) {asv=0; break;}
			bz[i]=last;
			a[last]--;
			if (!pd) last=(last==f1) ?f2 :f1 ;
				else if (a[last]<=0) last=(last==f1) ?f2 :f1 ;
		} else pd=1;
		
		if (!asv) {printf("IMPOSSIBLE\n"); continue;}
		fo(i,1,n) if (bz[i]==1) printf("R");
			else if (bz[i]==2) printf("Y");
				else printf("B");
		printf("\n");
	}
}