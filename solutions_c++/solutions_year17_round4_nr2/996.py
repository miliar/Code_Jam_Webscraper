#include<stdio.h>
#include<algorithm>

using namespace std;

pair<int,int> tic[1001];

int n,m,c,checkF[1001],checkS[1001];

int main()
{
	freopen("C:\\Users\\Administrator\\Downloads\\B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t,i,j;
	scanf("%d",&t);

	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d%d%d",&n,&c,&m);
		for(i=1;i<=c;i++)checkS[i]=0;
		for(i=1;i<=n;i++)checkF[i]=0;
		for(i=1;i<=m;i++)
		{
			scanf("%d%d",&tic[i].first,&tic[i].second);
			checkF[tic[i].first]++;
			checkS[tic[i].second]++;
		}

		int y=0,z=0,tmp=0;
		y = max(checkS[1],checkS[2]);
		y = max(y,checkF[1]);

		for(i=1;i<=n;i++)
		{
			if(checkF[i]>y)z+=checkF[i]-y;
		}
		
		printf("Case #%d: %d %d\n",tt,y,z);
	}

	return 0;
}