#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x) cerr << #x << " = " << x << endl
#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=(a); i<(b); i++)
#define _ << " " <<

typedef unsigned long long ll;
typedef pair<int, int> P;
#define X first
#define Y second

ll pot10[20];

ll check(ll n, ll dosad, int pot, int zn)
{
  REP(i, pot+1)
    dosad += pot10[i] * zn;
  return dosad <= n;
}

int main()
{
  pot10[0] = 1;
  FOR(i, 1, 20) pot10[i] = pot10[i-1] * 10;

  int brt;
  scanf("%d", &brt);

  FOR(br, 1, brt+1) {
    ll n;
    scanf("%lld", &n);

    ll rje = 0;
    for (int pot=18; pot>=0; pot--) {
      int da = 0;
      for (int j=9; j>=0; j--) {
	if (check(n, rje, pot, j)) {
	  da = 1;
	  rje += j * pot10[pot];
	  break;
	}
      }
      assert(da);
    }

    printf("Case #%d: %lld\n", br, rje);
  }

  return 0;
}
