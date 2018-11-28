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
const int N=1005;
int a[N],ans,i,j,K,len,pp,T,l;
char s[N];
int main()
{
//	freopen("t1.in","r",stdin);
//	freopen("A-data2.out","w",stdout);
	scanf("%d\n",&T);
	fo(l,1,T)
	{
		scanf("%s",s+1);
		len=strlen(s+1);
		fo(i,1,len) if (s[i]=='+') a[i]=1;else a[i]=0;
		scanf("%d\n",&K);
		ans=0;
		fo(i,1,len-K+1)
			if (!a[i])
			{
				fo(j,i,i+K-1)
					a[j]^=1;
				ans++;
			}
		pp=1;
		fo(i,len-K+1,len) 
			if (!a[i])
				pp=0;
		printf("Case #%d: ",l);
		if (!pp) printf("IMPOSSIBLE\n");else
		printf("%d\n",ans);
	}
}
