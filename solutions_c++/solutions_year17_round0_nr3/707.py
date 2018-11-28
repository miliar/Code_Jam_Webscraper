#include<cstdio>
#include<algorithm>
#include<cstring>
#include<bitset>
#include<cmath>
#define fo(i,j,k) for(i=j;i<=k;i++)
#define fd(i,j,k) for(i=j;i>=k;i--)
typedef long long ll;
typedef double db;
using namespace std;
struct rec
{
	ll a,cnt;
}b[10];
ll a[105][2],cnt[105][2],n,K,siz,amn,amx,ct,l;// 0,bigger, 1 smaller
int TT,T,i,j,k,ta,tt;
bool cmp(rec a,rec b)
{
	return a.a>b.a;
}
int main()
{
//	freopen("t3.in","r",stdin);
//	freopen("C-data3.out","w",stdout);
	scanf("%d\n",&T);
	fo(TT,1,T)
	{
		fo(i,1,100) fo(j,0,1) a[i][j]=cnt[i][j]=0;
		scanf("%lld %lld",&n,&K);
		a[1][0]=n;
		cnt[1][0]=1;
		siz=1;
		fo(i,1,100)
		{
			tt=0;
			fo(l,0,1)
			if (cnt[i][l])
			{
				if (a[i][l]) a[i][l]--;
				b[++tt].a=a[i][l]/2;
				b[tt].cnt=cnt[i][l];
				b[++tt].a=a[i][l]/2+a[i][l]%2;
				b[tt].cnt=cnt[i][l];
			}
			sort(b+1,b+1+tt,cmp);
			ta=0;
			fo(j,1,tt)
			{
				k=j;
				ct=b[j].cnt;
				while (k<tt&&b[j].a==b[k+1].a) k++,ct+=b[k].cnt;
				a[i+1][ta]=b[j].a;
				cnt[i+1][ta]=ct;
				j=k;
				ta++;
			}
			K-=siz;
			if (K<=0) break;
			siz*=2;
		}
		K+=siz;
		if (cnt[i][0]>=K) ta=0;else ta=1;
		amn=a[i][ta]/2;
		amx=a[i][ta]/2+a[i][ta]%2;
		printf("Case #%d: ",TT);
		printf("%lld %lld\n",amx,amn);
	}
}
