#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)

const int maxn = 20;
int a[maxn];
long long n,m;

void init()
{
	cin>>n;
	if(n<10)
	{
		cout<<n<<endl;
		return;
	}
	m=0;
	memset(a,0,sizeof a);
	while(n)
	{
		a[++m]=n%10;
		n/=10;
	}
	REPD(i,m,2)
		if(a[i]>a[i-1])
		{
			if(a[i]==1)
			{
				REP(j,1,m-1)
					printf("9");
				puts("");
				return;
			}
			REP(k,1,i-1)
				a[k]=9;
			REP(k,i,m)
				if(a[k]==a[k+1])
					a[k]=9;
				else
				{
					--a[k];
					break;
				}
			break;
		}
	REPD(i,m,1)
		printf("%d",a[i]);
	puts("");
}

void solve()
{
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
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
