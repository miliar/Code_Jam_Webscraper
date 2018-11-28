#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <fstream>
#include <thread>
#include <assert.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <iomanip>
#include <forward_list>
#include <bitset>
#include <math.h>

using namespace std;

typedef pair<int, int> pt;

long long area(long long r, long long h) {
  return r * r + 2 * h * r;
}

int main(int argc, const char * argv[]) {
  freopen("/Users/efimovmichael/Downloads/ala.txt","r",stdin);
  freopen("/Users/efimovmichael/a.out","w",stdout);

  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    int n, k;
    cin >> n >> k;
    vector<pt> v(n, pt());
    for (int i = 0; i < n; ++i) {
      cin >> v[i].first >> v[i].second;
    }
    sort(v.begin(), v.end(), [](pt& l, pt& r) {
      if (l.first == r.first) {
        return l.second > r.second;
      }
      return l.first > r.first;
    });
    long long maxarea = 0;
    for (int i = 0; i < n-k + 1; ++i) {
      long long ar = area(v[i].first, v[i].second);
      vector<pt> v1(v.begin() + i + 1, v.end());
      sort(v1.begin(), v1.end(), [](pt&l, pt&r) {
        long long rl = l.first;
        long long rr = r.first;
        return rl * l.second > rr * r.second;
      });
      for (int j = 0; j < k-1; ++j) {
        long long r = v1[j].first;
        ar += r * 2 * v1[j].second;
      }
      maxarea = max(maxarea, ar);
    }
    cout << "Case #" << tc << ": " << fixed << setprecision(9) << maxarea * M_PI << endl;
  }

  return 0;
}
