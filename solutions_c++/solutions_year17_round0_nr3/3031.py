#include <bits/stdc++.h>

using namespace std;

int T, cs;
long long n, k, h, mod, base;

int main()
{
  freopen("C-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  cin >> T;
  while(T--){
    cin >> n >> k;
    h = 1;
    long long tmp = n;
    while(h < k){
      n -= h;
      k -= h;
      h <<= 1;
    }
    base = n / h;
    mod = n % h;
    cout << "Case #" << ++cs << ": ";
    cout << (base + (k <= mod)) / 2 << " " << (base - 1 + (k <= mod)) / 2 << "\n";
  }
  return 0;
}
