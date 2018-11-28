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

ld Pole(ld r) {
  return M_PI * r * r;
}

ld Obwod(ld r) {
  return 2 * M_PI * r;
}

int H[nax];
int R[nax];

ld pole[nax];
ld bok[nax];

ld przyp() {
  int n, k;
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; i++) {
    scanf("%d%d", &R[i], &H[i]);
    pole[i] = Pole(R[i]);
    bok[i] = Obwod(R[i]) * H[i];
  }
  ld wyn = 0;
  for (int i = 1; i <= n; i++) {
    ld tmp = pole[i] + bok[i];
    vector<ld> naj;
    for (int j = 1; j <= n; j++) {
      if (i != j) {
        naj.push_back(bok[j]);
      }
    }
    sort(naj.rbegin(), naj.rend());
    for (int j = 0; j + 1 < k; j++) {
      tmp += naj[j];
    }
    wyn = max(wyn, tmp);
  }
  return wyn;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: %.9Lf\n", i, przyp());
  }
  return 0;
}
