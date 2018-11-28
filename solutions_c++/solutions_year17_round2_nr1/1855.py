#include <algorithm>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

double invertLine(int y, const pair<int, int> &line) {
  return (double) (y - line.first)/((double) line.second);
}

double maximizeSlope(int D,
                     const vector<pair<int, int>> &lines) {
  int N = lines.size();
  pair<int, int> slowestLine = lines.front();
  double slowestTime = invertLine(D, slowestLine);
  for (int i = 1; i < N; ++i) {
    double t = invertLine(D, lines[i]);
    if (slowestTime < t) slowestTime = t;
  }
  return D/slowestTime;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  cout << fixed << setprecision(6);
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    int D, N;
    cin >> D >> N;
    vector<pair<int, int>> lines; lines.reserve(N);
    for (int i = 0; i < N; ++i) {
      int K, S;
      cin >> K >> S;
      lines.emplace_back(K, S);
    }
    cout << "Case #" << t << ": "
         << maximizeSlope(D, lines)
         << '\n';
  }
  cout << flush;
  return 0;
}

