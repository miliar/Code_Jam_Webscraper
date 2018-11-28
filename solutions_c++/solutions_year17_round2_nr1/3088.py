#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>      // std::setprecision

using namespace std;

int D, N;

vector<pair<int, int> > horses;

double solve() {
  vector<pair<double, int> > results;

  for (int i=0; i<N; i++) {
    int remaining = D - horses[i].first;


    if (remaining > 0) {
      results.push_back(make_pair(remaining * 1.0 / horses[i].second, i));
    }
  }

  if (results.size() == 0) {
    return D;
  }

  sort(results.begin(), results.end());

  double slowest = results[results.size()-1].first;

  return D / slowest;
}

int main() {
  int T;
  cin >> T;

  for (int i=0; i<T; i++) {
    cin >> D >> N;
    horses = vector<pair<int, int> > (N);
    for (int j=0; j<N; j++) {
      cin >> horses[j].first >> horses[j].second;
    }

    double result = solve();

    cout << std::fixed;

    cout << "Case #" << (i+1) << ": " << std::setprecision(6) << result << endl;
  }

  return 0;
}
