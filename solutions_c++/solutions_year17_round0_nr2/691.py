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
const int N=25;
ll n,ten[N],ans,f[N][10][2];
int a[N],T,TT,i,j,k;
int main()
{
//	freopen("t2.in","r",stdin);
//	freopen("B-data2.out","w",stdout);
	scanf("%d\n",&T);
	fo(TT,1,T)
	{
		scanf("%lld",&n);
		fo(i,0,18) a[i]=n%10,n/=10;
		ten[0]=1;
		fo(i,1,18) ten[i]=ten[i-1]*(ll)10;
		fo(i,0,19) fo(j,0,9) fo(k,0,1) f[i][j][k]=0;
		ans=0;
		f[19][0][1]=1;
		fd(i,19,1)
			fo(j,0,9)
			{
				if (f[i][j][0])
					fo(k,j,9)
						f[i-1][k][0]=max(f[i-1][k][0],f[i][j][0]+ten[i-1]*k);
				if (f[i][j][1])
					fo(k,j,a[i-1])
						f[i-1][k][k==a[i-1]]=max(f[i-1][k][k==a[i-1]],f[i][j][1]+ten[i-1]*k);
			}
		fo(i,0,9)
			ans=max(ans,max(f[0][i][0],f[0][i][1]));
		printf("Case #%d: ",TT);
		printf("%lld\n",ans-1);
	}
}
