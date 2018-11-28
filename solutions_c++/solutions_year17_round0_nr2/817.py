#include <bits/stdc++.h>

using namespace std;

long long c(long long x, long long y) {
  long long ret = 1;
  for (long long i = 0; i < y; ++i) {
    ret = ret * (x - i) / (i + 1);
  }
  return ret;
}

long long calc(long long n) {
  int a[30];
  for (a[0] = 0; n; a[++a[0]] = n % 10, n /= 10);
  long long ret = 0;
  for (int i = 1; i < a[0]; ++i) {
    ret += c(i + 8, 8);
  }
  a[a[0] + 1] = 1;
  for (int i = a[0]; i; --i) {
    if (a[i] < a[i + 1]) {
      return ret;
    }
    for (int j = a[i + 1]; j < a[i]; ++j) {
      ret += c(i + 8 - j, 9 - j);
    }
  }
  return ret + 1;
}

long long solve(long long n) {
  int a[30];
  for (a[0] = 0; n; a[++a[0]] = n % 10, n /= 10);
  a[a[0] + 1] = 20;
  for (int i = a[0]; i > 1; --i) {
    if (a[i] > a[i - 1]) {
      for (int j = i + 1; j <= a[0] + 1; ++j) {
        if (a[j] != a[i]) {
          --a[j - 1];
          for (int k = 1; k < j - 1; ++k) {
            a[k] = 9;
          }
          break;
        }
      }
      break;
    }
  }
  long long ret = 0;
  for (int i = a[0]; i; --i) {
    ret = ret * 10 + a[i];
  }
  return ret;
}

long long search(long long n) {
  long long l = 0, r = n, std = calc(n);
  while (l + 1 < r) {
    long long mid = (l + r) >> 1;
    if (calc(mid) < std) {
      l = mid;
    } else {
      r = mid;
    }
  }
  assert(r == solve(n));
  return r;
}

int main() {
  calc(35);
  long long test, n;
  cin >> test;
  for (int ca = 1; ca <= test; ++ca) {
    cin >> n;
    cout << "Case #" << ca << ": " << search(n) << endl;
  }
  return 0;
}
