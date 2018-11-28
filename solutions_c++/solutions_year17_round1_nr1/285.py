#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxn=1000005;

int n,m;
char c[55][55];

void solve()
{
    int i,j,k;
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++) scanf("%s",c[i]);
    for(i=0;i<n;i++)
    {
        k=0;
        for(j=0;j<m;j++)
        {
            if(c[i][j]!='?')
            {
                for(k=j-1;k>=0&&c[i][k]=='?';k--) c[i][k]=c[i][j];
            }
        }
        for(j=m-1;j>=0&&c[i][j]=='?';j--);
        if(j>=0) for(k=j+1;k<m;k++) c[i][k]=c[i][j];
    }
    for(i=0;i<n;i++)
    {
        if(c[i][0]!='?')
        {
            for(j=i-1;j>=0&&c[j][0]=='?';j--)
            {
                for(k=0;k<m;k++) c[j][k]=c[i][k];
            }
        }
    }
    for(i=n-1;i>=0&&c[i][0]=='?';i--);
    for(j=i+1;j<n;j++) for(k=0;k<m;k++) c[j][k]=c[i][k];
    for(i=0;i<n;i++) printf("%s\n",c[i]);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,j;
	scanf("%d",&T);
	for(int ca=1;ca<=T;++ca)
	{
		printf("Case #%d:\n",ca);
		solve();
		cerr<<"Case #"<<ca<<" done\n";
	}
	return 0;
}
