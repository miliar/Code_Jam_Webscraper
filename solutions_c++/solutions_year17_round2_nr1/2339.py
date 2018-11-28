#include<bits/stdc++.h>

using namespace std;

#define ll long long int
#define pb push_back
#define f first
#define s second
#define mod 1e9+7
#define mp make_pair
#define PI 3.14159265
#define eps 0.000001

const int N = 1234567;

#define test
int main() {
  ios::sync_with_stdio(false); cin.tie(0);
#ifdef test
  freopen("a.in","rt",stdin);
  freopen("a.out","wt",stdout);
#endif
  int tt;
  cin >> tt;
  for(int ii = 1; ii <= tt; ii++) {
    cout << "Case #" << ii << ": ";
    double d, x, s, mt = 0.0;
    int n;
    cin >> d >> n;
    for(int i = 0; i < n; i++) {
      cin >> x >> s;
      mt = max(mt, ((d - x) / s));
    }
    printf("%.6f\n", d / mt);
  }
  return 0;
}