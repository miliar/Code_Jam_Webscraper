#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double ld;

// Ford Fulkerson mit Capacity Scaling. Laufzeit: O(|E|^2*log(C))
static const int MAX_N = 5000; // #Knoten, egal für die Laufzeit.
struct edge { int dest, rev; ll cap, flow; };
vector<edge> adjlist[MAX_N];
int visited[MAX_N], target, dfsCounter;
ll capacity;

bool dfs(int x) {
  if (x == target) return 1;
  if (visited[x] == dfsCounter) return 0;
  visited[x] = dfsCounter;
  for(int i = 0; i < adjlist[x].size(); i++) {
    edge& e = adjlist[x][i];
    if (e.cap >= capacity && dfs(e.dest)) {
      e.cap -= capacity; adjlist[e.dest][e.rev].cap += capacity;
      e.flow += capacity; adjlist[e.dest][e.rev].flow -= capacity;
      return 1;
  }}
  return 0;
}

void addEdge(int u, int v, ll c) {
  adjlist[u].push_back(edge {v, (int)adjlist[v].size(), c, 0});
  adjlist[v].push_back(edge {u, (int)adjlist[u].size() - 1, 0, 0});
}

ll maxFlow(int s, int t) {
  capacity = 1LL << 62;
  target = t;
  ll flow = 0L;
  while (capacity) {
    while (dfsCounter++, dfs(s)) flow += capacity;
    capacity /= 2;
  }
  return flow;
}

set<ll> getServs(int s, int p) {
	
	set<ll> ins;

	//printf("processing %d %d \n", s, p);

	ll start = p / s;

	//printf("%d\n", start*s);

	int lower = ceil(start*s*0.9);
	int upper = floor(start*s*1.1);

	if(start != 0 && p >= lower && p <= upper) {
		//printf("insert s %lld\n", start);
		ins.insert(start);
	}

	for(int i = start-1; i >= 0; i--) {
		lower = ceil(i*s*0.9);
		upper = floor(i*s*1.1);

		if(p < lower || p > upper) break;
		//printf("insert %d\n", i);
		ins.insert(i);
	}

	for(int i = start+1; ; i++) {
		lower = ceil(i*s*0.9);
		upper = floor(i*s*1.1);

		if(p < lower || p > upper) break;
		//printf("insert %d\n", i);
		ins.insert(i);
	}

	return ins;
}

ll checkInters(set<ll>& s1, set<ll>& s2) {

	for(set<ll>::iterator it = s1.begin(); it != s1.end(); it++) {
		if(s2.find(*it) != s2.end()) return 1;
	}

	return 0;
}

ll ins;
ll outs;
ll s;
ll t;
ll INF = 1000000000000LL;
ll N, P;

ll getIn(ll i, ll j) {
	return i*P+j;
}

ll getOut(ll i, ll j) {
	return outs+i*P+j;
}



void reset() {
	
	for(int i = 0; i < MAX_N; i++) adjlist[i] = vector<edge>();

	memset(visited, 0, sizeof visited);
	target = 0;
	dfsCounter = 0;
	capacity = 0;

}


void run() {
	ll T;
	cin >> T;

	//printf("%d\n", T);
	for(int tc = 0; tc < T; tc++) {
		cin >> N >> P;

		reset();

		vector< vector <ll> > pl(N, vector<ll>(P));
		vector<ll> sl(N);

		for(int i = 0; i < N; i++) cin >> sl[i];

		for(int i = 0; i < N; i++) {
			for(int j = 0; j < P; j++) cin >> pl[i][j];
		}

		vector< vector< set<ll> > > servs(N, vector< set<ll> >(P));

		
		vector<ll> markD(P, 0);

		for(int i = 0; i < N; i++) {
			for(int j = 0; j < P; j++) {
				servs[i][j] = getServs(sl[i], pl[i][j]);
				if(i == 0 && servs[i][j].size() == 0) markD[j] = 1;
			}		
		}

		ins = 0;
		outs = ins+N*P;
		s = outs+N*P;
		t = s+1;
	
		for(int j = 0; j < P; j++) {
			if(!markD[j]) addEdge(s, getIn(0, j), INF);
			addEdge(getOut(N-1, j), t, INF);
		}

		for(int i = 0; i < N; i++) {
			for(int j = 0; j <P; j++) {
				addEdge(getIn(i, j), getOut(i, j), 1);
			}
		}

		for(int i = 1; i < N; i++) {
			for(int p1 = 0; p1 <P; p1++) {
				for(int p2 = 0; p2 < P; p2++) {
					if(checkInters(servs[i-1][p1], servs[i][p2])) {
						addEdge(getOut(i-1, p1), getIn(i, p2), INF);
					}
				}
			}
		}

		ll mf = maxFlow(s, t);
		printf("Case #%d: %lld\n", tc+1, mf);
	}
}

int main() {
	run();
}
