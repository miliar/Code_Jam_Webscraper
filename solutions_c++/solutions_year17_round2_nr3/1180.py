#include <iostream>
#include <cstdio>
using namespace std;

long long n,q,u,v;
long long e[105];
long long s[105];
long long dis[105];

double rec[105][105];

double dec(long long l,long long horse,long long remin)
{
    if(remin<0)return 9999999999999;
    if(l==n-1)return 0;
    if(rec[l][horse]!=-1)return rec[l][horse];
    return rec[l][horse]=min(dec(l+1,horse,remin-dis[l])+1.0*dis[l]/s[horse],dec(l+1,l,e[l]-dis[l])+1.0*dis[l]/s[l]);
}

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        cin>>n>>q;
        long long i,j;
        for(i=0;i<105;i++)for(j=0;j<105;j++)rec[i][j]=-1;
        for(i=0;i<n;i++)cin>>e[i]>>s[i];
        //cout<<e[i]<<" "<<s[i]<<endl;}
        for(i=0;i<n;i++)for(j=0;j<n;j++)
        {
            long long t;
            cin>>t;
            if(i+1==j)dis[i]=t;
            //cout<<i<<" "<<j<<" "<<t<<" "<<dis[i]<<endl;
        }
        cin>>u>>v;
        printf("Case #%d: %.8lf\n",tci,dec(0,0,e[0]));
    }
    return 0;
}
