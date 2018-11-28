#include<stdio.h>
#include<string.h>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
using namespace std;
int S = 18, T = 19;
const   int oo=1e9;  
const int INF = oo;
/**oo 表示无穷大*/  
const  int mm=111111111;  
/**mm 表示边的最大数量，记住要是原图的两倍，在加边的时候都是双向的*/  
const  int mn=999;  
/**mn 表示点的最大数量*/  
int node,src,dest,edge;  
/**node 表示节点数，src 表示源点，dest 表示汇点，edge 统计边数*/  
int ver[mm],flow[mm],next[mm];  
/**ver 边指向的节点，flow 边的容量 ，next 链表的下一条边*/  
int head[mn],work[mn],dis[mn],q[mn];  
void prepare(int _node, int _src,int _dest)  
{  
    node=_node,src=_src,dest=_dest;  
    for(int i=0; i<node; ++i)head[i]=-1;  
    edge=0;  
}  
int ff[20][20];
void get() {
    memset(ff, 0, sizeof(ff));
    for (int i = 0; i < edge; i += 2) {
        ff[ver[i + 1]][ver[i]] = flow[i + 1];
    }
}


/**增加一条 u 到 v 容量为 c 的边*/  
void addE( int u,  int v,  int c)  
{  
    ver[edge]=v,flow[edge]=c,next[edge]=head[u],head[u]=edge++;  
    ver[edge]=u,flow[edge]=0,next[edge]=head[v],head[v]=edge++;  
}  
/**广搜计算出每个点与源点的最短距离，如果不能到达汇点说明算法结束*/  
bool Dinic_bfs()  
{  
    int i,u,v,l,r=0;  
    for(i=0; i<node; ++i)dis[i]=-1;  
    dis[q[r++]=src]=0;  
    for(l=0; l<r; ++l)  
        for(i=head[u=q[l]]; i>=0; i=next[i])  
            if(flow[i]&&dis[v=ver[i]]<0)  
            {  
                /**这条边必须有剩余容量*/  
                dis[q[r++]=v]=dis[u]+1;  
                if(v==dest)  return 1;  
            }  
    return 0;  
}  
/**寻找可行流的增广路算法，按节点的距离来找，加快速度*/  
int Dinic_dfs(  int u, int exp)  
{  
    if(u==dest)  return exp;  
    /**work 是临时链表头，这里用 i 引用它，这样寻找过的边不再寻找*/  
    for(  int &i=work[u],v,tmp; i>=0; i=next[i])  
        if(flow[i]&&dis[v=ver[i]]==dis[u]+1&&(tmp=Dinic_dfs(v,min(exp,flow[i])))>0)  
        {  
            flow[i]-=tmp;  
            flow[i^1]+=tmp;  
            /**正反向边容量改变*/  
            return tmp;  
        }  
    return 0;  
}  

int dinic()  
{  
    int i,ret=0,delta;  
    while(Dinic_bfs())  
    {  
        for(i=0; i<node; ++i)work[i]=head[i];  
        while(delta=Dinic_dfs(src,oo))ret+=delta;  
    }  
    return ret;  
}  
void go(int i, int n) {
    if (n == 0) {
    printf("\n");
    return;    
    }
    if (i == 0) printf("R");
    if (i == 1) printf("O");
    if (i == 2) printf("Y");
    if (i == 3) printf("G");
    if (i == 4) printf("B");
    if (i == 5) printf("V");
    for (int j = 6; j < 12;j++) {
        if (ff[i][j] > 0) {
            ff[i][j] --;
            go(j - 6, n - 1);
            return;
        }
    }
    printf("!!!!!!!\n");
}
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cas = 1; cas <= ca; cas++) {
        int N, R, O, Y, G, B, V;
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        prepare(20, S, T);
        addE(S, 0, R);
        addE(S, 1, O);
        addE(S, 2, Y);
        addE(S, 3, G);
        addE(S, 4, B);
        addE(S, 5, V);
        addE(6, T, R);
        addE(7, T, O);
        addE(8, T, Y);
        addE(9, T, G);
        addE(10, T, B);
        addE(11, T, V);
        addE(0, 8, INF);
        addE(0, 9, INF);
        addE(0, 10, INF);
        addE(1, 10, INF);
        addE(2, 6, INF);
        addE(2, 10, INF);
        addE(2, 11, INF);
        addE(3, 6, INF);
        addE(4, 6, INF);
        addE(4, 7, INF);
        addE(4, 8, INF);
        addE(5, 8, INF);
        printf("Case #%d: ", cas);
        if (dinic() != N) {
            printf("IMPOSSIBLE\n");
        } else {
            get();
            int st = 0;
            for (int i = 0; i < 6; i++) {
                for (int j = 6; j < 12; j++) {
                    if (ff[i][j] > 0) {
                        st = i;
                    }
                }
            }
            go(st, N);
        }
    }
}
