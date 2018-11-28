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

void doStuff() {
  string s;
  cin >> s;
  fprintf(stderr, "STARTING: %s\n", s.c_str());
  LL result = 0;
  bool good = true;
  REP(i,s.length()){
    if (i > 0 && s[i - 1] > s[i]) {
      good = false;
      break;
    } else if (i > 0 && s[i - 1] == s[i])
      continue;
    string aux = s;
    aux[i] -= 1;
    FOR(j,i+1,aux.length())aux[j]='9';
    fprintf(stderr, "%s\n", aux.c_str());
    result = max(result, stoll(aux));
  }
  if (good) result = stoll(s);
  printf("%lld\n", result);
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d: ", t + 1), doStuff();
  return 0;
}