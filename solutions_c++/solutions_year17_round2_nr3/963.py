#include <bits/stdc++.h>
/*
TASK: hidden
LANG: C++11
*/
using namespace std;
typedef long long ll;
typedef pair<double, int> pair2;
typedef pair<int, pair<int, int> > pair3;
typedef pair<int, pair<int, pair<int, int> > > pair4;
#define MAXN 200
#define MAXK 10
#define INFINITY 1000000000000000.0
#define mp make_pair
#define add push_back
#define remove pop

int n, q;
double maxDistance[MAXN], speed[MAXN];
double dist[MAXN][MAXN];
double shortestTime[MAXN];
bool seen[MAXN];
double dp[MAXN];

void dijkstra(int start) {
	for (int j = 0; j < MAXN; j++) {
		shortestTime[j] = INFINITY;
		seen[j] = false;
	}

	shortestTime[start] = 0;

	priority_queue<pair2> pq;

	pq.push(mp(0, start));

	while (!pq.empty()) {
		pair2 next = pq.top();
		pq.pop();

		int current = next.second;
		double time = -next.first;

		if (seen[current]) continue;
		seen[current] = true;

		//cout << "we are at currently " << current << endl;
		for (int i = 0; i < n; i++) {
			if (seen[i]) continue;
			if (dist[current][i] <= maxDistance[current]) { //if distance from current to i is less than our range
				if (shortestTime[i] > time + dist[current][i] / speed[current]) {
					//cout << "Updating " << i << " from " << current << " to be " << time + dist[current][i] / speed[current] << endl;
					shortestTime[i] = time + dist[current][i] / speed[current];

					pq.push(mp(-shortestTime[i], i));
				}
			}
		}
	}
}

int main() {
	//freopen("cbs.in", "r", stdin);
	//freopen("cbs.out", "w", stdout);
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);

	//cout << "wtf" << endl;
	int T;
	cin >> T;
	//cout << "we read first one" << endl;

	for (int asdf = 0; asdf < T; asdf++) {
		cin >> n >> q;

		for (int i = 0; i < n; i++) {
			cin >> maxDistance[i];
			cin >> speed[i];
		}

		//distanceFromStart[0] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int a;
				cin >> a;

				dist[i][j] = a;
				if (dist[i][j] == -1) {
					dist[i][j] = INFINITY;
				}
			}
		}

		//do Floyd warshall
		for (int k = 0; k < n; k++) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (dist[i][j] > dist[i][k] + dist[k][j]) {
						dist[i][j] = dist[i][k] + dist[k][j];
					}
				}
			}
		}
		/*
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cout << dist[i][j] << ' ';
			}
			cout << '\n';
		}*/

		//Run dijkstra for each query

		cout << setprecision(10) << "Case #" << asdf + 1 << ":";

		for (int i = 0; i < q; i++) {
			int start, end;
			cin >> start >> end;
			start--;
			end--;

			dijkstra(start);
			cout << ' ' << shortestTime[end];
		}
		cout << '\n';
		
	}
}