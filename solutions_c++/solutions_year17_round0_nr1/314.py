#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxn=1000005;

int k,n;

char c[maxn];
int a[maxn];

void solve()
{
    n=strlen(c);
    int r=0,i,j,tmp=0;
    memset(a,0,sizeof(a));
    for(i=0;i<=n-k;i++)
    {
        tmp+=a[i];
        int cur=(c[i]=='+')+tmp;
        cur&=1;
        if(!cur)
        {
            a[i+k]=-1;
            ++tmp;++r;
        }
    }
    for(;i<n;i++)
    {
        tmp+=a[i];
        int cur=(c[i]=='+')+tmp;
        cur&=1;
        if(!cur) {printf("IMPOSSIBLE\n");return;}
    }
    printf("%d\n",r);
}

int main()
{
	freopen("Al.in","r",stdin);
	freopen("alout.txt","w",stdout);
	int T,i,j;
	scanf("%d",&T);
	for(int ca=1;ca<=T;++ca)
	{
		scanf("%s %d",c,&k);
		printf("Case #%d: ",ca);
		solve();
		cerr<<"Case #"<<ca<<" done\n";
	}
	return 0;
}
