#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#include <algorithm>
using namespace std;

typedef pair<double, double> PDD;

double backtracking(const vector<PDD>& pancakes, int pos, int to_stack, double surface_area, double latera_area) {
  if (to_stack == 0) return surface_area + latera_area;
  if (pos >= pancakes.size()) return -1;
  return max(
      backtracking(pancakes, pos+1, to_stack-1, max(surface_area, pancakes[pos].first), latera_area + pancakes[pos].second),
      backtracking(pancakes, pos+1, to_stack, surface_area, latera_area)
    );
}

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int N, K;
    cin >> N >> K;
    vector<PDD> pancakes(N);
    for (int i = 0; i < N; ++i) {
      long long R, H;
      cin >> R >> H;
      pancakes[i].first = M_PI*R*R;
      pancakes[i].second = 2*M_PI*R*H;
    }
    cout.precision(9);
    cout.setf(ios::fixed);
    cout << "Case #" << cas << ": " << backtracking(pancakes, 0, K, 0.0, 0.0) << endl;
  }
}
