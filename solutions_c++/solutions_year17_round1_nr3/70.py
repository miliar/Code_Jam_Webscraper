#include <algorithm>
#include <iostream>
using namespace std;

inline long long numheals(int na, int Ak, int Hd, int curh) {
  na--;
  if (na*Ak < curh) return 0;
  if (Hd <= 2*Ak) return 1e18;
  na -= (curh-1)/Ak;
  long long hv = (Hd-Ak-1) / Ak;
  return (na+hv-1)/hv;
}

int main() {
  long long T, Hd, Ad, Hk, Ak, B, D, prob=1;
  for (cin >> T; T--;) {
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

    long long nb = 0, na = (Hk + Ad-1) / Ad;
    if (B) for (;;) {
      nb++;
      long long na2 = nb + (Hk + (Ad+nb*B-1)) / (Ad+nb*B);
      if (na2 > na) {nb--; break;}
      na = na2;
    }

    long long ret = 1e18, tot = na, curh = Hd;
    ret = min(ret, tot + numheals(na, Ak, Hd, curh));
    if (D) while (Ak > 0) {
      if (curh - (Ak-D) <= 0) {
        tot++;
        curh = Hd-Ak;
        if (curh <= 0 || curh - (Ak-D) <= 0) break;
      }
      tot++; Ak = max(0LL, Ak-D); curh -= Ak;
      ret = min(ret, tot + numheals(na, Ak, Hd, curh));
    }

    if (ret >= 1e18) {
      cout << "Case #" << prob++ << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << prob++ << ": " << ret << endl;
    }
  }
}
