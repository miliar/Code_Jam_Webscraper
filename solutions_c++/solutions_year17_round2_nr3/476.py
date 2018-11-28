#include <iostream>
#include <fstream>

#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

using std::vector;
using std::string;
using std::pair;

struct State {
  int city;
  int horse;
  int64_t capacity;


  bool operator<(const State& other) const {
    return make_tuple(city, horse, capacity) < make_tuple(other.city, other.horse, other.capacity);
  }
};

void work(std::ifstream& in, std::ofstream& out) {
  int n, q;
  in >> n >> q;
  vector<int64_t> e(n);
  vector<double> sp(n);

  for (int i = 0; i < n; ++i) {
    in >> e[i] >> sp[i];
  }
  
  vector<vector<int64_t>> dist(n, vector<int64_t>(n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      in >> dist[i][j];
    }
  }

  for (int i = 0; i < q; ++i) {
    int from, to;
    in >> from >> to;
    --from; --to;

    map<State, double> time;
    State s;
    s.city = from;
    s.horse = from;
    s.capacity = e[from];

    time[s] = 0;

    set<pair<double, State>> top;
    top.insert({ 0, s });

    while(!top.empty()) {
      State s = top.begin()->second;
      top.erase(top.begin());
      if (s.city == to) {
        out << setprecision(10) << time[s] << ' ';
        break;
      }

      for (int j = 0; j < n; ++j) {
        if (dist[s.city][j] != -1) {
          if (s.capacity >= dist[s.city][j]) {
            State curr = s;
            curr.city = j;
            curr.capacity -= dist[s.city][j];
            double t = time[s] + dist[s.city][j] / sp[s.horse];
            if (time.find(curr) == time.end() || time[curr] > t) {
              top.insert({ t, curr });
              time[curr] = t;
            }
            curr.horse = curr.city;
            curr.capacity = e[curr.horse];            
            if (time.find(curr) == time.end() || time[curr] > t) {
              top.insert({ t, curr });
              time[curr] = t;
            }
          }
        }
      }
    }
  }
  out << '\n';
}

int main() {

  std::ifstream in("input.in");
  std::ofstream out("output.out");

  size_t T;
  in >> T;

  for (size_t i = 0; i < T; ++i) {
    out << "Case #" << i + 1 << ": ";
    work(in, out);
  }
  return 0;
}