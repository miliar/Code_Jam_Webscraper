#include <iostream>
#include <string>
#include <string.h>
#include <map>
#include <vector>
using namespace std;
#include <iostream>
#include <limits.h>
#include <string.h>
#include <queue>
using namespace std;
 

double eps = 0.000001;
int graph[1200][1200], rGraph[1200][1200];
bool visited[1200];
int lastID;

bool bfs(int s, int t, int parent[])
{
    memset(visited, 0, sizeof(visited));

    queue <int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;
 

    while (!q.empty()) {
        int u = q.front();
        // cout << u << endl;
        q.pop();
 
        for (int v=0; v<=lastID; v++)
        {
        	// cout << rGraph[u][v] << endl;
            if (visited[v]==false && rGraph[u][v] > 0)
            {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }
    }
    return (visited[t] == true);
}

int fordFulkerson(int s, int t) {
    int u, v;
    for (u = 0; u <= lastID; u++) {
        for (v = 0; v <= lastID; v++) {
             rGraph[u][v] = graph[u][v];
             // cout << u << " " << v << " " << rGraph[u][v] << endl;
        }
    }
 
    int parent[lastID+1];
    memset(parent, 0, sizeof(parent));
 
    int max_flow = 0; 
    while (bfs(s, t, parent)) {
        int path_flow = INT_MAX;
        for (v=t; v!=s; v=parent[v]) {
            u = parent[v];
            path_flow = min(path_flow, rGraph[u][v]);
        }
 
        for (v=t; v != s; v=parent[v]) {
            u = parent[v];
            rGraph[u][v] -= path_flow;
            rGraph[v][u] += path_flow;
        }
 
        max_flow += path_flow;
    }
 
    return max_flow;
}
 



int main () {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti ++) {
		int n, p;
		cin >> n >> p;
		vector<int> r(n);
		for (int i = 0; i < n; i ++) {
			cin >> r[i];
		}
		vector<vector<pair<int, int> > > v(n);
		vector<vector<int> > id(n);
		lastID = 1;
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < p; j ++) {
				double a;
				cin >> a;
				double x1 = a / 1.1 / r[i] - eps;
				double x2 = a / 0.9 / r[i] + eps;
				// if (x1 == x2) continue; // x1
				
				if (x1 <= int(x2) && x2 >= 1) {
					int m1 = x1+1;
					int m2 = int(x2);
					// cout << m1 << "  "<< m2 << endl;
					v[i].push_back(make_pair(m1, m2));
					id[i].push_back(lastID);
					lastID ++;
				}

			}
		}
		memset(graph, 0, 1200*1200*sizeof(int));
		for (int i = 1; i < n ; i ++) {
			for (int j = 0; j < v[i].size(); j ++) {
				for (int k = 0; k < v[i-1].size(); k ++) {
					// cout << v[i][j].first << " " <<v[i-1][k].first << " "<< v[i-1][k].second << " ?" << endl;
					if ((v[i][j].first >= v[i-1][k].first && v[i][j].first <= v[i-1][k].second) ||
					(v[i-1][k].first >= v[i][j].first && v[i-1][k].first <= v[i][j].second)){
						// cout << id[i-1][k] << " " << id[i][j] << endl;
						graph[id[i-1][k]][id[i][j]] = 1;
					}
				}
			}
		}
		for (int k = 0; k < v[0].size(); k ++) {
			graph[0][id[0][k]] = 1;
		}
		for (int k = 0; k < v[n-1].size(); k ++) {
			graph[id[n-1][k]][lastID] = 1;
		}
		int ans = fordFulkerson(0, lastID);
		cout << "Case #" << ti << ": "<< ans << endl;

	}
}