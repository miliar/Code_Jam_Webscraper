#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

typedef long long LL;

using namespace std;

bool visited[101];

LL dist[101][101];

priority_queue<pair<double, int> > heap;

int main() {
  freopen("Cl.out","wt", stdout);
  freopen("Cl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    int N, Q;
    cin >> N >> Q;
    LL E[N], S[N];
    FOR (i, N)
			cin >> E[i] >> S[i];
		FOR (i, N)
			FOR (j, N)
				cin >> dist[i][j];
		FOR (i, N)
			dist[i][i] = 0;
		FOR (k, N)
			FOR (i, N)
				FOR (j, N)
					if (dist[i][k] != -1 && dist[k][j] != -1)
						if (dist[i][j] == -1 || dist[i][k] + dist[k][j] < dist[i][j])
							dist[i][j] = dist[i][k] + dist[k][j];

		int s, e;
		FOR (i, Q) {
			cin >> s >> e;
			s--;
			e--;
			SET(visited, 0);
			while (!heap.empty())
				heap.pop();
			heap.push(make_pair(0.0, s));
			while (!heap.empty()) {
				pair<double, int> el = heap.top();
				heap.pop();
				int v = el.second;
				if (v == e) {
					printf("%.7lf ", -el.first);
					break;
				}
				if (visited[v])
					continue;
				visited[v] = true;
				FOR (i, N) {
					if (visited[i])
						continue;
					LL d = dist[v][i];
					if (d <= E[v] && d != -1) {
						double t = 1.0 * d / (1.0 * S[v]);
						heap.push(make_pair(el.first - t, i));
					}
				}
			}
		}
    cout << "\n";
  }
  return 0;
}
