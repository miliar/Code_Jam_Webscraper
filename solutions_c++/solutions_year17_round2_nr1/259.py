#include<cstdio>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

const double inf=1e18;

int n,D;

int T;
int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%d %d",&D,&n);
		double spd=inf;
		
		fo(i,1,n)
		{
			int k,s;
			scanf("%d %d",&k,&s);
			spd=min(spd,(double)s*D/(D-k));
		}
		
		printf("%.8f\n",spd);
	}
}