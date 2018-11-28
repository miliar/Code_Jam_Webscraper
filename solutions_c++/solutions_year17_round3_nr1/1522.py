#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

vector<double> radius;
vector<double> area;
vector<pair<double, int> > pancakes;

void solve() {
  int N, K;
  cin >> N >> K;
  radius.clear();
  radius.resize(N);
  area.clear();
  area.resize(N);
  pancakes.clear();
  for(int i = 0; i < N; ++i) {
    double r, h;
    cin >> r >> h;
    pancakes.push_back(make_pair(-M_PI * 2 * r * h, i));
    radius[i] = r;
    area[i] = M_PI * 2 * r * h + M_PI * r * r;
  }

  sort(pancakes.begin(), pancakes.end());

  double most = -1;
  for(int i = 0; i < N; ++i) {
    double a = area[i];
    int j = 0;
    int c = 1;
    while(c < K && j < N) {
      if(pancakes[j].second != i && radius[pancakes[j].second] <= radius[i]) {
        c++;
        a += -pancakes[j].first;
      }
      j++;
    }

    if(c == K) {
      most = max(most, a);
    }
  }

  cout << most << endl;
}

int main() {
  cout << setprecision(16);
  cout << fixed;

  int T;
  cin >> T;
  for(int c = 0; c < T; ++c) {
    cout << "Case #" << (c+1) << ": ";
    solve();
  }

  return 0;
}
