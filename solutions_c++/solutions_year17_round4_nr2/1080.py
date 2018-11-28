#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <climits>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cassert>

#define SHOW(...) {;}
#define REACH_HERE {;}
#define PRINT(s, ...) {;}
#define PRINTLN(s, ...) {;}

#undef HHHDEBUG
#ifdef HHHDEBUG
#include "template.h"
#endif

// for distributed code jam
// #include <message.h>
// #include ".h"

using namespace std;

template<typename T>
using Grid = vector<vector<T>>;

const double E = 1e-8;
const double PI = acos(-1);

struct Network {
    struct Edge {
        int to;
        int pre_edge;
        int cap;
        int flow;
    };

    #define MAXNODE 2002
    int last[MAXNODE];

    int nv; // total number of vertex, index range: [0, nv)
    vector<Edge> edge;
    void init(int _nv) {
        nv = _nv;
        edge.clear();
        fill(last, last + nv, -1);
    }

    void add_e(int x, int y, int cap, int r_cap = 0) {
        Edge e = {y, last[x], cap, 0};
        // Edge e{y, last[x], cap, 0};
        last[x] = edge.size();
        // edge.push_back(move(e));
        edge.push_back(e);
        
        Edge r_e = {x, last[y], r_cap, 0};
        // Edge r_e{x, last[y], r_cap, 0};
        last[y] = edge.size();
        // edge.push_back(move(r_e));
        edge.push_back(r_e);
    }
    void show_edge() {
        for (int i = 0; i < nv; i++) {
            printf("v [%d]:", i);
            for (int ie = last[i]; ie != -1; ) {
                const Edge& e = edge[ie]; 
                ie = e.pre_edge;
                printf(" [%d]%d/%d", e.to, e.flow, e.cap);
            }
            printf("\n");
        }
        printf("\n");
    }

    // 
    // bipartite match
    // O(V * E)
    int peer[MAXNODE];
    bool went[MAXNODE];
    int bipartite_match() {
        fill(peer, peer + nv, -1);
        int ans = 0;
        for (int i = 0; i < nv; i++) {
            if (last[i] == -1 || peer[i] != -1)
                continue;
            fill(went, went + nv, false);
            if (match(i))
                ans++;
        }
        return ans;
    }
    bool match(int cur) {
        for (int ie = last[cur]; ie != -1; ) {
            const Edge& e = edge[ie];
            ie = e.pre_edge;
            int to = e.to;
            if (went[to])
                continue;
            went[to] = true;
            if (peer[to] == -1 || match(peer[to])) {
                peer[to] = cur;
                peer[cur] = to;
                return true;
            }
        }
        return false;
    }
    void show_peer() {
        for (int i = 0; i < nv; i++)
            printf("%d peer-> %d\n", i, peer[i]);
    }
    // end of 
    // bipartite match
    // 
};


int main() {
    ios::sync_with_stdio(false);

    int nt;
    cin >> nt;
    for (int it = 1; it <= nt; it++) {
    	int n, c, m;
    	cin >> n >> c >> m;
    	vector<vector<int>> t(c);
    	vector<int> n_one(c);
    	vector<int> not_one(c);
    	for (int i = 0; i < m; i++) {
    		int p, b;
    		cin >> p >> b;
    		b--;
    		t[b].push_back(p);
    		if (p == 1)
    			n_one[b]++;
    		else
    			not_one[b]++;
    	}
    	if (t[0].size() == 0 || t[1].size() == 0) {
    		printf("Case #%d: %d %d\n", it, m, 0);
    		continue;
    	}

    	int mm = max((int)t[0].size(), (int)t[1].size());
    	t[0].resize(mm);
    	t[1].resize(mm);

    	SHOW(n, c, m)
    	for (int i = 0; i < c; i++) {
    		SHOW(i, n_one[i], not_one[i])
    	}

    	Network g;
    	g.init(2000);
    	for (int i = 0; i < t[0].size(); i++) {
    		int t0 = t[0][i];
    		if (t0 == 1)
    			continue;
    		for (int j = 0; j < t[1].size(); j++) {
    			int t1 = t[1][j];
    			if (t1 == 1)
    				continue;
    			if (t0 == t1)
    				continue;
    			g.add_e(i, j + 1000, 0, 0);
    		}
    	}
    	// g.show_edge();
    	int diff = g.bipartite_match();
    	// g.show_peer();
    	int ans = max(n_one[0] + n_one[1], max((int)t[0].size(), (int)t[1].size()));
    	// int xx = not_one[0] - n_one[1];
    	// int yy = not_one[1] - n_one[0];
    	// int need = max(0, max(xx, yy));
    	int need = ans - (n_one[0] + n_one[1]);
    	need = max(0, need);
    	// SHOW(xx, yy, need, diff)
    	int promote = max(0, need - diff);
    	// SHOW(diff, ans, need, promote)
    	printf("Case #%d: %d %d\n", it, ans, promote);
    }
}

