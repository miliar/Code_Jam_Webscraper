#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#define ll long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)
using namespace std;
int a[52][52];
int req[52];
int inf=1000000000;
int par[1004],cap[10004][1004];
bool vis[1004];
queue<int> q;
bool bfs(int s,int t,int n)
{
    int i;
    for(i=1;i<=n;i++)
    {
        vis[i]=0;
    }
    vis[s]=1;
    q.push(s);
    while(!q.empty())
    {
        int x=q.front();
        q.pop();
        for(i=1;i<=n;i++)
        {
            if(!vis[i]&&cap[x][i]>0)
            {
                vis[i]=1;
                q.push(i);
                par[i]=x;
            }
        }

    }
    return vis[t];
}
int ford_fulkerson(int s,int t,int n)
{
    int totalflow=0;
    while(bfs(s,t,n))
    {
        int minflow=inf;
        for(int u=t;u!=s;u=par[u])
        {
            minflow=min(minflow,cap[par[u]][u]);
        }
        for(int u=t;u!=s;u=par[u])
        {
            cap[par[u]][u]-=minflow;
            cap[u][par[u]]+=minflow;
        }
        totalflow+=minflow;
    }
    return totalflow;
}

int main()
{
    //freopen("data4.in","r",stdin);
    //freopen("out4.txt","w",stdout);
    //freopen("data.txt","r",stdin);
    int t;
    cin>>t;
    int l1=0;
    while(t--)
    {
        l1++;
        int n,i,j,k,l,p;
        cin>>n>>p;
        for(i=0;i<n;i++)
        {
            cin>>req[i];
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<p;j++)
            {
                cin>>a[i][j];
            }
        }
        if(n==1)
        {
            req[1]=req[0];
            for(j=0;j<p;j++)
                a[1][j]=a[0][j];
            n++;
        }
        for(i=1;i<=(n*p+2);i++)
        {
            for(j=1;j<=(n*p+2);j++)
                cap[i][j]=0;
         //   cout<<"\n";
        }
        for(i=0;i<n-1;i++)
        {
            for(j=0;j<p;j++)
            {
                for(k=0;k<p;k++)
                {
                    double ad=(a[i][j]*1.0)/(1.1*req[i]);
                    double bd=(a[i][j]*1.0)/(0.9*req[i]);
                    double cd=(a[i+1][k]*1.0)/(1.1*req[i+1]);
                    double dd=(a[i+1][k]*1.0)/(0.9*req[i+1]);
                    int s1=(i*p+j)+2;
                    int t1=((i+1)*p+k)+2;
                    if(cd<ad)
                    {
                        swap(ad,cd);
                        swap(bd,dd);
                    }
                    int b1=floor(bd);
                    int c1=floor(cd);
                  /*  if(s1==2&&t1==3&&0)
                    {
                        cout<<a[i][j]<<" "<<a[i+1][k]<<" "<<req[i]<<" "<<req[i+1]<<"\n";
                        cout<<ad<<" "<<bd<<" "<<cd<<" "<<dd<<"\n";
                        cout<<b1<<" "<<c1<<"\n";
                    }*/
                    if(bd<cd)
                        cap[s1][t1]=0;
                    else if((b1==bd&&c1==cd&&b1==c1)||(b1!=c1))
                    {
                        cap[(i*p+j)+2][((i+1)*p+k)+2]=1;
                    }
                    else
                    {
                        cap[(i*p+j)+2][((i+1)*p+k)+2]=0;
                    }
                }
            }
        }
        for(i=2;i<p+2;i++)
        {
            cap[1][i]=1;
        }
        j=0;
        for(i=n*p+1;j<p;i--,j++)
        {
            cap[i][n*p+2]=1;
        }
        int n2=n*p+2;
        /*for(i=1;i<=(n*p+2);i++)
        {
            for(j=1;j<=(n*p+2);j++)
                cout<<cap[i][j]<<" ";
            cout<<"\n";
        }*/
        int maxflow=ford_fulkerson(1,n2,n2);
        cout<<"Case #"<<l1<<": ";
        cout<<maxflow<<"\n";
    }
    return 0;
}
