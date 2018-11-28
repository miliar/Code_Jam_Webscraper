#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

#define REP(a,b) for(int a=0;a<(b);a++)
#define PER(a,b) for(int a=(b)-1;a>=0;a--)
#define ll long long

using namespace std;

int T;

int main() {
  cin >> T;
  assert(cin);

  REP(i, T) {
    string s;
    int k;
    assert(cin >> s);
    assert(cin >> k);

    vector<int> v;
    for (int j = 0; j < s.size(); ++j) {
      if (s[j] == '+')
        v.push_back(0);
      else if (s[j] == '-')
        v.push_back(1);
      else
        break;
    }

    int cc = 0;
    for (int j = 0; j + k <= v.size(); ++j)
      if (v[j]) {
        for (int l = j; l < j + k; ++l)
          v[l] = (v[l] + 1) % 2;
        cc++;
      }

    int tmp = 0;
    for (int j = v.size() - k; j < v.size(); j++)
      tmp += v[j];

    if (tmp)
      cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << i + 1 << ": " << cc << endl;
  }

  return 0;
}
