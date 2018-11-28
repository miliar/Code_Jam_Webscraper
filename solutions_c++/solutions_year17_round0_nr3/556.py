#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)

long long n,K;
map<long long,long long> f[2];
void init()
{
	cin>>n>>K;
	f[0].clear();
	f[0][n]=1;
}

void solve()
{
	int o=1;
	while(1)
	{
		f[o].clear();
		map<long long,long long>::iterator i=f[o^1].end();
		do
		{
			i--;
			if(i->y >= K)
			{
				cout<<max((i->x-1)/2,i->x/2)<<' '<<min((i->x-1)/2,i->x/2)<<endl;
				return;
			}else
			{
				if(f[o].count((i->x-1)/2)==0)
					f[o][(i->x-1)/2]=0;
				f[o][(i->x-1)/2]+=i->y;
				if(f[o].count((i->x)/2)==0)
					f[o][(i->x)/2]=0;
				f[o][i->x/2]+=i->y;
				K-=i->y;
			}
		}while(i!=f[o^1].begin());
		o^=1;
	}
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	REP(i,1,T)
	{
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
