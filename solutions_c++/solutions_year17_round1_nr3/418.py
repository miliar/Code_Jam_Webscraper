#include<bits/stdc++.h>
using namespace std;
#define FOR(i,n,...) for (int i = 1 , ##__VA_ARGS__ ; i <= n ; ++i)
#define REP(i,s,n,...) for (int i = s , ##__VA_ARGS__ ; i <= n ; ++i)
#define ll long long
#define LL long long
#define calc1(x) ((x)+1+(hk-1)/((x)*b+ad))
int hd, ad, hk, ak, b, d , hnow;
int kill_cnt;
int calc2 () {
  int kc = kill_cnt , res = 0 ;
  if ((kill_cnt - 1) * ak < hnow) return kill_cnt;
  else {
    res += (hnow - 1) / ak;
    kc -= (hnow - 1) / ak;
  }
  //  cerr << res << ' ' << kc << ' ' << (hd-1)/ak << '/';
  return res + kc + ((hd - 1) / ak > 1 ? (kc - 1) / ((hd - 1) / ak - 1) : 0x3f3f3f3f);
}

int pai () {
  int res = 0x3f3f3f3f;
  for (int a = 0 ; a <= 200 ; ++a)
    for (int b = a ; b <= 200 ; ++b) {
        int hd = ::hd , ad = ::ad , hk = ::hk , ak = ::ak , hnow = hd , cnt = 0 ;
        FOR(i,200) {
          if (cnt >= 2000) break;
          if (i <= a) {
            if (hnow <= ak - d) --i,hnow = hd;
            else ak -= d;
          }
          else if (i <= b) {
            if (hnow <= ak) --i ,hnow = hd;
            else ad += ::b;
          }
          else {
            if (hnow <= ak && hk > ad) --i, hnow = hd;
            else hk -= ad;
          }
          ++cnt;
          if (hk <= 0) break;
          hnow -= ak;
        }
        res = min(res,cnt);
      }
  return res;
}

int main (void) {
  int T ; cin >> T ; FOR(Cas, T) {
    printf("Case #%d: ",Cas);

    cin >> hd >> ad >> hk >> ak >> b >> d;
    if ((ak - d >= hd && hk > ad) ||            \
        (ak * 2 - d * 3 >= hd && hk > ad * 2 && hk > ad + b)) {
      cout << "IMPOSSIBLE" << endl;
    }
    else {
      cout << pai() << endl;/*
      int l = 0 , r = b == 0 ? 0 : 1 + (hk - 1 - ad) / b;
      REP(i,l,r) if (calc1(i) < calc1(l)) l = i;
      kill_cnt = calc1(l);
      l = 0 ; r = d == 0 ? 0 : 1 + (ak - 1) / d;
      bool flag = false;
      hnow = hd;
      int ans = 0x3f3f3f3f , cnt = 0;
      REP(i,l,r) {
        if (calc2() + cnt < ans) {
          ans = calc2() + cnt;
          //          cerr << i << ' ' << calc2() + cnt << endl;
        }
        if (ak - d < hnow) {ak -= d; flag = false;}
        else {
          --i; hnow = hd;
          if (flag) break;
          else flag = true;
        }
        hnow -= ak;
        ++cnt;
      }
      cout << ans << endl;*/
    }
  }
  return 0;
}
