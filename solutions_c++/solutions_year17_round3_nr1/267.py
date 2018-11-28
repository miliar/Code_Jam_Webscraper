#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

int main()
{
  int T;
  cin >> T;

  const double pi = 3.14159265358979323846;

  auto cmp = [] (const int& a, const int& b) {
    return a>b;
  };

  for (int i = 0; i < T; i++)
  {
    int64_t K, N;
    cin >> N >> K;
    vector<int> inds(N), inds2(N);
    vector<double> r(N), h(N), top(N), side(N);
    for (int j = 0; j < N; j++) {
      cin >> r[j] >> h[j];
      inds[j] = j;
      inds2[j] = j;
      top[j] = pi * r[j] * r[j];
      side[j] = 2 * pi * r[j] * h[j];
    }

    std::sort(inds.begin(), inds.end(), [&r, &h](const int& a, const int& b) {
      return r[a] > r[b] || (r[a] == r[b] && h[a] > h[b]);
    });

    std::sort(inds2.begin(), inds2.end(), [&side, &r](const int& a, const int& b) {
      return side[a] > side[b] || (side[a] == side[b] && r[a] > r[b]);
    });

    double res = 0.0;
    double maxTop = 0.0;

    for (int x = 0; x < K-1; x++) {
      res += side[inds2[x]];
      maxTop = max(maxTop, top[inds2[x]]);
    }

    double lmax = 0.0;
    for (int x = K-1; x < N; x++) {
      lmax = max(lmax, max(maxTop, top[inds2[x]]) + side[inds2[x]]);
    }

    res += lmax;

    cout << "Case #" << i+1 << ": " << setprecision(12) << res << endl;
  }

  return 0;
}
