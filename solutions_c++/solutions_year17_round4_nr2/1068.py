#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
#define MAXN 20005
#define MAXE 6000000
#define inf  0x3f3f3f3f
struct Edge{  int v,c,x; }E[MAXE]; //指向的节点, 剩余可增广的流量
int l[MAXN],e;                     //必须保证e的初始值是偶数
void init(){ e=0; memset(l,-1,sizeof(l));  }
inline void insert(int u,int v,int f,int invf){ //u->v=f   v->u=invf
	E[e].v=v; E[e].c=f;   E[e].x=l[u]; l[u]=e++;
	E[e].v=u; E[e].c=invf;E[e].x=l[v]; l[v]=e++;
}
struct Netflow{
	int src,sink; //需要初始化
	//以上
	int L[MAXN],Q[MAXN]; //L=level  Q=queue
	int _bfs(){ //广搜,并标记level(只取流量大于0的边)
		int s=0,t=0,u;
		memset(L,0xff,sizeof(L));
		L[src]=0; Q[t++]=src;
		while (s<t){
			u=Q[s++];
			for (int p=l[u];p>=0;p=E[p].x)
				if (E[p].c && L[E[p].v]==-1)
					L[(Q[t++]=E[p].v)]=L[u]+1;
		}
		return L[sink]!=-1;
	}
	int _find(int u,int in){ //in:能流入u节点的最大流量. 返回u节点能流出的最大流量
		if (u==sink) return in;
		int t,w=0; //w表示已经从u流出的总流量
		for (int p=l[u];p>=0 && w<in;p=E[p].x){
			if (E[p].c>0 && L[E[p].v]==L[u]+1){
				if (t=_find(E[p].v,min(E[p].c,in-w))){
					E[  p].c-=t;
					E[p^1].c+=t; //这里表示必须
					w+=t;     //多路增广优势巨大
				}
			}
		}
		if( w<in )L[u]=-1;//关键的一句话
		return w;
	}
	int dinic(){
		int t,res=0;
		while (_bfs())while (t=_find(src,inf))res+=t;
		return res;
	}
}flow;

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        int n, m, c;
        scanf("%d%d%d", &n, &c, &m);
        vector< vector<int> > f(c + 1, vector<int>(0, 0));
        vector< pair<int, int> > g(m, pair<int, int>(0, 0));
        for (int i = 0; i < m; i++) {
            int p, b;
            scanf("%d%d", &p, &b);
            f[b].push_back(p);
            g[i].first = p;
            g[i].second = b;
        }
        int ans1 = 0, ans2 = m;
        int u1 = 0, u2 = 0, v1 = 0, v2 = 0;;
        for (int i = 0; i < f[1].size(); i++) {
            if (f[1][i] == 1) {
                u1++;
            } else {
                u2++;
            }
        }
        for (int i = 0; i < f[2].size(); i++) {
            if (f[2][i] == 1) {
                v1++;
            } else {
                v2++;
            }
        }

        if (u1 > v2) {
            ans1 += u1;
            ans2 = 0;
            if (u2 > v1) {
                ans1 += u2;
            } else {
                ans1 += v1;
            }
        } else {
            if (u2 > v1) {
                ans1 = u1 + v1 + max(u2 - v1, v2 - u1);
                ans2 = 0;
                map<int, int> temp;
                int x = u1, y = v1, z = max(u2 - v1, v2 - u1);
                for (int i = 0; i < f[1].size(); i++) {
                    temp[f[1][i]]++;
                }
                for (int i = 0; i < f[2].size(); i++)
                if (f[2][i] != 1) {
                    temp[f[1][i]]++;
                }
            } else {
                ans1 = v1 + v2;
                ans2 = 0;
            }
        }
        init();
        flow.src = 1; flow.sink = 2 + n + n;
        for (int i = 0; i < f[1].size(); i++) {
            insert(1, f[1][i] + 1, 1, 0);
        }
        for (int i = 0; i < f[2].size(); i++) {
            insert(1 + n + f[2][i], 1 + n + n + 1, 1, 0);
        }
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
        if (i != j) {
            insert(1 + i, 1 + n + j, 100000, 0);
        }
        int temp = flow.dinic();
        ans2 = m - temp * 2 - (ans1 - temp);

        /* big
        sort(g.begin(), g.end(), cmp1);
        vector<int> num;
        vector< set<int> > set_g, set_k;
        for (int i = 0; i < m; i++) {
            bool check = false;
            for (int j = 0; j < ans1; j++) {
                if (set_g[j].find(g[i].second) == set_g[j].end() && num[j] < g[i].first) {
                    set_g[j].insert(g[i].second);
                    check = true;
                    num[j]++;
                    break;
                }
            }
            if (!check) {
                ans1++;
                num.push_back(1);
                set<int> temp;
                temp.insert(g[i].second);
                set_g.push_back(temp);
            }
        }

        for (int j = 0; j < ans1; j++) {
            set_g[j].clear();
            set<int> temp;
            set_k.push_back(temp);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < ans1; j++) {
                if (set_g[j].find(g[i].second) == set_g[j].end() &&
                    set_k[j].find(g[i].first) == set_k[j].end()) {
                    set_g[j].insert(g[i].second);
                    set_k[j].insert(g[i].first);
                    ans2--;
                    break;
                }
            }
        }*/

        printf("Case #%d: %d %d\n", t, ans1, ans2);
    }
    return 0;
}
