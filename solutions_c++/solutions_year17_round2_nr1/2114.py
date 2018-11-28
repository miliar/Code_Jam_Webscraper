#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
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
#include <time.h>
#include <iomanip>
#include <forward_list>

using namespace std;

int main(int argc, const char * argv[]) {
  freopen("/Users/efimovmichael/Downloads/a2.txt","r",stdin);
  freopen("/Users/efimovmichael/a.out","w",stdout);

  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    int d, n;
    cin >> d >> n;
    vector<pair<int, int>> h(n, pair<int, int>());
    for (int i = 0; i < n; ++i) {
      cin >> h[i].first >> h[i].second;
    }
    sort(h.begin(), h.end(), [](pair<int, int>& l, pair<int, int>& r) {
      return l.first > r.first;
    });
    double slowest = (double)(d - h[0].first) / h[0].second;
    for (int i = 1; i < n; ++i) {
      double cur = (double)(d - h[i].first) / h[i].second;
      if (cur > slowest) {
        slowest = cur;
      }
    }
    double res = d / slowest;
    cout << "Case #" << tc << ": " << fixed << setprecision(6) << res << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
