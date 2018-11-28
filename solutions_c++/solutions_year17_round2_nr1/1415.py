#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const __int128 INF = (__int128)1e18 * (__int128)1e18;
const __int128 shift = 1e10;

struct horse {
  __int128 k, v;
  __int128 time;
  bool operator<(const horse &h) const {
    return time < h.time;
  }
  void calc(__int128 dist) {
    time = (dist - k) / v;
  }
};

horse arr[1000];

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int n;
    __int128 dist;
    int d;
    cin >> d >> n;
    dist = (__int128)d * shift;
    for (int i = 0; i < n; ++i) {
      int k, v;
      cin >> k >> v;
      arr[i].k = (__int128)k * shift;
      arr[i].v = v;
      arr[i].calc(dist);
      cerr.precision(10);
      cerr << fixed;
      cerr << (double)dist << endl;
      cerr << arr[i].time / (double)shift << endl;
    }
    horse slowest = *max_element(arr, arr + n);
    cout.precision(10);
    cout << fixed;
    cout << "Case #" << t << ": " << ((double)dist / slowest.time);
    cout << endl;
  }
  return 0;
}