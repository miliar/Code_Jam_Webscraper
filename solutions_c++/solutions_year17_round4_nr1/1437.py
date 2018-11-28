#include<bits/stdc++.h>
using namespace std;

int calc3(int a, int b) {

  if ( a >= b ) {
    return b+(a-b)/3+((a-b)%3==1 || (a-b)%3==2);
  } else {
    return a+(b-a)/3+((b-a)%3==1 || (b-a)%3==2);
  }

}

int calc4(int a, int b, int c) {
  int res = b/2;
  b = b % 2;
  if ( a >= c ) { // left 1
    res += c;
    a -= c;
    if ( b ) a += 2;
    res += a/4;
    if ( a % 4 ) res++;
  } else { // left 3
    res += a;
    c -= a;
    if ( b ) c++;
    res += c/4;
    if ( c % 4 ) res++;
  }
  return res;
}

int main() {
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int T;
  int n, p, r[5], res;
  cin >> T;
  for ( int t = 1 ; t <= T ; t++ ) {
    memset(r, 0, sizeof(r));
    res = 0;
    cin >> n >> p;
    for ( int i = 0 ; i < n ; i++ ) {
      int g;
      cin >> g;
      r[g%p]++;
    }
    res += r[0];
    if ( p == 2 ) {
      res += (r[1] + 1)/2;
    } else if ( p == 3 ) {
      res += calc3(r[1], r[2]);
    } else if ( p == 4 ) {
      res += calc4(r[1], r[2], r[3]);
    }
    printf("Case #%d: %d\n", t, res);
  }
}
