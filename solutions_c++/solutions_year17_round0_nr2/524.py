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
  int tests;
  cin >> tests;
  long long n;
  for (auto t = 1; t <= tests; ++t)
  {
    cin >> n;
    vector<int> digs;
    while (n > 0)
      digs.push_back(n % 10), n /= 10;
    auto it = adjacent_find(digs.rbegin(), digs.rend(), 
        [](int left, int right) { return right < left; });
    if (it != digs.rend())
    {
      auto val = *it;
      while (it != digs.rbegin() && *(it-1) == val)
        --it;
      (*it)--;
      fill(it + 1, digs.rend(), 9);
    }
    it = digs.rbegin();
    while(*it == 0)
      ++it;
    cout << "Case #" << t << ": ";
    for (; it != digs.rend(); ++it)
      cout << *it;
    cout << endl;
  }

  return 0;
}
