#include <iostream>
#include <algorithm>
#include <set>

using namespace std;


const double PI = 3.14159265359;

struct cake {
  long long r, h;
  bool operator<(cake c) const {
    if (r == c.r)
      return h > c.h;
    return r > c.r;
  }
};

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int n, k;
    cin >> n >> k;
    vector<cake> arr(n);
    vector<long long> h_suff(n);
    set<pair<long long, int>> hts;
    for (int i = 0; i < n; ++i) {
      cin >> arr[i].r >> arr[i].h;
    }
    sort(arr.begin(), arr.end());
    long long Ht = 0;
    for (int i = 0; i < k - 1; ++i) {
      hts.insert({arr[n - i - 1].h * 2 * arr[n - i - 1].r, n - i - 1});
      Ht += arr[n - i - 1].h * 2 * arr[n - i - 1].r;
    }
    h_suff[n - k] = Ht;
    for (int i = n - k; i > 0; --i) {
      if (hts.size() && (arr[i].h * 2 * arr[i].r > hts.begin()->first)) {
        Ht -= hts.begin()->first;
        Ht += arr[i].h * 2 * arr[i].r;
        hts.erase(hts.begin());
        hts.insert({arr[i].h * 2 * arr[i].r, i}); 
      }
      h_suff[i - 1] = Ht;
    }
    long long ans = 0;
    for (int be = 0; be + k <= n; ++be) {
      ans = max(ans, h_suff[be] + arr[be].h * 2 * arr[be].r + arr[be].r * arr[be].r);
    }
    cout.precision(10);
    cout << fixed;
    cout << "Case #" << t << ": " << (double)ans * PI << endl;
  }
  return 0;
}