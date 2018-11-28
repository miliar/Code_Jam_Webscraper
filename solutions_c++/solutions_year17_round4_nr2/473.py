#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;

struct Te {
    int y;
    int flow;
    int cost;
    int revIndex;
};
vector< vector<Te> > g;
int S, T;
int N, C, M;

void add(int x, int y, int fl, int cost) {
    g[x].push_back({y, fl, cost, (int)g[y].size()});
    g[y].push_back({x, 0, -cost, (int)g[x].size() - 1});
}

bool flow(vector< vector<Te> > g, int& mincost) {
    mincost = 0;
    
    for (int iter = 0; iter < M; ++iter) {
        vector<int> d(g.size(), 1e9 + 1);
    	d[S] = 0;
	    vector<int> id(g.size());
    	deque<int> q;
	    q.push_back(S);
        vector<int> px(g.size(), -1);
        vector<int> pi(g.size(), -1);

    	while (!q.empty()) {
	    	int v = q.front();
            q.pop_front();
    		id[v] = 1;
	    	for (size_t i = 0; i < g[v].size(); ++i) {
                if (g[v][i].flow <= 0) {
                    continue;
                }
		    	int to = g[v][i].y;
                int len = g[v][i].cost;
    			if (d[to] > d[v] + len)	{
	    			d[to] = d[v] + len;
		    		if (id[to] == 0) {
			    		q.push_back(to);
                    } else 
                    if (id[to] == 1) {
		    			q.push_front(to);
                    }
    			    px[to] = v;
                    pi[to] = i;
	    			id[to] = 1;
		    	}
    		}
	    }
        if (d[T] > 1e9) {
            return false;
        }

        int x = T;
        while (x != S) {
            int y = px[x];
            int yi = pi[x];
            --g[y][yi].flow;
            ++g[x][g[y][yi].revIndex].flow;
//            cerr << x << " , ";
            x = y;
        }
//        cerr << endl;

        mincost += d[T];
    }

    return true;
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(false);

    int Te;
    cin >> Te;
    for (int __ =1; __ <= Te; ++__) {
        cin >> N >> C >> M;

        vector<int> w(C + 1);
        S = 0;
        T = M + N + N + 1;
        g.clear();
        g.resize(T + 1); 
        for (int i = 0; i < M; ++i) {
            int p, b;
            cin >> p >> b;
            add(S, i + 1, 1, 0);
            add(i + 1, M + p, 1, 0);
            add(i + 1, M + N + p, 1, 1);
            w[b]++;
        }
        for (int i = 2; i <= N; ++i) {
            add(M + N + i, M + N + i - 1, 100500, 0);
        }
        for (int i = 1; i <= N; ++i) {
            add(M + N + i, M + i, 100500, 0);
        }
        for (int i = 1; i <= N; ++i) {
           add(M + i, T, 0, 0);
        }

        int left = 0;
        for (int i = 1; i <= C; ++i) {
            left = max(left, w[i]);
        }

        int right = M;
        int mincost = 0;
        while (left < right) {
            int center = (left + right) / 2;
        
            for (int i = 1; i <= N; ++i) {
                g[M + i].back().flow = center;
            }

//            cerr << endl << endl << endl;
            if (flow(g, mincost)) {
                right = center;
            } else {
                left = center + 1;
            }
        }
        
        for (int i = 1; i <= N; ++i) {
            g[M + i].back().flow = left;
        }
        flow(g, mincost);

        cout << "Case #" << __ << ": " << left << ' ' << mincost << endl;
        cerr << __ << endl;
    }

    return 0;
}
