#include <bits/stdc++.h>
using namespace std;
struct edg
{
    int t,r,c,f;
    edg(int tt,int rr,int cc,int ff)
    {
        t=tt,r=rr,c=cc,f=ff;
    }
};
vector<edg> es[70100];
int ade(int a,int b,int m)
{
    int r1=es[a].size(),r2=es[b].size();
    es[a].push_back(edg(b,r2,m,0));
    es[b].push_back(edg(a,r1,0,0));
    return r1;
}
int vi[60100];
int pt[60100];
int bfs(int s,int t)
{
    deque<int> q;
    q.push_back(s);
    int u,v;
    for(int i=0;i<=60000;i++)
        vi[i]=-1;
    vi[s]=0;
    while(q.size()!=0)
    {
        u=q[0];
        q.pop_front();
        for(int i=0;i<es[u].size();i++)
        {
            v=es[u][i].t;
            if(es[u][i].f==es[u][i].c||vi[v]!=-1)
                continue;
            vi[v]=vi[u]+1;
            q.push_back(v);
        }
    }
    return vi[t];
}
int dfs(int c,int f,int t)
{
    if(c==t)
        return f;
    int u,v,df;
    for(;pt[c]<es[c].size();pt[c]++)
    {
        int i=pt[c];
        if(vi[es[c][i].t]==vi[c]+1)
        {
            df=min(f,es[c][i].c-es[c][i].f);
            if(df==0)
                continue;
            df=dfs(es[c][i].t,df,t);
            if(df>0)
            {
                es[c][i].f+=df;
                es[es[c][i].t][es[c][i].r].f-=df;
                return df;
            }
        }
    }
    return 0;
}
int mxf(int s,int t)
{
    int fo=0;
    int dl;
    while(bfs(s,t)!=-1)
    {
        dl=1;
        for(int i=0;i<=60010;i++)
            pt[i]=0;
        while(dl!=0)
        {
            dl=dfs(s,100000000,t);
            fo+=dl;
        }
    }
    return fo;
}
int na[110][110];
int nb[110][110];
char nt[110][110];
char fn[110][110];
int nr[110];
int nc[110];
int rx[110];
int cx[110];
int nda[330];
int dap[330];
int dbp[330];
int ndb[330];
int ta[110][110];
int tb[110][110];
int main()
{
    freopen("Di.in","r",stdin);
    freopen("D.out","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int n,m;
        cin>>n>>m;
        int ns=1;
        int s=0;
        for(int i=0;i<=50000;i++)
            es[i].clear();
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                na[i][j]=ns++;
                nb[i][j]=ns++;
                nt[i][j]='.';
            }
        }
        for(int i=1;i<=n;i++)
        {
            nr[i]=ns++;
            nc[i]=ns++;
            rx[i]=0;
            cx[i]=0;
        }
        for(int i=0;i<=230;i++)
        {
            nda[i]=ns++;
            ndb[i]=ns++;
            dap[i]=0;
            dbp[i]=0;
        }
        int t=ns++;
        int cp=0;
        for(int i=1;i<=m;i++)
        {
            int rr,cc;
            char ty;
            cin>>ty>>rr>>cc;
            nt[rr][cc]=ty;
            if(ty=='+'||ty=='o')
                dap[rr+cc]=1,dbp[rr-cc+100]=1,cp++;
            if(ty=='x'||ty=='o')
                rx[rr]=1,cx[cc]=1,cp++;
        }
        for(int i=1;i<=n;i++)
        {
            ade(s,nr[i],1);
            ade(nc[i],t,1);
        }
        for(int i=0;i<=230;i++)
        {
            ade(s,nda[i],1);
            ade(ndb[i],t,1);
        }
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(rx[i]==0&&cx[j]==0&&nt[i][j]!='x'&&nt[i][j]!='o')
                {
                    ta[i][j]=ade(nr[i],na[i][j],1);
                    ade(na[i][j],nc[j],1);
                }
                if(dap[i+j]==0&&dbp[i-j+100]==0&&nt[i][j]!='+'&&nt[i][j]!='o')
                {
                    tb[i][j]=ade(nda[i+j],nb[i][j],1);
                    ade(nb[i][j],ndb[i-j+100],1);
                }
            }
        }
        //cout<<cp<<" ";
        cp+=mxf(s,t);
        //cout<<cp<<endl;
        vector<pair<char, pair<int,int> > > cg;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                fn[i][j]=nt[i][j];
                if(es[na[i][j]].size()!=0&&es[na[i][j]][0].f!=0)
                {
                    if(fn[i][j]=='+')
                        fn[i][j]='o';
                    else
                        fn[i][j]='x';
                }
                if(es[nb[i][j]].size()!=0&&es[nb[i][j]][0].f!=0)
                {
                    if(fn[i][j]=='x')
                        fn[i][j]='o';
                    else
                        fn[i][j]='+';
                }
                if(fn[i][j]!=nt[i][j])
                {
                    cg.push_back(make_pair(fn[i][j],make_pair(i,j)));
                }
            }
        }
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                //cout<<i<<" "<<j<<" "<<na[i][j]<<" "<<nb[i][j]<<endl;
                //cout<<"ROW/COL"<<endl;
                for(int k=0;k<es[na[i][j]].size();k++)
                {
                    edg x=es[na[i][j]][k];
                    //cout<<x.t<<" "<<x.r<<" "<<x.c<<" "<<x.f<<endl;
                }
                //cout<<"DIAG"<<endl;
                for(int k=0;k<es[nb[i][j]].size();k++)
                {
                    edg x=es[nb[i][j]][k];
                    //cout<<x.t<<" "<<x.r<<" "<<x.c<<" "<<x.f<<endl;
                }
            }
        }
        printf("Case #%d: %d %d\n",tt,cp,cg.size());
        for(int i=0;i<cg.size();i++)
            cout<<cg[i].first<<" "<<cg[i].second.first<<" "<<cg[i].second.second<<"\n";
    }
}
