#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool cmp(pair<uint, string> a, pair<uint, string> b) {
  return a.first < b.first;
}

int main()
{
  uint nCase;
  cin >> nCase;
  for (auto iCase = 1; iCase <= nCase; ++iCase) {
    uint n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    // int nL = max(r, max(y, b));
    // int nS = min(r, min(y, b));
    // int nM = (r + y + b) - nL - nS;

    vector<pair<uint, string>> mapping;
    mapping.push_back(make_pair(r, "R"));
    mapping.push_back(make_pair(y, "Y"));
    mapping.push_back(make_pair(b, "B"));

    sort(mapping.begin(), mapping.end(), cmp);
    uint nS = mapping[0].first;
    uint nM = mapping[1].first;
    uint nL = mapping[2].first;

    string S = mapping[0].second;
    string M = mapping[1].second;
    string L = mapping[2].second;

    string ans;
    if (nS + nM < nL) {
      ans = "IMPOSSIBLE";
    } else {
      uint nd = nS + nM - nL;
      for (auto i = 0; i < nL; ++i) {
        string base;
        if (i < nM) {
          base = "" + L + M;
        } else {
          base = "" + L + S;
        }

        if (i < nd) {
          ans += base + S;
        } else {
          ans += base;
        }
      }
    }

    cout << "Case #" << iCase << ": " << ans << endl;
  }

  return 0;
}
