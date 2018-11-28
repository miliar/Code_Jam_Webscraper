#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

int ok(long long n)
{
  string s = to_string(n);
  for (int i=s.length()-1; i>=0; --i)
  {
    for (int j=i-1; j>=0; --j)
      if (s[i] < s[j])
        return i;
  }
  return 0;
}

long long work(long long n)
{
  long long res = n;
  long long base = 10;
  while (ok(res) > 0)
  {
    res = n/base*base-1;
    base *= 10;
  }
  return res;
}

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int T;
  cin >> T;
  for (int i=1; i<=T; ++i)
  {
    long long n;
    cin >> n;
    cout << "Case #" << i << ": ";
    cout << work(n) << endl;
  }
}
