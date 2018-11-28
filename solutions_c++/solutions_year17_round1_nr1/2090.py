#include<bits/stdc++.h>
using namespace std;

int T;
int m,n;
int f[33][33];
string str;
int xl[33],xr[33],yl[33],yr[33];

void kz(int u)
{
    vector<int>x;
    vector<int>y;
    for(int i=1;i<=m;i++)
        for(int j=1;j<=n;j++)
            if(f[i][j]==u)
            {
                x.push_back(i);
                y.push_back(j);
            }
    sort(x.begin(),x.end());
    sort(y.begin(),y.end());
    if(x.size()!=0)
    {
        xl[u]=x[0];
        xr[u]=x[x.size()-1];
        yl[u]=y[0];
        yr[u]=y[y.size()-1];

        for(int i=xl[u];i<=xr[u];i++)
            for(int j=yl[u];j<=yr[u];j++)
                f[i][j]=u;
    }
}

int kz2(int u)
{
    int ret = 0;
    if(xl[u]!=0)
    {
        //cout<<"kz2 "<<u<<" "<<xl[u]<<" "<<xr[u]<<endl;
        int minyl=yl[u],maxyr=yr[u];
        for(int i=yl[u]-1;i>=1;i--)
        {
            bool same = 1;
            for(int j=xl[u];j<=xr[u];j++)
                if(f[j][i]!=-1)
                    same=0;
            if(same)
            {
                for(int j=xl[u];j<=xr[u];j++)
                    f[j][i]=u;
                minyl = i;
                ret++;
            }            else
                break;
        }

        
        for(int i=yr[u]+1;i<=n;i++)
        {
            //cout<<"i="<<i<<endl;
            bool same = 1;
            for(int j=xl[u];j<=xr[u];j++)
                if(f[j][i]!=-1)
                {
                    //cout<<"j="<<j<<" not"<<endl;
                    same=0;
                }
            if(same)
            {
                for(int j=xl[u];j<=xr[u];j++)
                    f[j][i]=u;
                maxyr=i;
                ret++;
            }            else
                break;
        }
        yl[u]=minyl;
        yr[u]=maxyr;
    }
    return ret;
}

int kz3(int u)
{
    int ret = 0;
    if(xl[u]!=0)
    {
        int minxl=xl[u],maxxr=xr[u];
        for(int i=xl[u]-1;i>=1;i--)
        {
            bool same = 1;
            for(int j=yl[u];j<=yr[u];j++)
                if(f[i][j]!=-1)
                    same=0;
            if(same)
            {
                for(int j=yl[u];j<=yr[u];j++)
                    f[i][j]=u;
                minxl = i;
                ret++;
            }
            else
                break;
        }

        
        for(int i=xr[u]+1;i<=m;i++)
        {
            bool same = 1;
            for(int j=yl[u];j<=yr[u];j++)
                if(f[i][j]!=-1)
                    same=0;
            if(same)
            {
                for(int j=yl[u];j<=yr[u];j++)
                    f[i][j]=u;
                maxxr=i;
                ret++;
            }
            else
                break;
        }
        xl[u]=minxl;
        xr[u]=maxxr;
    }
    return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out2","w",stdout);
    
    cin>>T;
    for(int it=1;it<=T;it++)
    {
        memset(xl,0,sizeof(xl));
        memset(xr,0,sizeof(xr));
        memset(yl,0,sizeof(yl));
        memset(yr,0,sizeof(yr));
        cin>>m>>n;
        for(int i=1;i<=m;i++)
        {
            cin>>str;
            for(int j=1;j<=n;j++)
                f[i][j]=str[j-1]=='?'?-1:str[j-1]-'A';
        }
        for(int i=0;i<26;i++)
            kz(i);
        for(int i=0;i<26;i++)
            kz3(i);
        for(int i=0;i<26;i++)
            kz2(i);
        cout<<"Case #"<<it<<":"<<endl;
        for(int i=1;i<=m;i++)
        {
            for(int j=1;j<=n;j++)
                printf("%c",f[i][j]+'A');
            printf("\n");
        }
    }
    return 0;
}
