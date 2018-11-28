
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;
using mat = vector<vector<double>>;

const double inf = 1e50;

struct Horse {
  double max_dist;
  double speed;
};

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++) {
    int N, Q;
    //1) Read input
    cin >> N >> Q;
    vector<Horse> horses(N);
    for (int i=0; i<N; i++) 
      cin >> horses[i].max_dist >> horses[i].speed;
    mat dist(N, vector<double>(N,0.0)), time(N, vector<double>(N,0.0));
    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
        cin >> dist[i][j];
        if (dist[i][j]==-1) dist[i][j] = inf;
      }
    }

    //2) Compute distances
    for (int k=0; k<N; k++) {
      for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        }
      }
    }
    //3) Compute time without changing horses
    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
        if (dist[i][j] <= horses[i].max_dist)
          time[i][j] = dist[i][j] / horses[i].speed;
        else
          time[i][j] = inf;
      }
    }
    //4) Compute optimal time allowing change horse
    for (int k=0; k<N; k++) {
      for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
          time[i][j] = min(time[i][j], time[i][k] + time[k][j]);
        }
      }
    }
    //5) Read and answer queries
    cout << "Case #" << tc << ":";
    for (int q=0; q<Q; q++) {
      int u, v;
      cin >> u >> v;
      cout << " " << setprecision(8) << fixed << time[u-1][v-1];
    }
    cout << endl;
  }
}
