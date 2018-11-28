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

int przyp() {
  int Ac, Aj;
  scanf("%d%d", &Ac, &Aj);
  vector<pair<pair<int, int>, int>> prz;
  int roznica = 0;
  for (int i = 0; i < Ac + Aj; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    const int znak = (i < Ac) ? 1 : -1;
    roznica += (b - a) * znak;
    prz.emplace_back(make_pair(a, b), znak);
  }
  sort(prz.begin(), prz.end());
  int zapas = 0;
  vector<int> czesci[2];
  int wynik = 0;
  prz.emplace_back(make_pair(prz[0].first.first + 24 * 60,
                   prz[0].first.second + 24 *60), prz[0].second);
  for (int i = 1; i < (int) prz.size(); i++) {
    const int dlu = prz[i].first.first - prz[i - 1].first.second;
    if (prz[i - 1].second == prz[i].second) {
      czesci[prz[i].second < 0].push_back(dlu);
    } else {
      zapas += dlu;
      wynik++;
    }
  }
  debug() << imie(roznica) << imie(zapas) << imie(wynik) << imie(czesci[0]) << imie(czesci[1]);
  for (int i = 0; i < 2; i++) {
    const int z = (i == 0) ? 1 : -1;
    sort(czesci[i].begin(), czesci[i].end());
    for (int c : czesci[i]) {
      roznica += c * z;
    }
  }
  while (abs(roznica) > zapas) {
    int kto = (roznica < 0) ? 1 : 0;
    const int z = (kto == 0) ? 1 : -1;
    assert(!czesci[kto].empty());
    const int c = czesci[kto].back();
    czesci[kto].pop_back();
    roznica -= z * c;
    zapas += c;
    wynik += 2;
  }
  return wynik;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: %d\n", i, przyp());
  }
  return 0;
}
