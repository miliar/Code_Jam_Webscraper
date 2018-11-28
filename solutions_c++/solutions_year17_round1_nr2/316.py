#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cstring>
#include <unordered_map>

using namespace std;
typedef long long LL;

#define MAXN 3000

struct Edge {
	int from, to, cap, flow, index;
	Edge(int from, int to, int cap, int flow, int index):
	from(from), to(to), cap(cap), flow(flow), index(index){}
};
struct Dinic {
	vector<vector<Edge> > G;
	vector<Edge *> dad;
	vector<int> Q;
	void init() {
		G.resize(MAXN);
		dad.resize(MAXN);
		Q.resize(MAXN);
	}
	void addEdge(int from, int to, int cap) {
		//cout<<"edge: "<<from<<" "<<to<<endl;
		G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
		if (from==to) G[from].back().index++;
		G[to].push_back(Edge(to, from, 0, 0, G[from].size()-1));
	}
	LL calc(int s, int t) {
		LL ret=0;
		while (1) {
			fill(dad.begin(), dad.end(), (Edge*)NULL);
			dad[s]=&G[0][0]-1;
			int head=0, tail=0;
			Q[tail++]=s;
			while (head<tail) {
				int x=Q[head++];
				for (int i=0;i<(int)G[x].size();i++) {
					Edge &e=G[x][i];
					if (!dad[e.to] && e.cap-e.flow>0) {
						dad[e.to]=&G[x][i];
						Q[tail++]=e.to;
					}
				}
			}
			if (!dad[t]) break;
			LL tot=0;
			for (int i=0;i<(int)G[t].size();i++) {
				Edge *start=&G[G[t][i].to][G[t][i].index];
				int amt=1000000000;
				for (Edge *e=start;amt && e!=dad[s];e=dad[e->from])
					if (!e) {amt=0;break;}
					else amt=min(amt, e->cap-e->flow);
				if (amt==0) continue;
				for (Edge *e=start;amt && e!=dad[s];e=dad[e->from]) {
					e->flow+=amt;
					G[e->to][e->index].flow-=amt;
				}
				tot+=amt;
			}
			if (tot==0) break;
			ret+=tot;
		}
		return ret;
	}
};

int a[55];
int v[55][55];
int n, p;
int in[55][55];
int out[55][55];

pair<int, int> check(int a, int b) {
	pair<int, int> ret;
	ret.first=-1;
	ret.second=-1;
	int x=a*100/110/b;
	int y=a*100/90/b;
	while (x<=y) {
		if (b*x*90<=a*100 && a*100<=b*x*110) {
			ret.first=x;
			break;
		}
		x++;
	}
	while (y>=x) {
		if (b*y*90<=a*100 && a*100<=b*y*110) {
			ret.second=y;
			break;
		}
		y--;
	}
	return ret;
}

int main() {
	freopen("ratatouille.in","r",stdin);
	freopen("ratatouille.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		cin>>n>>p;
		for (int i=0;i<n;i++) cin>>a[i];
		for (int i=0;i<n;i++)
			for (int j=0;j<p;j++) cin>>v[j][i];
		Dinic dinic;
		dinic.init();
		int source=n*p*2, sink=source+1;
		for (int i=0;i<p;i++)
			for (int j=0;j<n;j++) {
				in[i][j]=i*n+j;
				out[i][j]=i*n+j+n*p;
				dinic.addEdge(in[i][j], out[i][j], 1);
				if (j==0 && check(v[i][j], a[j]).first!=-1) {
					dinic.addEdge(source, in[i][j], 1);
				}
				if (j==n-1 && check(v[i][j], a[j]).first!=-1) {
					dinic.addEdge(out[i][j], sink, 1);
				}
			}
		for (int i=0;i<n-1;i++)
			for (int j=0;j<p;j++)
				for (int k=0;k<p;k++) {
					//int x=check(v[j][i], a[i]), y=check(v[k][i+1], a[i+1]);
					//cout<<v[j][i]<<" "<<a[i]<<"     "<<v[k][i+1]<<" "<<a[i+1]<<endl;
					pair<int, int> x=check(v[j][i], a[i]), y=check(v[k][i+1], a[i+1]);
					if (x.first!=-1 && y.first!=-1 && ((x.first>=y.first && x.first<=y.second) || (y.first>=x.first && y.first<=x.second))) {
						//cout<<"asdf "<<j<<" "<<i<<" -> "<<k<<" "<<i+1<<endl;
						dinic.addEdge(out[j][i], in[k][i+1], 1);
					}
				}
		cout<<"Case #"<<nt++<<": "<<dinic.calc(source, sink)<<endl;
	}
}
