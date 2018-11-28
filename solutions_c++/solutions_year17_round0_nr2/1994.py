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


//auto& fin = cin;
//auto& fout = cout;
ifstream fin("///Users/Zetilov/Downloads/B-large.in.txt");
ofstream fout("output.txt");


void solve()
{
  long long n;
  fin >> n;
  vector<int> v;
  auto cn = n;
  while (cn > 0) {
    v.push_back(cn % 10);
    cn /= 10;
  }
  reverse(v.begin(), v.end());
  long long c = 0, cc = 0;
  for (int i = 0; i < v.size(); ++i) {
    cc = c;
    cc *= 10;
    cc += v[i];
    for (int j = i + 1; j < v.size(); ++j) {
      cc *= 10;
      cc += v[i];
    }
    c *= 10;
    c += v[i];
    if (cc > n) {
      --c;
      for (auto &x : v) {
        x = 9;
      }
    }
  }
  fout << c;
}

int main()
{
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  cout.setf(ios_base::fixed);
  cout.precision(28);

  int T;
  fin >> T;
  for (int cs = 1; cs <= T; ++cs) {
    fout << "Case #" << cs << ": ";
    solve();
    fout << endl;
  }
  return 0;
}