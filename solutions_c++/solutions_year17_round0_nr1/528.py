#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <cmath>
#include <utility>
#include <set>
#include <string>

using namespace std;

int main()
{
  cin.sync_with_stdio(false);
  int tests;
  std::string cakes;
  int k;
  cin >> tests;
  for (auto t = 0; t < tests; t++)
  {
    cin >> cakes >> k;
    std::vector<char> v(cakes.size());
    int nothappy = 0;
    transform(cakes.begin(), cakes.end(), v.begin(),
        [&nothappy](char c) { return c=='-' ? ++nothappy, 1 : 0; });
    int flips = 0;
    for (auto s = 0; s <= v.size() - k && nothappy > 0; ++s)
    {
      if (!v[s])
        continue;
      for (auto ss = s; ss < s + k; ++ss)
      {
        nothappy -= v[ss] ? 1 : -1;
        v[ss] ^= 1;
      }
      ++flips;
    }
    cout << "Case #" << t + 1 << ": ";
    if (nothappy)
      cout << "IMPOSSIBLE\n";
    else
      cout << flips << endl;
  }

  return 0;
}
