#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long ll;

const int NCITY = 100;

int N;
ll dist[NCITY][NCITY];
ll mcost[NCITY][NCITY];
ll energy[NCITY], speed[NCITY];

class State {
public:
  int city;
  int horse;
  int energy;

  State(int c, int h, int e) : city(c), horse(h), energy(e) {
  }
};

double solve(int u, int v) {
  for(int i = 0; i < N; ++i) {
    fill_n(mcost[i], N, LONG_LONG_MAX);
  }
  multimap<double, State> q;
  q.insert(make_pair(0, State(u, -1, -1)));
  while(!q.empty()) {
    double cost = q.begin()->first;
    State cur = q.begin()->second;
    q.erase(q.begin());

    if(v == cur.city) return cost;

    for(int i = 0; i < N; ++i) {
      ll d = dist[cur.city][i];
      if (d == -1) continue;

      if(d <= energy[cur.city]) {
        double ncost = cost + d / (double)speed[cur.city];
        if(mcost[i][cur.city] > ncost) {
          mcost[i][cur.city] = ncost;
          q.insert(make_pair(ncost, State(i, cur.city, energy[cur.city] - d)));
        }
      }

      if(d <= cur.energy) {
        double ncost = cost + d / (double)speed[cur.horse];
        if(mcost[i][cur.horse] > ncost) {
          mcost[i][cur.horse] = ncost;
          q.insert(make_pair(ncost, State(i, cur.horse, cur.energy - d)));
        }
      }
    }
  }
  assert(false);
}

int main(void){
  int T;
  cin >> T;
  for (int tt = 0; tt < T; ++tt) {
    int Q;
    cin >> N >> Q;
    for(int i = 0; i < N; ++i)
      cin >> energy[i] >> speed[i];
    for(int i = 0; i < N; ++i)
      for(int j = 0; j < N; ++j)
        cin >> dist[i][j];

    cout << "Case #" << tt+1 << ":";

    for(int i = 0; i < Q; ++i) {
      int u, v;
      cin >> u >> v;
      printf(" %.6lf", solve(u-1, v-1));
    }
    cout << endl;
  }

  return 0;
}
