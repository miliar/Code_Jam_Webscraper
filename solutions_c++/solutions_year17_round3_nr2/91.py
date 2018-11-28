#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=15e2+1;
const double pi=acos(-1);
int a[N][N/2][2],b[N][2];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int n[2],i,j,l;
        cin>>n[0]>>n[1];
        memset(a,0,sizeof a);
        memset(b,0,sizeof b);
        for(i=0;i<2;i++)
            for(j=0;j<n[i];j++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            for(l=x;l<y;l++)b[l][i]=1;
        }
        for(i=0;i<=24*60;i++)
            for(j=0;j<=720;j++)a[i][j][0]=a[i][j][1]=N;
        a[0][0][0]=a[0][0][1]=0;
        for(i=1;i<=24*60;i++)
            for(j=max(i-720,0);j<=min(720,i);j++)
        {
            a[i][j][0]=a[i][j][1]=N;
            if(!b[i][0]&&j)a[i][j][0]=min(a[i-1][j-1][0],a[i-1][j-1][1]+1);
            if(!b[i][1])a[i][j][1]=min(a[i-1][j][0]+1,a[i-1][j][1]);
        }
        printf("%d\n",min(a[24*60][720][0]+b[0][0],a[24*60][720][1]+b[0][1])+(min(a[24*60][720][0]+b[0][0],a[24*60][720][1]+b[0][1])&1));
    }
	return 0;
}
