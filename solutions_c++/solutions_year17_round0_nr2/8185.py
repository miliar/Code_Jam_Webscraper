#include <bits/stdc++.h>

using namespace std;
int t;
long long n;
bool check(long long n) {
  int prev = 10;
  while (n) {
    long long dig = n % 10;
    if (dig > prev) return false;
    prev = dig;
    n /= 10;
  }
  return true;
}
long long fun(long long n) {
  vector<long long> a;
  while (n) {
    long long dig = n % 10;
    a.push_back(dig);
    n/=10;
  }
  reverse(a.begin(), a.end());
  long long res = 0;
  for (int i = 0; i < a.size(); ++i) {
    long long tmp = 0;
    if (a[i] == 0) continue;
    else {
      for (int j = 0; j < i; ++j) tmp = tmp * 10 + a[j];
      tmp = tmp * 10 + a[i]-1;
      for (int j = i+1; j < a.size(); ++j)
        tmp = tmp * 10 + 9;
      if (check(tmp))
      res = max(tmp, res);
    }
  }
  return res;
}
int main()
{
  cin >> t;
  for (int test= 1; test <=t ;++test) {
    cin >> n;
    cout << "Case #" << test << ": ";
    if (check(n)) cout << n << endl;
    else cout << fun(n) << endl;
  }
  return 0;
}
