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

typedef long long ll;
typedef pair<int, int> P;
#define X first
#define Y second

int main()
{
  int brt;
  scanf("%d", &brt);

  REP(tt, brt) {
    int len, n;
    scanf("%d%d", &len, &n);

    double rje = 0;
    REP(i, n) {
      int poz, v;
      scanf("%d%d", &poz, &v);
      rje = max(rje, (len - poz) / (double) v);
    }

    rje = len / rje;
    printf("Case #%d: %.10lf\n", tt+1, rje);
  }

  return 0;
}
