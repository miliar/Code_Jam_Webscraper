#include <iostream>
#include <fstream>

#include <stack>
#include <queue>
#include <deque>
#include <vector>

#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>

#include <cmath>

#include <cassert>

#include <algorithm>

using namespace std;

int main()
{
  ifstream fin("input.txt");
  //ifstream fin("/Users/Zetilov/Downloads/C-small-attempt0.in.txt");
  ofstream fout("output.txt");
  fin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  fout.setf(ios_base::fixed);
  fout.precision(28);

  int T;
  fin >> T;
  for (int cs = 1; cs <= T; ++cs) {
    fout << "Case #" << cs << ": ";
    int n, m, c;
    fin >> n >> c >> m;
    cout << cs << ' ' << c << endl;
    vector<int> sp(n), sc(c);
    for (int i = 0; i < m; ++i) {
      int p, cc;
      fin >> p >> cc;
      //cout << p << ' ' << cc << endl;
      ++sp[p - 1];
      ++sc[cc - 1];
    }
    int L = 0, R = m, M;
    //cout << n << ' ' << m << endl;
    for (auto x : sc) {
      L = max(L, x);
    }
    --L;
    while (R - L > 1) {
      int M = (L + R) / 2;
      int lef = 0;
      for (int i = 0; i < n; ++i) {
        if (sp[i] < M) {
          lef += M - sp[i];
        } else {
          lef -= sp[i] - M;
          if (lef < 0) {
            lef = -1e9;
          }
        }
      }
      if (lef >= 0) {
        R = M;
      } else {
        L = M;
      }
    }
    M = R;
    int add = 0;
    for (int i = 0; i < n; ++i) {
      if (sp[i] > M) {
        add += sp[i] - M;
      }
    }
    fout << R << " " << add << '\n';
  }
  return 0;
}