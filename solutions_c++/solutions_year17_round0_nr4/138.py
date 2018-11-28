#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#define CLR(a,x) memset(a,x,sizeof(a))
#define LL int
using namespace std;
const int maxn=11000;
const int maxm=2e5+10;
const LL INF=0x3f3f3f3f;
template <typename T> inline void read(T &x)
{
    x=0;bool f=false;char ch=getchar();
    while (ch<'0'||'9'<ch) {if(ch=='-')f=!f;ch=getchar();}
    while ('0'<=ch&&ch<='9') {x=x*10+ch-'0';ch=getchar();}
    if (f) x=-x;
}
inline void readc(char &ch)
{
    ch=getchar();
    while (!(ch=='o'||ch=='x'||ch=='+'||ch=='.')) ch=getchar();
}
struct ISAP
{
    int n,m,s,t;
    struct EDGE
    {
        int from,to;
        LL cap,flow;
        EDGE(){}
        EDGE(int _from,int _to,LL _cap,LL _flow){from=_from;to=_to;cap=_cap;flow=_flow;}
    }edge[maxm];
    vector <int>G[maxn];
    bool vis[maxn];
    int num[maxn],pre[maxn],d[maxn],cur[maxn];
    void init(int _n,int _s,int _t)
    {
        n=_n;s=_s;t=_t;m=0;
        for (int i=0;i<n;i++) G[i].clear();
    }
    void addedge(int from,int to,LL cap)
    {
        edge[m]=EDGE(from,to,cap,0);G[from].push_back(m++);
        edge[m]=EDGE(to,from,0,0);G[to].push_back(m++);
    }
    bool BFS()
    {
        CLR(vis,false);vis[t]=true;
        queue<int>Q;Q.push(t);
        d[t]=0;
        while (!Q.empty())
        {
            int x=Q.front();Q.pop();
            for (int i=0;i<G[x].size();i++)
            {
                EDGE &e=edge[G[x][i]^1];
                if (!vis[e.from]&&e.cap>e.flow)
                {
                    vis[e.from]=true;
                    d[e.from]=d[x]+1;
                    Q.push(e.from);
                }
            }
        }
        return vis[s];
    }
    LL Augment()
    {
        int x=t;
        LL a=INF;
        while (x!=s)
        {
            EDGE e=edge[pre[x]];
            a=min(a,e.cap-e.flow);
            x=e.from;
        }
        x=t;
        while (x!=s)
        {
            edge[pre[x]].flow+=a;
            edge[pre[x]^1].flow-=a;
            x=edge[pre[x]].from;
        }
        return a;
    }
    LL Maxflow()
    {
        LL flow=0;
        if (!BFS()) return 0;
        CLR(num,0);
        for (int i=0;i<n;i++) num[d[i]]++;
        int x=s;CLR(cur,0);
        while (d[s]<n)
        {
            if (x==t) {flow+=Augment();x=s;}
            bool advance=false;
            for (int i=cur[x];i<G[x].size();i++)
            {
                EDGE e=edge[G[x][i]];
                if (e.cap>e.flow&&d[x]==d[e.to]+1)
                {
                    advance=true;
                    cur[x]=i;pre[e.to]=G[x][i];
                    x=e.to;break;
                }
            }
            if (!advance)
            {
                int m=n-1;
                for (int i=0;i<G[x].size();i++)
                {
                    EDGE e=edge[G[x][i]];
                    if (e.cap>e.flow) m=min(m,d[e.to]);
                }
                if (--num[d[x]]==0) break;
                num[d[x]=m+1]++;
                cur[x]=0;
                if (x!=s) x=edge[pre[x]].from;
            }
        }
        return flow;
    }
}isap1,isap2;
int n,m,bk;
char maz[110][110],a[110][110];
int b[110][110],c[110][110];
bool X[210],Y[210];
int dx[110][110],dy[110][110];
void init()
{
    for (int i=1;i<=n;i++)
            for (int j=1;j<=n;j++) b[i][j]=-1,c[i][j]=-1;
    for (int i=1;i<=n;i++)
        for (int j=1;j<=n;j++) maz[i][j]='.';
    bk=0;
    int p,q;
    for (int i=1;i<=n;i++)
    {
        p=i;q=1;bk++;
        while (p<=n&&q<=n&&p>=1&&q>=1)
        {
            dx[p][q]=bk;
            p++;q++;
        }
    }
    for (int j=2;j<=n;j++)
    {
        p=1;q=j;bk++;
        while (p<=n&&q<=n&&p>=1&&q>=1)
        {
            dx[p][q]=bk;
            p++;q++;
        }
    }
    bk=0;
    for (int j=1;j<=n;j++)
    {
        p=1;q=j;bk++;
        while (p<=n&&q<=n&&p>=1&&q>=1)
        {
            dy[p][q]=bk;
            p++;q--;
        }
    }
    for (int i=2;i<=n;i++)
    {
        p=i;q=n;bk++;
        while (p<=n&&q<=n&&p>=1&&q>=1)
        {
            dy[p][q]=bk;
            p++;q--;
        }
    }
//    for (int i=1;i<=n;i++)
//    {
//        for (int j=1;j<=n;j++) cout<<dx[i][j]<<" ";
//        cout<<endl;
//    }
//    for (int i=1;i<=n;i++)
//    {
//        for (int j=1;j<=n;j++) cout<<dy[i][j]<<" ";
//        cout<<endl;
//    }
}
int main()
{
    #ifdef VGel
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    #endif // VGel
    int T_T,x,y;
    char ch;
    read(T_T);
    for (int T=1;T<=T_T;T++)
    {
        read(n);read(m);
        init();
        for (int i=1;i<=m;i++) {readc(ch);read(x);read(y);maz[x][y]=ch;}

        int tmp=0;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=n;j++)
        {
            if (maz[i][j]=='o') tmp+=2;
            if (maz[i][j]=='x'||maz[i][j]=='+') tmp+=1;
        }
//        cout<<tmp<<endl;



        int s1=0,t1=n+n+1;
        isap1.init(t1+1,s1,t1);
        for (int i=1;i<=n;i++) X[i]=false;
        for (int j=1;j<=n;j++) Y[j]=false;
        for (int i=1;i<=n;i++)
        {
            for (int j=1;j<=n;j++)
            {
                //if (maz[i][j]=='.'||maz[i][j]=='+') {b[i][j]=isap1.m;isap1.addedge(i,j+n,1);}
                if (maz[i][j]=='x'||maz[i][j]=='o') {X[i]=true;Y[j]=true;}
            }
        }
        for (int i=1;i<=n;i++)
        {
            for (int j=1;j<=n;j++) if (!X[i] && !Y[j])
            {
                if (maz[i][j]=='.'||maz[i][j]=='+') {b[i][j]=isap1.m;isap1.addedge(i,j+n,1);}
                //if (maz[i][j]=='x'||maz[i][j]=='o') {X[i]=true;Y[j]=true;}
            }
        }
        for (int i=1;i<=n;i++) if (!X[i]) isap1.addedge(s1,i,1);
        for (int j=1;j<=n;j++) if (!Y[j]) isap1.addedge(j+n,t1,1);


//        cout<<isap1.Maxflow()<<endl;
        isap1.Maxflow();

//        cout<<isap1.m<<endl;

        for (int i=1;i<=bk;i++) X[i]=false;
        for (int j=1;j<=bk;j++) Y[j]=false;
        int s2=0,t2=bk*2+1;
        isap2.init(t2+1,s2,t2);
        for (int i=1;i<=n;i++)
        {
            for (int j=1;j<=n;j++)
            {
                //if (maz[i][j]=='.'||maz[i][j]=='x') {c[i][j]=isap2.m;isap2.addedge(dx[i][j],dy[i][j]+bk,1);}
                if (maz[i][j]=='+'||maz[i][j]=='o') {X[dx[i][j]]=true;Y[dy[i][j]]=true;}
            }
        }
        for (int i=1;i<=n;i++)
        {
            for (int j=1;j<=n;j++) if (!X[dx[i][j]] && !Y[dy[i][j]])
            {
                if (maz[i][j]=='.'||maz[i][j]=='x') {c[i][j]=isap2.m;isap2.addedge(dx[i][j],dy[i][j]+bk,1);}
                //if (maz[i][j]=='+'||maz[i][j]=='o') {X[dx[i][j]]=true;Y[dy[i][j]]=true;}
            }
        }
        for (int i=1;i<=bk;i++) if (!X[i]) isap2.addedge(s2,i,1);
        for (int j=1;j<=bk;j++) if (!Y[j]) isap2.addedge(j+bk,t2,1);
//        cout<<isap2.Maxflow()<<endl;
        isap2.Maxflow();





        int ans=0;
        int tot=0;

        int cnt1=0,cnt2=0,cnt3=0,cnt4=0;

        for (int i=1;i<=n;i++)
        {
            for (int j=1;j<=n;j++)
            {
                if (maz[i][j]=='x'||maz[i][j]=='o') x=1,cnt1++;
                    else if (b[i][j]!=-1) x=isap1.edge[b[i][j]].flow,cnt2+=isap1.edge[b[i][j]].flow; else x=0;
                if (maz[i][j]=='+'||maz[i][j]=='o') y=1,cnt1++;
                    else if (c[i][j]!=-1) y=isap2.edge[c[i][j]].flow,cnt3+=isap2.edge[c[i][j]].flow; else y=0;

                if (x>0&&y>0) {ch='o';ans+=2;}
                if (x>0&&y==0) {ch='x';ans+=1;}
                if (x==0&&y>0) {ch='+';ans+=1;}
                if (x==0&&y==0) ch='.';
//                ans+=(x>0)+(y>0);
                //cout<<i<<" "<<j<<" "<<" "<<x+y<<" "<<ans<<endl;

                if (ch!=maz[i][j]) tot++;
                a[i][j]=ch;
            }
        }

        printf("Case #%d: %d %d\n",T,ans,tot);
//        printf("%d %d %d\n",cnt1,cnt2,cnt3);
        for (int i=1;i<=n;i++)
            for (int j=1;j<=n;j++)
            {
                if (a[i][j]!=maz[i][j]) printf("%c %d %d\n",a[i][j],i,j);
            }
    }
    return 0;
}
