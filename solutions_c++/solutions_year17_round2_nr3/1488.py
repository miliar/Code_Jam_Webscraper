#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;





int main() {
    string name = "C-small-attempt2";
	string path = "";

	freopen((path + name + ".in").c_str(), "r", stdin);
	freopen((path + name + ".out").c_str(), "w", stdout);



	int N;
	cin >> N;
	for (int prob = 1; prob <= N; prob++) {
        int q;
        int n; cin >> n >> q;
        double graph[n][n];

        double distance[n];
        double speed[n];

        double timeGraph[n][n];


        // horse travel, speed travel
        for (int i = 0; i < n; ++i) {
            cin >> distance[i] >> speed[i];
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; j++) {
                cin >> graph[i][j];
                timeGraph[i][j] = -1;
                if (i == j) graph[i][j] = timeGraph[i][j] = 0;
            }
        }

        // shortest paths in distance
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if ((graph[i][k] != -1 && graph[k][j] != -1) && (graph[i][j] > graph[i][k] + graph[k][j] || graph[i][j] == -1) ) {
                        graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }
        }



        // time for horse at i to get to j
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                // within horse's range
                if (graph[i][j] > -1 && graph[i][j] <= distance[i]) {
                    // distance / speed
                    timeGraph[i][j] = graph[i][j]/speed[i];
                }
            }
        }

        // shortest paths using times
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if ( (timeGraph[i][k] > -1 && timeGraph[k][j] > -1) && (timeGraph[i][j] > timeGraph[i][k] + timeGraph[k][j] || timeGraph[i][j] < 0) ){
                         timeGraph[i][j] = timeGraph[i][k] + timeGraph[k][j];
                    }
                }
            }
        }

        int u, v;
		//printf("Case #%d: \n", prob);
        cout << "Case #" << prob << ":";
        for (int i = 0; i < q; ++i) {
            cin >> u >> v;
            cout << " " << std::fixed << std::setprecision(6) << timeGraph[u-1][v-1];
        }
        cout << endl;

	}

	return 0;
}
