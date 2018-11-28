#include <bits/stdc++.h>

using namespace std;

#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef LOCAL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair < b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
    *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

using ll = long long;
using ld = long double;

constexpr int nax = 1000 * 1000 + 105;
constexpr int infty = 1000 * 1000 * 1000 + 5;
constexpr int mod = 1000 * 1000 * 1000 + 7;

int n, k;
ll p[nax];

ll Wczytaj() {
  ll n = 0;
  char c;
  scanf(" %c", &c);
  n = c - '0';
  while (true) {
    scanf("%c", &c);
    if (c == '.') break;
    else n = (n * 10) + c - '0';
  }
  for (int i = 0; i < 4; i++) {
    scanf("%c", &c);
    n = n * 10 + c - '0';
  }
  return n;
}

ld przyp() {
  scanf("%d%d", &n, &k);
  debug() << imie(n) << imie(k);
  ll u = Wczytaj();
  for (int i = 0; i < n; i++) {
    p[i] = Wczytaj();
  }
  if (k != n) return -1;
  while (true) {
    int licz = 0;
    ll najm_val = 10000;
    ll dru_najm = 10000;
    for (int i = 0; i < n; i++) {
      if (p[i] < najm_val) {
        licz = 1;
        dru_najm = najm_val;
        najm_val = p[i];
      } else if (p[i] == najm_val) {
        licz++;
      } else if (p[i] < dru_najm) {
        dru_najm = p[i];
      }
    }
    const ll potrzeba = (dru_najm - najm_val) * licz;
    debug() << imie(najm_val) << imie(dru_najm) << imie(licz) << imie(potrzeba) << imie(u);
    if (najm_val == 10000 || potrzeba > u) {
      ld wynik = 1;
      for (int i = 0; i < n; i++) {
        ld tmp_p = p[i];
        if (p[i] == najm_val) {
          tmp_p = p[i] + (ld) u / licz;
        }
        wynik *= tmp_p / 10000;
      }
      return wynik;
    }
    for (int i = 0; i < n; i++) {
      if (p[i] == najm_val) {
        p[i] = dru_najm;
        u -= dru_najm - najm_val;
      }
    }
    assert(u >= 0);
  }
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: %.6Lf\n", i, przyp());
  }
  return 0;
}
