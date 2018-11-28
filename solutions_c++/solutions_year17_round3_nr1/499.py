#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;
int N;
int K;
vector<pair<long, long>> pancakes;

double exposed_area(pair<long, long> pancake) {
  return 2 * M_PI * pancake.first * pancake.second;
}

bool sort_fun(pair<long, long> a, pair<long, long> b) {
  return exposed_area(a) > exposed_area(b);
}

double try_pancake(int i) {
  pair<long, long> pancake = pancakes[i];
  double exposed = {M_PI * pancake.first * pancake.first + exposed_area(pancake)};
  long radius {pancake.first};
  int taken = 1;
  int j=0;
  while(j<N && taken<K) {
    if(i == j) {
      j++; continue;
    }
    if(pancakes[j].first <= radius) {
      taken++;
      exposed += exposed_area(pancakes[j]);
    }
    j++;
  }
  if(taken == K) return exposed;
  return 0.0;
}

void solve(int t) {
  cerr << "test " << t << endl;
  cin >> N;
  cin >> K;
  pancakes.clear();
  for(int i=0; i<N; i++) {
    pair<long, long> p;
    cin >> p.first;
    cin >> p.second;
    pancakes.push_back(p);
  }
  sort(pancakes.begin(), pancakes.end(), sort_fun);
  double max_exposed = 0;
  for(int i=0; i<N; i++) {
    cerr << "radius: " << pancakes[i].first << " height: " << pancakes[i].second << endl;
    double exposed = try_pancake(i);
    max_exposed = max(max_exposed, exposed);
  }
  cout << setprecision(9);
  cout << "Case #" << t << ": " << max_exposed << endl;
}

int main() {
  cin >> T;
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
