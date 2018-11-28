#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "parenting_partnering"

#pragma comment(linker,"/STACK:32000000")

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

const double PI = 3.1415926535897932384626433832795;

int GetMinSwitches(const vector<pii>& cameron, const vector<pii>& jamie) {
  vector<vi> segments;
  for (int i = 0; i < cameron.size(); ++i) {
    vi segment;
    segment.push_back(cameron[i].first);
    segment.push_back(cameron[i].second - cameron[i].first);
    segment.push_back(0);
    segments.push_back(segment);
  }
  for (int i = 0; i < jamie.size(); ++i) {
    vi segment;
    segment.push_back(jamie[i].first);
    segment.push_back(jamie[i].second - jamie[i].first);
    segment.push_back(1);
    segments.push_back(segment);
  }
  sort(segments.begin(), segments.end());
  int sum = 0;
  for (int i = 0; i < cameron.size(); ++i) {
    sum += cameron[i].second - cameron[i].first;
  }
  int cameron_segment_count = cameron.size();
  vector<int> mergeable;
  vector<int> increasable;
  vector<int> bad;
  for (int i = 0; i < segments.size(); ++i) {
    int nxt = (i + 1) % segments.size();
    int len = (1440 + segments[nxt][0] - segments[i][0] - segments[i][1]) % 1440;
    if (segments[i][2] == 0 && segments[nxt][2] == 0) {
      mergeable.push_back(len);
    }
    if (segments[i][2] != segments[nxt][2]) {
      increasable.push_back(len);
    }
    if (segments[i][2] == 1 && segments[nxt][2] == 1) {
      bad.push_back(len);
    }
  }
  sort(mergeable.begin(), mergeable.end());
  int pos = 0;
  while (pos < mergeable.size() && sum + mergeable[pos] <= 720) {
    sum += mergeable[pos];
    --cameron_segment_count;
    ++pos;
  }
  while (pos < mergeable.size()) {
    increasable.push_back(mergeable[pos]);
    ++pos;
  }
  int pos_inc = 0;
  while (sum < 720 && pos_inc < increasable.size()) {
    sum += increasable[pos_inc];
    ++pos_inc;
  }
  sort(bad.rbegin(), bad.rend());
  int pos_bad = 0;
  while (sum < 720 && pos_bad < bad.size()) {
    sum += bad[pos_bad];
    ++pos_bad;
    ++cameron_segment_count;
  }
  if (sum < 720) {
    cerr << "Can't get 720" << endl;
    abort();
  }
  int result = 2 * cameron_segment_count;
  return result;
}

int GetMinSwitchesDP(const vector<pii>& cameron, const vector<pii>& jamie) {
  vector< vector< vector< vector<int> > > > min_switches(1441, vector<vvi> (721, vvi(2, vi(2, 2000))));
  min_switches[0][0][0][0] = min_switches[0][0][1][1] = 0;
  for (int i = 0; i < 1440; ++i) {
    for (int s = 0; s <= 720; ++s) {
      for (int j = 0; j < 2; ++j) {
        for (int st = 0; st < 2; ++st) {
          for (int k = 0; k < 2; ++k) {
            bool ok = true;
            if (k == 0) {
              if (s == 720) {
                ok = false;
              }
              else {
                for (int t = 0; t < jamie.size(); ++t) {
                  if (jamie[t].first <= i && jamie[t].second > i) {
                    ok = false;
                    break;
                  }
                }
              }
            }
            else {
              for (int t = 0; t < cameron.size(); ++t) {
                if (cameron[t].first <= i && cameron[t].second > i) {
                  ok = false;
                  break;
                }
              }
            }
            if (!ok) {
              continue;
            }
            int value = min_switches[i][s][j][st] + (k == j ? 0 : 1);
            min_switches[i + 1][s + (k == 0 ? 1 : 0)][k][st] = min(min_switches[i + 1][s + (k == 0 ? 1 : 0)][k][st], value);
          }
        }
      }
    }
  }
  return min(min(min_switches[1440][720][0][0], min_switches[1440][720][0][1] + 1), min(min_switches[1440][720][1][0] + 1, min_switches[1440][720][1][1]));
}

int main() {
  /*while (true) {
    vector<pii> cameron;
    vector<pii> jamie;
    int Ac = rand() % 10 + 1;
    int Aj = rand() % 10 + 1;
    cerr << Ac << ' ' << Aj << endl;
    int sum_c = 0;
    int sum_j = 0;
    for (int i = 0; i < Ac; ++i) {
      int left, len;
      do {
        left = rand() % 1440;
        len = rand() % min(720 - sum_c - (Ac - i - 1), 1440 - left) + 1;
        bool ok = true;
        for (int j = 0; j < cameron.size(); ++j) {
          if (max(cameron[j].first, left) < min(cameron[j].second, left + len)) {
            ok = false;
            break;
          }
        }
        if (ok) {
          cameron.push_back(MP(left, left + len));
          sum_c += len;
          break;
        }
      } while (true);
    }
    for (int i = 0; i < Aj; ++i) {
      int left, len;
      do {
        left = rand() % 1440;
        len = rand() % min(720 - sum_j - (Aj - i - 1), 1440 - left) + 1;
        bool ok = true;
        for (int j = 0; j < cameron.size(); ++j) {
          if (max(cameron[j].first, left) < min(cameron[j].second, left + len)) {
            ok = false;
            break;
          }
        }
        if (ok) {
          for (int j = 0; j < jamie.size(); ++j) {
            if (max(jamie[j].first, left) < min(jamie[j].second, left + len)) {
              ok = false;
              break;
            }
          }
        }
        if (ok) {
          jamie.push_back(MP(left, left + len));
          sum_j += len;
          break;
        }
      } while (true);
    }
    cerr << "Computing usual solution" << endl;
    int res1 = GetMinSwitches(cameron, jamie);
    cerr << "Computing dp solution" << endl;
    int res2 = GetMinSwitchesDP(cameron, jamie);
    if (res1 != res2) {
      cerr << "Wrong answer: " << res1 << ' ' << res2 << endl;
      cerr << cameron.size() << ' ' << jamie.size() << endl;
      for (int i = 0; i < cameron.size(); ++i) {
        cerr << cameron[i].first << ' ' << cameron[i].second << endl;
      }
      for (int i = 0; i < jamie.size(); ++i) {
        cerr << jamie[i].first << ' ' << jamie[i].second << endl;
      }
      return 1;
    }
    else {
      cerr << "OK" << endl;
    }
  }*/
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int ti = 0; ti < tests; ++ti) {
    int Ac, Aj;
    cin >> Ac >> Aj;
    vector<pii> cameron(Ac);
    for (int i = 0; i < Ac; ++i) {
      cin >> cameron[i].first >> cameron[i].second;
    }
    vector<pii> jamie(Aj);
    for (int i = 0; i < Aj; ++i) {
      cin >> jamie[i].first >> jamie[i].second;
    }
    int result = GetMinSwitches(cameron, jamie);
    cout << "Case #" << ti + 1 << ": " << result << endl;
    cerr << "Case #" << ti + 1 << ": " << result << endl;
  }
  return 0;
}
