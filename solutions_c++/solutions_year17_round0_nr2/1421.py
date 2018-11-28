#include <bits/stdc++.h>
using namespace std;

long long f[20][10];

long long calc(long long n)
{
  int digits[20], len = 0;
  while (n)
  {
    digits[++len] = n % 10;
    n /= 10;
  }

  long long res = 0;
  int minDigit = 1, good = 1;
  for (int i = 1; i < len; i++)
    for (int j = 1; j <= 9; j++)
      res += f[i][j];

  for (int i = len; i; i--)
  {
    for (int j = minDigit; j < digits[i]; j++)
      res += f[i][j];
    if (digits[i] >= minDigit) minDigit = digits[i];
    else 
    {
      good = 0;
      break;
    }
  }
  res += good;
  return res;
}

int main()
{
  for (int i = 1; i <= 9; i++)
    f[1][i] = 1;
  for (int i = 2; i <= 18; i++)
    for (int j = 1; j <= 9; j++)
      for (int k = j; k <= 9; k++)
        f[i][j] += f[i - 1][k];

  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    long long n;
    cin >> n;
    long long cnt = calc(n), low = 2, high = n, ans = 1;
    while (low <= high)
    {
      long long mid = (low + high) / 2;
      if (calc(mid) < cnt) low = mid + 1;
      else 
      {
        ans = mid;
        high = mid - 1;
      }
    }
    cout << "Case #" << iTest << ": " << ans << endl;
  }
}