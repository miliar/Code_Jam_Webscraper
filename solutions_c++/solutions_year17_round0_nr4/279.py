#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int MAXN = 409;//点数的最大值
const int MAXM = 40010;//边数的最大值
const int INF = 0x3f3f3f3f;
struct Edge
{
    int to,next,cap,flow;
} edge[MAXM]; //注意是MAXM
int tol;
int head[MAXN];
int gap[MAXN],dep[MAXN],cur[MAXN];
void init()
{
    tol = 0;
    memset(head,-1,sizeof(head));
}
void addedge(int u,int v,int w,int rw = 0)
{
    edge[tol].to = v;
    edge[tol].cap = w;
    edge[tol].flow = 0;
    edge[tol].next = head[u];
    head[u] = tol++;
    edge[tol].to = u;
    edge[tol].cap = rw;
    edge[tol].flow = 0;
    edge[tol].next = head[v];
    head[v] = tol++;
}
int Q[MAXN];
void BFS(int start,int end)
{
    memset(dep,-1,sizeof(dep));
    memset(gap,0,sizeof(gap));
    gap[0] = 1;
    int front = 0, rear = 0;
    dep[end] = 0;
    Q[rear++] = end;
    while(front != rear)
    {
        int u = Q[front++];
        for(int i = head[u]; i != -1; i = edge[i].next)
        {
            int v = edge[i].to;
            if(dep[v] != -1)continue;
            Q[rear++] = v;
            dep[v] = dep[u] + 1;
            gap[dep[v]]++;
        }
    }
}
int S[MAXN];
int sap(int start,int end,int N)
{
    BFS(start,end);
    memcpy(cur,head,sizeof(head));
    int top = 0;
    int u = start;
    int ans = 0;
    while(dep[start] < N)
    {
        if(u == end)
        {
            int Min = INF;
            int inser;
            for(int i = 0; i < top; i++)
                if(Min > edge[S[i]].cap - edge[S[i]].flow)
                {
                    Min = edge[S[i]].cap - edge[S[i]].flow;
                    inser = i;
                }
            for(int i = 0; i < top; i++)
            {
                edge[S[i]].flow += Min;
                edge[S[i]^1].flow -= Min;
            }
            ans += Min;
            top = inser;
            u = edge[S[top]^1].to;
            continue;
        }
        bool flag = false;
        int v;
        for(int i = cur[u]; i != -1; i = edge[i].next)
        {
            v = edge[i].to;
            if(edge[i].cap - edge[i].flow && dep[v]+1 == dep[u])
            {
                flag = true;
                cur[u] = i;
                break;
            }
        }
        if(flag)
        {
            S[top++] = cur[u];
            u = v;
            continue;
        }
        int Min = N;
        for(int i = head[u]; i != -1; i = edge[i].next)
            if(edge[i].cap - edge[i].flow && dep[edge[i].to] < Min)
            {
                Min = dep[edge[i].to];
                cur[u] = i;
            }
        gap[dep[u]]--;
        if(!gap[dep[u]])return ans;
        dep[u] = Min + 1;
        gap[dep[u]]++;
        if(u != start)u = edge[S[--top]^1].to;
    }
    return ans;
}
int T,n,m;
char s[109][109];
char no[109][109];
bool oa[209],ob[209];
int ida[209],idb[209];
int tty[409];
struct qq{
    char a;
    int r,c;
};
vector<qq> aas;
int main(){
//    freopen("D-small-attempt2.in","r",stdin);
//    freopen("D-large.in","r",stdin);
//    freopen("D.out","w",stdout);
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d",&n,&m);
        int ans=0;
        for(int i=1;i<=n;++i){
            for(int j=1;j<=n;++j)s[i][j]='.';
            oa[i]=ob[i]=0;
        }
        for(int i=0;i<m;++i){
            char aa[10];
            int r,c;
            scanf("%s%d%d",aa,&r,&c);
            s[r][c]=aa[0];
            if(aa[0]!='+')oa[r]=ob[c]=1;
            ++ans;
            if(aa[0]=='o')++ans;
        }
        for(int i=1;i<=n;++i)for(int j=1;j<=n;++j)no[i][j]=s[i][j];
        init();
        int S=0,en=1,nono=2;
        for(int i=1;i<=n;++i){
            if(!oa[i]){
                tty[nono]=i;
                addedge(S,nono,1);
                //printf(" %d %d %d\n",S,nono,1);
                ida[i]=nono++;
            }
            if(!ob[i]){
                tty[nono]=i;
                addedge(nono,en,1);
                idb[i]=nono++;
            }
        }
        for(int i=1;i<=n;++i){
            if(!oa[i])
            for(int j=1;j<=n;++j){
                if(!ob[j]){
                    addedge(ida[i],idb[j],1);
                    //printf("%d %d\n",i,j);
                }
            }
        }
        sap(S,en,nono);
        for(int i = head[S]; i != -1; i = edge[i].next){
            //printf("%d %d %d %d\n",0,edge[i].to,edge[i].cap,edge[i].flow);
            if(edge[i].cap==edge[i].flow){
                int uu=edge[i].to,tt;
                for(int j=head[uu];j!=-1;j=edge[j].next)
                if(edge[j].cap==edge[j].flow){tt=edge[j].to;break;}
                uu=tty[uu];
                tt=tty[tt];
                //printf("%d %d %c\n",uu,tt,no[uu][tt]);
                if(no[uu][tt]=='.')no[uu][tt]='x';
                else no[uu][tt]='o';
                ++ans;
            }
        }


        for(int i=2;i<=n+n;++i){
            oa[i]=ob[i]=0;
        }
        for(int i=1;i<=n;++i){
            for(int j=1;j<=n;++j){
                if(s[i][j]!='.'&&s[i][j]!='x'){
                    oa[i+j]=1;
                    ob[i-j+n+1]=1;
                }
            }
        }
        init();
        S=0,en=1,nono=2;
        for(int i=2;i<=n+n;++i){
            if(!oa[i]){
                tty[nono]=i;
                addedge(S,nono,1);
                ida[i]=nono++;
            }
            if(!ob[i]){
                tty[nono]=i;
                addedge(nono,en,1);
                idb[i]=nono++;
            }
        }
        for(int i=1;i<=n;++i){
            for(int j=1;j<=n;++j){
                if(!oa[i+j]&&!ob[i-j+n+1]){
                    addedge(ida[i+j],idb[i-j+n+1],1);
                }
            }
        }
        sap(S,en,nono);
        for(int i = head[0]; i != -1; i = edge[i].next){
            if(edge[i].cap==edge[i].flow){
                int uu=edge[i].to,tt;
                for(int j=head[uu];j!=-1;j=edge[j].next)
                if(edge[j].cap==edge[j].flow){tt=edge[j].to;break;}
                uu=tty[uu];
                tt=tty[tt];
                tt=(uu-tt+n+1)/2;
                uu-=tt;
                if(no[uu][tt]=='.')no[uu][tt]='+';
                else no[uu][tt]='o';
                ++ans;
            }
        }

        aas.clear();
        for(int i=1;i<=n;++i){
            for(int j=1;j<=n;++j){
                if(s[i][j]!=no[i][j]){
                    aas.push_back((qq){no[i][j],i,j});
                }
            }
        }
        printf("Case #%d: ",ca);
        printf("%d %d\n",ans,aas.size());
        for(auto &e:aas){
            printf("%c %d %d\n",e.a,e.r,e.c);
        }
    }
    return 0;
}
