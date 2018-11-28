#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define gc getchar
#define pb push_back
#define eb emplace_back
typedef pair<int,int> pii;
typedef long double LD;
typedef long long LL;
int tc,n,p,occ[10],ans;
int main()
{
	freopen("ASmall.in","r",stdin);
	freopen("ASmall.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		scanf("%d%d",&n,&p);
		memset(occ,0,sizeof(occ));
		for(int i=1;i<=n;i++)
		{
			int input;
			scanf("%d",&input);
			occ[input%p]++;
		}
		ans=0;
		if(p==2)
		{
			ans+=occ[0];
			occ[0]=0;
			ans+=(occ[1]+1)>>1;
		}
		else if(p==3)
		{
			ans+=occ[0];
			occ[0]=0;
			int temp=min(occ[1],occ[2]);
			occ[1]-=temp;
			occ[2]-=temp;
			ans+=temp;
			if(occ[1]!=0)
				ans+=(occ[1]+2)/3;
			else
				ans+=(occ[2]+2)/3;
		}
		else if(p==4)
		{
			ans+=occ[0];
			occ[0]=0;
			int temp=min(occ[1],occ[3]);
			occ[1]-=temp;
			occ[3]-=temp;
			ans+=temp;
			temp=occ[2]>>1;
			occ[2]-=temp*2;
			ans+=temp;
			//kasus 3
			if(occ[2]!=0)
			{
				assert(occ[2]==1);
				if(max(occ[1],occ[3])>=2)
				{
					occ[2]--;
					if(occ[1]>occ[3])
						occ[1]-=2;
					else
						occ[3]-=2;
					ans++;
				}
			}
			
			ans+=(max(occ[1],occ[3])+3)/4;
		}
		printf("Case #%d: %d\n",test,ans);
	}
}
