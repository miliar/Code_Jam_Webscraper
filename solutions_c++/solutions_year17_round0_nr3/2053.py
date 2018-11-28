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
ifstream fin("///Users/Zetilov/Downloads/C-large.in.txt");
ofstream fout("output.txt");


void solve()
{
  long long n, k;
  fin >> n >> k;
  map<long long, long long> m;
  m[n] = 1;
  while (k > m.rbegin()->second) {
    auto x = m.rbegin()->first, y = m[x];
    //cout << x << ' ' << y << endl;
    m.erase(x);
    k -= y;
    --x;
    m[x / 2] += y;
    m[x - x / 2] += y;
  }
  long long y = m.rbegin()->first - 1;
  fout << y - y / 2 << ' ' << y / 2;
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
    cout << cs << endl;
    fout << "Case #" << cs << ": ";
    solve();
    fout << endl;
  }
  return 0;
}