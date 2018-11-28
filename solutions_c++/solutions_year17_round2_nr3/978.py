#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;
int N;

int test_case;

map<int, int> horse_length;
map<int, int> horse_speed;
map<pair<int, int>, int> original_distances;
map<pair<int, int>, double> times;

map<int, double> places;

int find_min(map<int, long> &places) {
  int min_index = -1;
  int min = numeric_limits<int>::max();
  for(pair<int, int> p : places) {
    if(p.second < min) {
      min = p.second;
      min_index = p.first;
    }
  }
  return min_index;
}

int find_min(map<int, double> &places) {
  int min_index = -1;
  double min = numeric_limits<double>::max();
  for(pair<int, double> p : places) {
    //cerr << "compare " << p.first << ": " << p.second << " with " << min << endl;
    if(p.second < min) {
      min = p.second;
      min_index = p.first;
    }
  }
  return min_index;
}

long sd(int from, int to) {
  map<int, long> plac;
  set<int> seen;
  plac[from] = 0;
  while(true) {
    int amin = find_min(plac);
    seen.insert(amin);
    if(amin == to) {
      if(plac[amin] == 0) return -1;
      return plac[amin];
    }
    long start_dist = plac[amin];
    plac.erase(amin);
    pair<int, int> p;
    for(int i=1; i<=N; i++) {
      if(seen.find(i) != seen.end()) continue;
      p.first = amin;
      p.second = i;
      if(original_distances[p] != -1) {
        auto it = plac.find(i);
        long dist = numeric_limits<long>::max();
        if(it != plac.end()) {
          dist = it->second;
        }
        if(test_case == 29) {
          //cerr << "compare " << dist << " with " << start_dist << " + " << original_distances[p] << endl;
        }
        dist = min(dist, start_dist + original_distances[p]);
        plac[i] = dist;
      }
    }
  }
}

void calculate_times() {
  for(int i=1; i<=N; i++) {
    for(int j=1; j<=N; j++) {
      pair<int, int> p;
      p.first = i;
      p.second =j;
      if(i == j) {
        times[p] = -1;
        continue;
      }
      long dist = sd(i, j);
      if(dist == -1) {
        times[p] = -1;
      }
      else if(dist <= horse_length[i]) {
        if(test_case == 29) {
          //cerr << "divide: " << (1.0*dist) << "/" << (1.0 * horse_speed[i]) << endl;
        }
        times[p] = (1.0*dist)/(1.0 * horse_speed[i]);
      } else {
        times[p] = -1;
      }
    }
  }
}

double delivery_time(int from, int to) {
  places.clear();
  places[from] = 0;
  while(true) {
    int amin = find_min(places);
    //cerr << "Min: " << amin << " " << places[amin] << endl;
    if(amin == to) return places[amin];
    double start_time = places[amin];
    places.erase(amin);
    for(int i=1; i<=N; i++) {
      pair<int, int> p;
      p.first = amin;
      p.second = i;
      //cerr << "lookup " << p.first << ", " << p.second << endl;
      if(times.at(p) != -1) {
        //cerr << "from " << p.first << " to " << p.second << " is " << times[p] << endl;
        double time = times[p];
        auto it = places.find(i);
        double prev_time = numeric_limits<double>::max();
        if(it != places.end()) {
          prev_time = it->second;
        }
        //cerr << "set " << i << " to " << min(start_time + time, prev_time) << endl;
        //cerr << "before: " << prev_time << endl;
        //cerr << "or " << start_time << " + " << time << endl;
        places[i] = min(start_time + time, prev_time);
      }
    }
  }
}

void solve(int t) {
  horse_length.clear();
  horse_speed.clear();
  original_distances.clear();
  times.clear();
  cerr << "test " << t << endl;
  int Q;
  cin >> N >> Q;
  for(int i=1; i<=N; i++) {
    int l;
    int s;
    cin >> l >> s;
    horse_length[i] = l;
    horse_speed[i] = s;
  }
  
  for(int i=1; i<=N; i++) {
    for(int j=1; j<=N; j++) {
      int d;
      pair<int, int> p;
      cin >> d;
      p.first = i;
      p.second =j;
      original_distances[p] = d;
    }
  }
  calculate_times();
  cerr << "done calculating times " << endl;
  if(test_case == 29) {
    for(int i=1; i<=N; i++) {
      for(int j=1; j<=N; j++) {
        pair<int, int> p = {i, j};
        //cerr << "from " << i << " to " << j << ": " << times[p] << endl;
      }
    }
  }
  cout << "Case #" << t << ": ";
  for(int i=0; i<Q; i++) {
    int from;
    int to;
    cin >> from >> to;
    //cerr << "find dist from " << from << " to " << to << endl;
    double time = delivery_time(from, to);
    if(i > 0) cout << " ";
    cout << time;
  }
  cout << endl;
}

int main() {
  cout << setprecision(9);
  cin >> T;
  for(int t=0; t<T; t++) {
    test_case = t+1;
    solve(t+1);
  }
}
