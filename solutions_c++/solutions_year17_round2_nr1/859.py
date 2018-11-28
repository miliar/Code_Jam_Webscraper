
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;


void solve(int case_, int distance, std::vector<std::pair<int, int>>& horses) {
  // cout << "distance: " << distance << endl;
  double best_time = 0;
  for(auto& horse: horses) {
    double t = ((double)distance - (double)horse.first) / (double)horse.second;
    if(t > best_time) { best_time = t; }
    // cout << horse.first << " " << horse.second << " " << t << endl;
  }
  double best = distance / best_time;
  printf("Case #%d: %f\n", case_, best);
  //  std::cout << "Case #" << case_ << ": " << best << endl;
}

int main() {
  int t_num;
  cin >> t_num;
  for (auto t = 1; t <= t_num; ++t) {
    int D, N;
    cin >> D >> N;
    std::vector<std::pair<int, int>> data(N);
    for(int i = 0; i < N; ++i) {
      cin >> data[i].first >> data[i].second;
    }
    solve(t, D, data);
  }
}
