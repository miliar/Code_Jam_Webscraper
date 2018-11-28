/*
 * c.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: istrandjev
 */

#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";

struct horse {
  int distance;
  double speed;
};
vector<horse> horses;
vector<vector<pair<int, ll> > > ne;
vector<vector<ll> > total_distance;
int n;

double solve(int from, int to) {
  priority_queue<pair<double, pair<int, int> > > tc;
  tc.push(mpair(0.0, mpair(from, from)));
  vector<vector<double> > dist(n, vector<double>(n, -1.0));
  vector<vector<char> > vis(n, vector<char>(n, 0));
  dist[from][from] = 0.0;
  double best = 1e100;
  while (!tc.empty()) {
    double d = -tc.top().first;
    int city = tc.top().second.first;
    int horse_index = tc.top().second.second;
    tc.pop();
    if (vis[city][horse_index]) {
      continue;
    }
    vis[city][horse_index] = 1;
    if (city == to) {
      best = min(best, d);
    }
    for (int i = 0; i < (int)ne[city].size(); ++i) {
      int next_city = ne[city][i].first;
      // continue on with same horse
      if (total_distance[horse_index][next_city] <= horses[horse_index].distance
          && vis[next_city][horse_index] == 0) {
        double time_needed = double(ne[city][i].second)
            / horses[horse_index].speed;
        if (dist[next_city][horse_index] < -0.5
            || dist[next_city][horse_index] > d + time_needed) {
          dist[next_city][horse_index] = d + time_needed;
          tc.push(
              mpair(-dist[next_city][horse_index],
                  mpair(next_city, horse_index)));
        }
      }
      if (ne[city][i].second <= horses[city].distance
          && vis[next_city][city] == 0) {
        double time_needed = double(ne[city][i].second) / horses[city].speed;
        if (dist[next_city][city] < -0.5
            || dist[next_city][city] > d + time_needed) {
          dist[next_city][city] = d + time_needed;
          tc.push(mpair(-dist[next_city][city], mpair(next_city, city)));
        }
      }
    }
  }

  return best;
}
int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    cerr << "On test" << it << endl;
    int q;
    cin >> n >> q;
    horses.clear();
    horses.resize(n);
    for (int i = 0; i < (int)horses.size(); ++i) {
      int ispeed;
      scanf("%d %d", &horses[i].distance, &ispeed);
      horses[i].speed = ispeed;
    }
    ne.clear();
    ne.resize(n);
    total_distance.clear();
    total_distance.resize(n, vector<ll>(n, -1));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        int d;
        scanf("%d", &d);
        if (d != -1) {
          ne[i].push_back(mpair(j, (ll)d));
          total_distance[i][j] = d;
        }
      }
    }

    for (int k = 0; k < n; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (i == j || total_distance[i][k] == -1
              || total_distance[k][j] == -1) {
            continue;
          }
          if (total_distance[i][j] == -1
              || total_distance[i][k] + total_distance[k][j]
                  < total_distance[i][j]) {
            total_distance[i][j] = total_distance[i][k] + total_distance[k][j];
          }
        }
      }
    }
    vector<double> res;
    for (int i = 0; i < q; ++i) {
      int x, y;
      cin >> x >> y;
      res.push_back(solve(x - 1, y - 1));
    }

    cout << "Case #" << it << ": ";
    for (int i = 0; i < (int)res.size(); ++i) {
      printf("%.9lf%c", res[i], ((i + 1) != res.size() ? ' ' : '\n'));
    }
  }
  return 0;
}

