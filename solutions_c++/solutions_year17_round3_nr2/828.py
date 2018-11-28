#include <bits/stdc++.h>
#define REP(x, n) for (int x = 0; x < (int)(n); x++)
#define RREP(x, n) for (int x = (int)(n)-1; x >= 0; --x)
#define FOR(x, m, n) for (int x = (int)m; x < (int)(n); x++)
#define EACH(itr, cont) \
  for (typeof((cont).begin()) itr = (cont).begin(); itr != (cont).end(); ++itr)
#define ALL(X) (X).begin(), (X).end()
#define mem0(X) memset((X), 0, sizeof(X))
#define mem1(X) memset((X), 255, sizeof(X))

using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

int doStuff() {
  int Ac, Aj, result = 0, ic = 0, ij = 0, lib = 0, t = 0;
  int sumC = 0, sumJ = 0;
  char now = 'X', first = 'X';
  scanf("%d %d", &Ac, &Aj);
  vector<PII> Xc(Ac), Xj(Aj);
  vector<int> free;
  REP(i, Ac) scanf("%d %d", &Xc[i].first, &Xc[i].second);
  REP(i, Aj) scanf("%d %d", &Xj[i].first, &Xj[i].second);
  sort(ALL(Xc)), sort(ALL(Xj));
  while (ic < Ac && ij < Aj) {
    if (Xc[ic].first < Xj[ij].first) {
      if (now == 'X')
        first = 'C', t = Xc[ic].first;
      else if (now == 'C')
        free.push_back(Xc[ic].first - t);
      else
        lib += Xc[ic].first - t, ++result;
      // fprintf(stderr, "Cameron %d to %d\n", t, Xc[ic].second);
      sumC += Xc[ic].second - t, t = Xc[ic].second, ic++, now = 'C';
    } else {
      if (now == 'X')
        first = 'J', t = Xj[ij].first;
      else if (now == 'J')
        free.push_back(Xj[ij].first - t);
      else
        lib += Xj[ij].first - t, ++result;
      // fprintf(stderr, "Jamal %d to %d\n", t, Xj[ij].second);
      sumJ += Xj[ij].second - t, t = Xj[ij].second, ij++, now = 'J';
    }
  }
  while (ic < Ac) {
    if (now == 'X')
      first = 'C', t = Xc[ic].first;
    else if (now == 'C')
      free.push_back(Xc[ic].first - t);
    else
      lib += Xc[ic].first - t, ++result;
    // fprintf(stderr, "Cameron %d to %d\n", t, Xc[ic].second);
    sumC += Xc[ic].second - t, t = Xc[ic].second, ic++, now = 'C';
  }
  while (ij < Aj) {
    if (now == 'X')
      first = 'J', t = Xj[ij].first;
    else if (now == 'J')
      free.push_back(Xj[ij].first - t);
    else
      lib += Xj[ij].first - t, ++result;
    // fprintf(stderr, "Jamal %d to %d\n", t, Xj[ij].second);
    sumJ += Xj[ij].second - t, t = Xj[ij].second, ij++, now = 'J';
  }
  int dif;
  if (now == first) {
    if (now == 'J') {
      dif = 1440 - t + Xj[0].first;
      sumJ += dif;
    } else {
      dif = 1440 - t + Xc[0].first;
      sumC += dif;
    }
    free.push_back(dif);
  } else {
    if (now == 'J') {
      dif = 1440 - t + Xc[0].first;
      sumC += dif;
    } else {
      dif = 1440 - t + Xj[0].first;
      sumJ += dif;
    }
    lib += dif, ++result;
  }
  int need = abs(720 - sumJ);
  fprintf(stderr, "SumJ %d SumC %d\n", sumJ, sumC);
  fprintf(stderr, "Need %d Liberty %d\n", need, lib);
  assert(sumJ + sumC == 1440);
  if (need <= lib) return result;
  need -= lib;
  sort(ALL(free));
  int idx = free.size() - 1;
  while (need > 0) {
    assert(idx > -1);
    result += 2;
    need -= free[idx];
    --idx;
  }
  return result;
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d: %d\n", t + 1, doStuff());
  return 0;
}