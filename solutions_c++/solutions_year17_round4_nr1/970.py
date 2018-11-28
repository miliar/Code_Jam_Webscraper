#include<bits/stdc++.h>
using namespace std;

#define pb push_back
typedef long long ll;

const int maxn=1005;

int n,p;
int a[5];

void solve()
{
    int i,j,k;
    memset(a,0,sizeof(a));
    scanf("%d %d",&n,&p);
    for(i=0;i<n;i++)
    {
        int x;
        scanf("%d",&x);
        a[x%p]++;
    }
    int r=0;
    if(p==2)
    {
        r=a[0]+(a[1]+1)/2;
    }
    if(p==3)
    {
        r=a[0];
        r+=min(a[1],a[2]);
        if(a[1]>a[2])
        {
            r+=(a[1]-a[2])/3+((a[1]-a[2])%3!=0);
        }
        else
        {
            r+=(a[2]-a[1])/3+((a[2]-a[1])%3!=0);
        }
    }
    if(p==4)
    {
        r=a[0]+min(a[1],a[3])+a[2]/2;
        a[2]%=2;
        if(a[1]>a[3])
        {
            a[1]-=a[3];
            if(a[2]>0&&a[1]>=2)
            {
                a[1]-=2,a[2]=0,++r;
            }
            r+=a[1]/4+(a[1]%4!=0);
            if(a[2]>0&&a[1]%4==0) ++r;
        }
        else
        {
            a[3]-=a[1];
            if(a[2]>0&&a[3]>=2)
            {
                a[3]-=2,a[2]=0,++r;
            }
            r+=a[3]/4+(a[3]%4!=0);
            if(a[2]>0&&a[3]%4==0) ++r;
        }
    }
    printf(" %d\n",r);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,j;
	scanf("%d",&T);
	for(int ca=1;ca<=T;++ca)
	{
		printf("Case #%d:",ca);
		solve();
		cerr<<"Case #"<<ca<<" done\n";
	}
	return 0;
}
