#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

#define x first
#define y second
#define mkp(a,b) make_pair(a,b)
#define PII pair<int,int>

const int MaxN = 55;

char S[MaxN][MaxN];
int id[MaxN][MaxN], tp[MaxN][MaxN], PX[MaxN * MaxN], PY[MaxN*MaxN];
int N,M,K,V;

const int MaxK = MaxN * MaxN * 2;
vector<int> adj[MaxK], rev[MaxK];
#define DW (0)
#define RT (1)
#define UP (2)
#define LT (3)
const int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}}; // D, R, U, L
// 0: \,   1: /
const int reflect[4][2] = {{RT,LT},{DW,UP},{LT,RT},{UP,DW}};

bool inside(int x,int y){return x>0&&x<=N&&y>0&&y<=M;}

vector<PII > hit[2];
bool is_circle[2];

void add_edge(int x, int v1, int y, int v2) {
//	cout << ">> Edge <"<<x<<","<<v1<<"> -> <"<<y<<","<<v2<<">"<<endl;
	x += v1 * K;
	y += v2 * K;
	adj[x].push_back(y);
	rev[y].push_back(x);
}

int go(int sx,int sy) {
	hit[0].clear();
	hit[1].clear();
	is_circle[0] = is_circle[1] = false;
	bool is_cross = false;
	for(int sd=0;sd<4;++sd) {
		if(is_cross || is_circle[sd & 1]) continue;
		vector<PII >& cur = hit[sd & 1];
		int x=sx+dir[sd][0],y=sy+dir[sd][1], d = sd;
		while(inside(x,y) && tp[x][y] != 3) {
			if(inside(x,y) && tp[x][y] == 2) { // start empty, now shooter
				cur.push_back(mkp(id[x][y], d & 1));
			}
			if(tp[x][y] == 1 || tp[x][y] == 0) 
				d = reflect[d][tp[x][y]];
			x += dir[d][0];
			y += dir[d][1];
			if (x == sx && y == sy) {
				if((d & 1) != (sd & 1)) {
				//	cout << "Cross!! ["<<sx<<", "<<sy<<"]"<<endl;
					is_cross = true;
					return -1;
				} else {
					is_circle[d & 1] = true;
					if(is_circle[0] && is_circle[1]) {
					//	cout<<">>> Two Circles!"<<" ["<<sx<<","<<sy<<"]"<<endl;
						return -1;
					}
				}
				break;
			}
		}
	}
	if (tp[sx][sy] == 2) { // shooter
		int k = id[sx][sy];
		if(is_circle[0] || hit[0].size() > 0) add_edge(k, 0, k, 1);
		if(is_circle[1] || hit[1].size() > 0) add_edge(k, 1, k, 0);
		return 0;
	}
	// empty cell
	vector<PII > choice;
	for(int d=0;d<2;++d) {
		if(!is_circle[d] && hit[d].size() == 1) choice.push_back(hit[d][0]);
		if(is_circle[d] || hit[d].size() > 1) {
			for(int j=0;j<hit[d].size();++j) {
				PII p = hit[d][j];
				add_edge(p.x, p.y, p.x, 1 - p.y);
			}
		}
	}
	if(choice.size() == 0) {
	//	cout << "No Choice! ["<<sx<<","<<sy<<"]"<<endl;
		return -1;
	}
	//cout << "Choice["<<sx<<","<<sy<<"] = "<<choice.size()<<endl;
	if(choice.size() == 1) {
		PII p = choice[0];
		add_edge(p.x, 1 - p.y, p.x, p.y);
	} else {
		PII p=choice[0],q=choice[1];
		add_edge(p.x, 1-p.y, q.x, q.y);
		add_edge(q.x, 1-q.y, p.x, p.y);
	}
	return 0;
}

int vis[MaxK], seq[MaxK], n, order[MaxK], mark[MaxK];

void dfs1(int x) {
	vis[x] = true;
	for(int i=0;i<adj[x].size();++i) {
		if(!vis[adj[x][i]]) {
			dfs1(adj[x][i]);
		}
	}
	seq[n ++] = x;
}

void dfs2(int x, int mk) {
//	cout << "dfs2 >>"<<x<<" mk="<<mk<<endl;
	vis[x] = true;
	mark[x] = mk;
	order[n ++] = x;
	for(int i=0;i<rev[x].size();++i) {
		if(!vis[rev[x][i]]) {
			dfs2(rev[x][i],mk);
		}
	}
}

int run() {
	K = 0;
	memset(id,-1,sizeof(id));
	memset(tp,-1,sizeof(tp));
	scanf("%d %d", &N, &M);
	for(int i=1;i<=N;++i) {
		scanf("%s",S[i]+1);
		for(int j=1;j<=M;++j) {
			if(S[i][j]=='|' or S[i][j]=='-') {
				PX[K]=i;
				PY[K]=j;
				id[i][j] = K++;
				tp[i][j] = 2;
			} else
			if(S[i][j] == '/')
				tp[i][j] = 1;
			else
			if(S[i][j]=='\\')
				tp[i][j]=0;
			else
			if(S[i][j]=='#')
				tp[i][j]=3;
		}
	}
	V=K+K;
	for(int i=0;i<V;++i) {
		adj[i].clear();
		rev[i].clear();
	}
	for(int i=1;i<=N;++i)
		for(int j=1;j<=M;++j) {
			if(S[i][j]=='.') {
				if(go(i,j) < 0) return -1; // hit itself
			} else
			if(tp[i][j] == 2)
				go(i, j);
		}
	memset(vis,0,sizeof(vis));
	n = 0;
	for(int i=0;i<V;++i)
		if(!vis[i])
			dfs1(i);
	/*
	cout << "K = "<<K<<endl;
	for(int i=0;i<n;++i)
		cout << seq[i]<<" ";
	cout<<endl;
*/
	memset(vis,0,sizeof(vis));
	memset(mark,-1,sizeof(mark));
	int iter=0;
	n = 0;
	for(int i=V-1;i>=0;--i) {
		++ iter;
		if(!vis[seq[i]]) {
		//	cout << ">> go"<<endl;
			dfs2(seq[i], iter);
		}
	}
	for(int i=0;i<K;++i) {
		if(mark[i]==mark[i+K] || mark[i]<0||mark[i+K]<0) {
			
		//	cout << ">>> No SAT Sol!"<<endl;
			
			return -1; // impossible
		}
		if(mark[i] > mark[i+K])
			S[PX[i]][PY[i]]='|';
		else
			S[PX[i]][PY[i]]='-';
	}
	return 0;
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int test;scanf("%d",&test);
	for(int no=1;no<=test;++no)
	{
		printf("Case #%d:", no);
		int ret=run();
		if(ret<0) printf(" IMPOSSIBLE\n");
		else {
			 printf(" POSSIBLE\n");
			 for(int i=1;i<=N;++i)
			 	printf("%s\n",S[i]+1);
		}
	}
}

/*

*/
