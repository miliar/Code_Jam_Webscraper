#include<cstdio>
#include<cstdint>
#include<cassert>
#include<cmath>
#include<iostream>
#include<iomanip>
#include<vector>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<string>
#include<algorithm>
#include<utility>
#include<functional>

using namespace std;

int idx(int i, int j, int N) {
  return i * N + j;
}

void single(int i, bool run) {
  // Input
  int N, Q;
  cin >> N >> Q;
  vector<int> E, S;
  for (int i = 0; i < N; i++) {
    int e, s;
    cin >> e >> s;
    E.push_back(e);
    S.push_back(s);
  }
  vector<int> D;
  D.resize(N * N);
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      int d;
      cin >> d;
      D[idx(i, j, N)] = d;
    }
  }
  vector<int> U, V;
  for (int i = 0; i < Q; i++) {
    int u, v;
    cin >> u >> v;
    U.push_back(u - 1);
    V.push_back(v - 1);
  }
  if (! run) return;
  // Solve
  cout << "Case #" << i << ": ";
  for (int k = 0; k < Q; k++) {
    vector<double> reachAt(N*N, INFINITY);
    vector<int> leftoverDist(N*N, -1);
    //reachAt[idx(U[k], U[k], N)] = 0;
    //leftoverDist[idx(U[k], U[k])] = E[U[k]];
    reachAt[idx(1, 0, N)] = D[idx(U[k], 1, N)] * 1.0 / S[U[k]];
    //cerr << 1 << " " << 0 << " " << reachAt[idx(1, 0, N)] << endl;
    leftoverDist[idx(1, 0, N)] = E[U[k]] - D[idx(U[k], 1, N)];
    for (int i = 1; i < N-1; i++) {
      int next_city = i + 1;
      int city = i;
      int dist = D[idx(city, next_city, N)];
      double reachTime = INFINITY;
      for (int j = 0; j < city; j++) {
        reachTime = fmin(reachTime, reachAt[idx(city, j, N)]);
      }
      // try continuing with horse
      for (int j = 0; j < city; j++) {
        int leftover = leftoverDist[idx(city, j, N)];
        if (leftover < dist) continue;
        leftoverDist[idx(next_city, j, N)] = leftover - dist;
        reachAt[idx(next_city, j, N)] = reachAt[idx(city, j, N)] + dist * 1.0 / S[j];
//        cerr << next_city << " " << j << " " << reachAt[idx(next_city, city, N)] << endl;
      }
      // try fresh horse
      if (E[city] < dist) continue;
      leftoverDist[idx(next_city, city, N)] = E[city] - dist;
      reachAt[idx(next_city, city, N)] = reachTime + dist * 1.0 / S[city];
  //    cerr << next_city << " " << city << " " << reachAt[idx(next_city, city, N)] << endl;
    }
    double reachTime = INFINITY;
    for (int j = 0; j < N; j++) {
      reachTime = fmin(reachTime, reachAt[idx(V[k], j, N)]);
    }
    cout << setprecision(9) << reachTime << " ";
  }
  cout << endl;
}

int main(int argc, char ** argv) {
  FILE * ret;
  ret = freopen(argv[1], "r", stdin);
  assert(ret != nullptr);
  int testcases;
  cin >> testcases;
  int first_testcase = 1;
  int last_testcase = testcases;
  if (argc >= 3) first_testcase = atoi(argv[2]);
  if (argc >= 4) last_testcase = atoi(argv[3]);
  for (int i = 1; i <= testcases; i++) {
    single(i, i >= first_testcase && i <= last_testcase);
  }
  return EXIT_SUCCESS;
}
