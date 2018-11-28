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
  //ifstream fin("input.txt");
  ifstream fin("/Users/Zetilov/Downloads/A-small-attempt1.in.txt");
  ofstream fout("output.txt");
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  fout.setf(ios_base::fixed);
  fout.precision(28);

  int T;
  fin >> T;
  for (int cs = 1; cs <= T; ++cs) {
    fout << "Case #" << cs << ": ";
    cout << cs << endl;
    int n, p;
    fin >> n >> p;
    vector<int> s(4);
    for (int i = 0; i < n; ++i) {
      int x;
      fin >> x;
      ++s[x % p];
    }
    int res = s[0];
    if (p == 2) {
      fout << res + (s[1] + 1) / 2 << '\n';
    }
    if (p == 3) {
      fout << res + min(s[1], s[2]) + (max(s[1], s[2]) - min(s[1], s[2]) + 2) / 3 << '\n';
    }
    if (p == 4) {
      res += min(s[1], s[3]);
      int nr = min(max(s[1], s[3]) / 2, s[2]);
      res += nr;
      s[1] -= 2 * nr;
      s[3] -= 2 * nr;
      s[2] -= nr;
      if (s[2] > 0) {
        res += s[2] / 2 + (s[2] % 2 + max(s[1], s[3]) > 0);
      } else {
        res += (max(s[1], s[3]) + 3) / 4;
      }
      fout << res << '\n';
    }
  }
  return 0;
}