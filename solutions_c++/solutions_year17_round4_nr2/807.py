//#include<stdio.h>
//#include<stdlib.h>
#include<bits/stdc++.h>
//#define Min(a,b,c) min((a),min((b),(c)))
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<LL,LL>
#define pb(x) push_back(x)
#define x first
#define y second
#define sqr(x) ((x)*(x))
#define EPS 1e-11
#define MEM(x) memset(x,0,sizeof(x))
#define MEMS(x) memset(x,-1,sizeof(x))
#define N 100005
#define pi 3.14159265359
using namespace std;
typedef long long LL;
int F[2005][2005];
struct Dinic{
    static const int MXN = 10000;
    struct Edge{ int v,f,re; 
		Edge(int a,int b,int c):v(a),f(b),re(c){
		}
	};
    int n,s,t,level[MXN];
    vector<Edge> E[MXN];
    void init(int _n, int _s, int _t){
        n = _n; s = _s; t = _t;
        for (int i=0; i<n; i++) E[i].clear();
    }
    void add_edge(int u, int v, int f){
        E[u].pb(Edge(v,f,sizeof(E[v])));
        E[v].pb(Edge(u,f,sizeof(E[u])-1));
    }
    bool BFS(){
        MEMS(level);
        queue<int> que;
        que.push(s);
        level[s] = 0;
        while (!que.empty()){
            int u = que.front(); que.pop();
            for (vector<Edge>::iterator  it = E[u].begin();it!=E[u].end();it++){
                if (it->f > 0 && level[it->v] == -1){
                    level[it->v] = level[u]+1;
                    que.push(it->v);
                }
            }
        }
        return level[t] != -1;
    }
    int DFS(int u, int nf){
        if (u == t) return nf;
        int res = 0;
        for (vector<Edge>::iterator  it = E[u].begin();it!=E[u].end();it++){
            if (it->f > 0 && level[it->v] == level[u]+1){
                int tf = DFS(it->v, min(nf,it->f));
                res += tf; nf -= tf; it->f -= tf;
                E[it->v][it->re].f += tf;
                if (nf == 0) return res;
            }
        }
        if (!res) level[u] = -1;
        return res;
    }
    int flow(int res=0){
        while ( BFS() )
        res += DFS(s,2147483647);
        return res;
    }
}flow;
int main() {
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		int n,c,m;
		MEM(F);
		scanf("%d %d %d",&n,&c,&m);
		vector<int> v[1005];
		for(int i=0;i<1005;i++)
		v[i].clear();
		for(int i=0;i<m;i++){
			int a,b;
			scanf("%d %d",&a,&b);
			v[b].pb(a);
		}
		sort(v[1].begin(),v[1].end());
		sort(v[2].begin(),v[2].end());
		if(v[1].size()<v[2].size())
		swap(v[1],v[2]);
		reverse(v[1].begin(),v[1].end());
		int ans=0;
		for(int i=0;i<v[2].size();i++){
			if(v[1][i]==1&&v[2][i]==1)
			ans++;
		}
		if(ans!=0){
			printf("Case #%d: %d 0\n",T,max(v[1].size(),v[2].size())+ans);
			continue;
		}
		for(int i=1;i<=2;i++)
			for(int j=0;j<v[i].size();j++)
			F[v[i][j]][i+1000]++;
		ans=max(v[1].size(),v[2].size());
		for(int i=1;i<=1000;i++)
		F[0][i]=ans;
		for(int i=1;i<=2;i++)
		F[i+1000][2001]=v[i].size();
		flow.init(2002,0,2001);
		for(int i=0;i<2002;i++){
			for(int j=0;j<2002;j++)
			flow.add_edge(i,j,F[i][j]);
		}
		int pp=flow.flow();
		printf("Case #%d: %d %d\n",T,max(v[1].size(),v[2].size()),m-pp);
	}
} 
//1 1 2 6 3 8 4 11 5 17 6 15 7 13 8 25 9 22 10 27
//1
//2 4 6 8 10
//3 6 9
//4 2 6 8 10
//5 5 10
//6 2 3 4 6 8 10
