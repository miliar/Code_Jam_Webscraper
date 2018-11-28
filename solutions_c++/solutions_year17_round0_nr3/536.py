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
  for (auto t = 1; t <= tests; ++t)
  {
    long long n, k; 
    cin >> n >> k;
    long long lval = n, rval = n;
    long long decr = 1;
    while (k > decr)
    {
      lval = (lval - 1) / 2;
      rval = rval / 2;
      k -= decr;
      n -= decr;
      decr <<= 1;
    }
    auto count_rval = n - decr * lval;
    if (k > count_rval)
    {
      rval = lval / 2;
      lval = (lval - 1) / 2;
    }
    else
    {
      lval = (rval - 1) / 2;
      rval = rval / 2;
    }
    cout << "Case #" << t << ": ";
    cout << rval << " " << lval <<endl;
  }
  return 0;
}
