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

int getmin(int m, int r) {
  int k = m*10 / (11 * r);
  if (k * r * 11 < m * 10) {
    ++k;
  }
  return k;
}

int getmax(int m, int r) {
  int k = m*10 / (9 * r);
  return k;
}

int main(int argc, const char * argv[]) {
  freopen("/Users/efimovmichael/Downloads/b1.txt","r",stdin);
  freopen("/Users/efimovmichael/b.out","w",stdout);

  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    int n, p;
    cin >> n >> p;
    vector<int> r(n, 0);
    for (int i = 0; i < n; ++i) {
      cin >> r[i];
    }
    vector<vector<int>> m(n, vector<int>(p, 0));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        cin >> m[i][j];
      }
      sort(m[i].begin(), m[i].end());
    }
    vector<int> v(n, 0);
    int count = 0;
    while (true) {
      bool stop = false;
      for (int i = 0; i < n; ++i) {
        if (v[i] == p) {
          stop = true;
          break;
        }
      }
      if (stop) {
        break;
      }
      int kmin = 1;
      int kmax = 10000000;
      for (int i = 0; i < n; ++i) {
        kmin = max(kmin, getmin(m[i][v[i]], r[i]));
        kmax = min(kmax, getmax(m[i][v[i]], r[i]));
      }
      if (kmin > kmax) {
        int imin = 0;
        for (int i = 1; i < n; ++i) {
          if (getmax(m[i][v[i]], r[i]) < getmax(m[imin][v[imin]], r[imin])) {
            imin = i;
          }
        }
        v[imin]++;
      } else {
        ++count;
        for (int i = 0; i < n; ++i) {
          v[i]++;
        }
      }
    }
    cout << "Case #" << tc << ": " << count << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
