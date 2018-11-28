#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";
int n, c, m;
int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    cerr << "Processing case " << it << endl;
    cin >> n >> c >> m;
    vector<pair<int,int> > a(m);
    for (int i = 0; i < (int)a.size(); ++i) {
      scanf("%d %d", &a[i].first, &a[i].second);
      a[i].first--;
      a[i].second--;
    }
    vector<int> cnt(c, 0);
    for (int i = 0; i < (int)a.size(); ++i) {
      cnt[a[i].second]++;
    }

    int answer = 0;
    for (int i = 0; i < (int)cnt.size(); ++i) {
      answer = max(answer, cnt[i]);
    }
    vector<int> br(n, 0);
    for (int i = 0; i < (int)a.size(); ++i) {
      br[a[i].first]++;
    }
    int cur = 0;
    for (int i = 0; i < n; ++i) {
      int temp = (cur + br[i] + i) / (i + 1);
      if (temp > answer) {
        answer = temp;
      }
    }
    int needed = 0;
    for (int i = 0; i < n; ++i) {
      if (br[i] > answer) {
        needed += br[i] - answer;
      }
    }
    cout << "Case #" << it << ": " << answer << " " << needed << endl;
  }
  return 0;
}
