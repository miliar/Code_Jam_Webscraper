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

  REP(tcase, T) {
    string s;
    assert(cin >> s);

    vector<int> v;
    for (int j = 0; j < s.size(); ++j) {
      if (s[j] < '0' || s[j] > '9')
        break;
      v.push_back(s[j] - '0');
    }

    for (int j = 0; j + 1 < v.size(); ++j)
      if (v[j] > v[j + 1]) {
        for (int l = j + 1; l < v.size(); ++l)
          v[l] = 9;
        for (int l = j ; l >= 0; --l) {
          v[l] --;
          if (l == 0 || v[l - 1] <= v[l]) break;
          v[l]= 9;
        }
        break;
      }

    cout << "Case #" << tcase + 1 << ": ";
    for (int j = 0; j < v.size(); ++j)
      if (v[j])
        cout << v[j];
    cout << endl;
  }

  return 0;
}
