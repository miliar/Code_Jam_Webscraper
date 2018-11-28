#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>
#define _ << " _ " <<
#define dbg(x) //cerr << #x << " == " << x << endl
#define mp(x,y) make_pair((x),(y))
#define pv(x,y) {for(typeof(y) z=(x);z!=(y);z++)cerr<<*z<<" ";cerr<<endl;}
#define rep(x,y) for(int(x)=(0);(x)<int(y);++(x))
#define x first
#define y second
using namespace std;

typedef long long ll;
typedef pair<int,int> pt;

#if 0
#define GENERATE 1
#endif

int N, C, M;
pair<int,int> P[1111];

void read() {
	cin>>N>>C>>M;
	rep(i,M) cin>> P[i].x >> P[i].y;
}

////////////
const int maxe = 300000*2 + 10;
const int maxv = 5000 + 10;
int to[maxe], cap[maxe], ant[maxe], adj[maxv], m, n;

void add(int u, int v, int uv, int vu = 0) {

	dbg(u _ v _ uv);

	to[m] = v, cap[m] = uv, ant[m] = adj[u], adj[u] = m++;
	to[m] = u, cap[m] = vu, ant[m] = adj[v], adj[v] = m++;
	n = max(n, max(u,v)+1);
}

int level[maxv], fila[maxv], copy_adj[maxv];

int bfs(int source, int sink) {
	memset(level,-1,sizeof level);
	level[source] = 0;
	int pos = 0, tam = 0;
	fila[tam++] = source;
	while(pos < tam) {
		//dbg("???");
		int now = fila[pos++];
		for(int i = adj[now]; i >= 0; i = ant[i]) if(cap[i] && level[to[i]] == -1) {
			level[to[i]] = level[now] + 1;
			fila[tam++] = to[i];
		}
	}
	return level[sink] != -1;
}

int dfs(int no, int sink, int flow) {
	if(no == sink) return flow;
	for(int &i = copy_adj[no]; i >= 0; i = ant[i]) if(cap[i] && level[no] + 1 == level[to[i]]) {
		int nflow = dfs(to[i],sink,min(flow,cap[i]));
		if(nflow) {
			cap[i] -= nflow, cap[i^1] += nflow;
			return nflow;
		}
	}
	return 0;
}

long long maxflow(int source, int sink) {
	long long mf = 0;
	while(true) {
		//dbg("...");
		if(bfs(source,sink)) {
			memcpy(copy_adj,adj,sizeof adj);
			while(true) {
				//dbg("oooo");
				int add = dfs(source,sink,1<<30);
				if(add) mf += add; else break;
			}
		} else break;
	}
	return mf;
}

void init() {
	memset(adj,-1,sizeof adj), n = m = 0;
}
////////////

int fb(int d) {
	init();
	int source = 0, sink = N + C + C + 1;
	rep(i,M) {
		int id = P[i].y;
		int plc = P[i].x;
		add(id, C + id, 1);
		add(C + id, C + C + plc, 1);
	}
	rep(i,C) add(source, i + 1, d);
	rep(i,N) add(C + C + i + 1, sink, d);
	rep(i,N-1) add(C + C + i + 2, C + C + i + 1,1e9);

	long long mf = maxflow(source, sink);

	dbg(d _ mf);

	//exit(0);

	return mf >= M;
}

int func() {

	dbg( fb(1) );
	dbg( fb(2) );

	int ans = M, take = M;
	while (take > 0) {
		int nans = ans - take;
		if(nans > 0 && fb(nans)) ans = nans;
		else take /= 2;
	}
	return ans;

	// init();
	// int source = 0, sink = N + C + C + 1;
	// rep(i,M) {
	// 	add(C + N + P[i].y, N + P[i].y, 1);
	// 	add(N + P[i].y, P[i].x, 1);
	// }
	// rep(i,N-1) add(i + 2, i + 1,1e9);
	// long long tf=0;
	// for(int d=1;d<=1111111;d++) {
	// 	dbg(d);
	// 	dbg(tf _ M);
	// 	rep(i,C) add(source, C + i + 1, 1);
	// 	rep(i,N) add(i + 1, sink, 1);
	// 	tf += maxflow(source, sink);
	// 	if(tf >= M) return d;
	// }
}

int fb2(int days, int lim) {
	init();
	int source = 0, sink = N + C + 1;
	rep(i,M) {
		int id = P[i].y;
		int plc = P[i].x;

		add(source, id, 1);
		add(id, C + plc, 1);
	}
	rep(i,N) add(C + i + 1, sink, days);
	rep(i,N-1) add(C + i + 2, C + i + 1, lim);

	return maxflow(source, sink) >= M;
}

int func(int days) {
	int ans = M, take = M;
	while (take > 0) {
		int nans = ans - take;
		if(nans >= 0 && fb2(days,nans)) ans = nans;
		else take /= 2;
	}
	return ans;
	// init();
	// int source = 0, sink = N + C + 1;
	// rep(i,M) {
	// 	add(source, N + P[i].y, 1);
	// 	add(N + P[i].y, P[i].x, 1);
	// }
	// rep(i,N) add(i + 1, sink, days);
	// long long tf=0;
	// for(int lim=0;lim<=111111;lim++) {
	// 	dbg(lim);
	// 	tf += maxflow(source, sink);
	// 	if(tf >= M) return lim;
	// 	rep(i,N-1) add(i + 2, i + 1, 100);
	// }
	// return -1;
}

void process() {
	int y = func(); dbg(y);
	int z = func(y); dbg(z);
	//int z=0;
	printf("%d %d\n", y, z);
}

int main() {
	int T;
#ifdef GENERATE
	unsigned int seed=time(0);
	dbg(seed);
	srand(seed);
	T=50;
	for(int testcase=1;testcase<=T;++testcase) {
		fprintf(stderr,"Case #%d: ",testcase);
		// *generate input!
		// BEGIN
		// END
#else
		cin>>T;
		for(int testcase=1;testcase<=T;++testcase) {
			dbg(testcase);
			fprintf(stdout,"Case #%d: ",testcase);
			read();
#endif
		try {
			process();
		} catch(char const*exception) {
			puts(exception);
		}
	}
	return 0;
}
