#include <bits/stdc++.h>
#define loop(i,n) for(int i = 0;i < (n);i++)
#define range(i,a,b) for(int i = (a);i <= (b);i++)
#define all(A) A.begin(),A.end()
#define pb push_back
#define mp make_pair
#define sz(A) ((int)A.size())
#define vi vector<int>
#define vl vector<long long>
#define vd vector<double>
#define vp vector<pair<int,int> >
#define ll long long
#define pi pair<int,int>
#define popcnt(x) __builtin_popcount(x)
#define LSOne(x) ((x) & (-(x)))
#define xx first
#define yy second
#define PQ priority_queue
#define print(A,t) cerr << #A << ": "; copy(all(A),ostream_iterator<t>(cerr," " )); cerr << endl
#define prp(p) cerr << "(" << (p).first << " ," << (p).second << ")";
#define prArr(A,n,t)  cerr << #A << ": "; copy(A,A + n,ostream_iterator<t>(cerr," " )); cerr << endl
#define PRESTDIO() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define what_is(x) cerr << #x << " is " << x << endl
#define bit_lg(x) (assert(x > 0),__builtin_ffsll(x) - 1)
const double PI = acos(-1);
using namespace std;

const int maxnode = 30000 + 5;
const int maxedge = 2100000 + 5;
const int oo = 1000000000;
int node, src, dest, nedge;
int head[maxnode], point[maxedge], nxt[maxedge], flow[maxedge],
capa[maxedge];
int dist[maxnode], Q[maxnode], work[maxnode];

void init(int _node, int _src, int _dest) {
	node = _node;
	src = _src;
	dest = _dest;
	for (int i = 0; i < node; i++)
		head[i] = -1;
	nedge = 0;
}
void addedge(int u, int v, int c1, int c2) {
	point[nedge] = v, capa[nedge] = c1, flow[nedge] = 0,
	nxt[nedge] = head[u], head[u] =(nedge++);
	point[nedge] = u, capa[nedge] = c2, flow[nedge] = 0,
	nxt[nedge] = head[v], head[v] =(nedge++);
}
bool dinic_bfs() {
	memset(dist, 255, sizeof(dist));
	dist[src] = 0;
	int sizeQ = 0;
	Q[sizeQ++] = src;
	for (int cl = 0; cl < sizeQ; cl++)
		for (int k = Q[cl], i = head[k]; i >= 0; i = nxt[i])
			if (flow[i] < capa[i] && dist[point[i]] < 0) {
				dist[point[i]] = dist[k] + 1;
				Q[sizeQ++] = point[i];
			}
	return dist[dest] >= 0;
}
int dinic_dfs(int x, int exp) {
	if (x == dest)
		return exp;
	for (int &i = work[x]; i >= 0; i = nxt[i]) {
		int v = point[i], tmp;
		if (flow[i] < capa[i] && dist[v] == dist[x] + 1 && (tmp = dinic_dfs(v, min(exp, capa[i] - flow[i]))) > 0) {
			flow[i] += tmp;
			flow[i ^ 1] -= tmp;
			return tmp;
		}
	}
	return 0;
}
int dinic_flow() {
	int result = 0;
	while (dinic_bfs()) {
		for (int i = 0; i < node; i++)
			work[i] = head[i];
		while (1) {
			int delta = dinic_dfs(src, oo);
			if (delta == 0)
				break;
			result += delta;
		}
	}
	return result;
}

const int MAX = 1 << 10;
int n;
int N,P;
int R[MAX],I[MAX][MAX];
vector<pi> intr[MAX];
vi name[MAX];

int main(){
	freopen("logger.out","w",stderr);
	#ifndef ONLINE_JUDGE
	//	freopen("B-small-attempt1.in", "r", stdin);
	//	freopen("output1.out", "w", stdout);
	#endif
	int T; scanf("%d",&T);
	for(int t = 1;t <= T;t++){
		scanf("%d %d",&N,&P);
		loop(i,N) scanf("%d",R + i);
		int ans = 0;
		loop(i,N) {
			loop(j,P ){
				scanf("%d",&I[i][j]);
				int s = 0,e = 1 << 20;
				while(s < e){
					int m = (s + e) >> 1;
					if(10*I[i][j] <= 11LL*m*1LL*R[i]) e = m;
					else s = m + 1;
				}
				int st = s;
				s = 0,e = 1 << 20;
				while(s < e){
					int m = (s + e) >> 1;
					if(10*I[i][j] < 9LL*m*1LL*R[i]) e = m;
					else s = m + 1;
				}
				int en = s - 1;
				if(st <= en) intr[i].pb(mp(st,en));
//				else cerr << I[i][j] << " " << R[i] << " " << st << " " << en << endl;*/
				/*int st = 0,en = 0;
				for(;st*11LL*R[i] < 10*I[i][j];st++);
				en = st;
				for(;(en + 1)*9LL*R[i] <= 10*I[i][j];en++);
				intr[i].pb(mp(st,en));*/
			}
//			for(auto p : intr[i]) prp(p);
//			cerr << endl;
		}
		int n = 0,cond = 1;
		loop(i,N) {
			n += intr[i].size();
			if(intr[i].empty()) cond = 0;
			sort(all(intr[i]));
		}
		if(!cond) ans = 0;
		else{
			int src = 0,snk = 2*n + 1;
			init(2*n + 2,src,snk);
			n = 0;
			loop(i,N) for(auto p : intr[i]) name[i].pb(++n);
			for(int x : name[0]) addedge(0,x,1,0);
			for(int x : name[N - 1]) addedge(x + n,snk,1,0);
			loop(i,N) for(int x : name[i]) addedge(x,x + n,1,0);
			loop(i,N - 1){
				loop(j,sz(intr[i])){
					loop(k,sz(intr[i + 1])){
//						if(intr[i + 1][k].xx > intr[i][j].yy) break;
//						if(intr[i][j].yy < intr[i + 1][k].xx) continue;
						pi A = intr[i][j],B = intr[i + 1][k];
						if(A.xx > B.xx) swap(A,B);
						if(B.xx <= A.yy)
							addedge(name[i][j] + n,name[i + 1][k],1,0);
					}
				}
			}
			ans = dinic_flow();
		}
		printf("Case #%d: %d\n",t,ans);
		loop(i,N) intr[i].clear(),name[i].clear();
	}
	return 0;
}
