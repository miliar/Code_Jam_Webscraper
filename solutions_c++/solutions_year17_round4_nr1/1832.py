#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)

const int maxn = 110;

int a[10];
int n;
int m;
int ans;

void init()
{
	memset(a,0,sizeof a);
	cin>>n>>m;
	REP(i,1,n)
	{
		int t;
		cin>>t;
		++a[t%m];
	}
	ans=a[0];
	if(m==2)
	{
		ans+=(a[1]+1)/2;
	}else if(m==3)
	{
		int t=min(a[1],a[2]);
		ans+=t;
		a[1]-=t;
		a[2]-=t;
		ans+=(a[1]+2)/3+(a[2]+2)/3;
	}else
	{
		int t=min(a[1],a[3]);
		ans += t + a[2]/2;
		a[1]-=t;
		a[3]-=t;
		a[2]%=2;
		if(a[2]) ans += (1+a[1]+a[3])/4;
		else ans += (3+a[1]+a[3])/4;
 
	}
}

void solve()
{
	cout<<ans<<endl;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
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
