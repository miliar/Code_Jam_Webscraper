#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

struct Horse {
  int64_t e, s;

};

istream& operator >> (istream& is, Horse& horse) {
  return is >> horse.e >> horse.s;
}

vector<double> subsolve(int start, const vector<vector<int>>& lengths, const Horse horse) {
  const int n = lengths.size();
  vector<int64_t> distances(n, 1e18);
  distances[start] = 0;
  vector<int> used(n, 0);
  for(int i = 0; i < n; ++i){
    int best = 0;
    for(int j = 1; j < n; ++j){
      if(used[best]){
        best = j;
      }
      if(used[j]){
        continue;
      }
      if(distances[best] > distances[j]){
        best = j;
      }
    }
    used[best] = 1;
    for(int j = 0; j < n; ++j){
      if(lengths[best][j] == -1){
        continue;
      }
      int64_t newDistance = distances[best] + lengths[best][j];
      if(newDistance <= horse.e && newDistance <= distances[j]){
        distances[j] = newDistance;
      }
    }
  }
  vector<double> times(n);
  transform(distances.begin(), distances.end(), times.begin(),
      [horse](int64_t d){return double(d) / horse.s;});
  return times;
}

void solve() {
  int n, q;
  cin >> n >> q;
  vector<Horse> horses(n);
  copy_n(istream_iterator<Horse>(cin), n, horses.begin());
  vector<vector<int>> lengths(n, vector<int>(n));
  for(int i = 0; i < n; ++i){
    copy_n(istream_iterator<int>(cin), n, lengths[i].begin());
  }
  vector<vector<double>> times(n);
  for(int i = 0; i < n; ++i){
    times[i] = subsolve(i, lengths, horses[i]);
  }
  for(int k = 0; k < n; ++k){
    for(int i = 0; i < n; ++i){
      for(int j = 0; j < n; ++j){
        times[i][j] = min(times[i][j], times[i][k] + times[k][j]);
      }
    }
  }
  for(int query = 0; query < q; ++query){
    int u, v;
    cin >> u >> v;
    cout << times[u - 1][v - 1] << ' ';
  }
  cout << endl;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(12);
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}
