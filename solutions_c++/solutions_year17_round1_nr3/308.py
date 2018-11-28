// Author: Chi-Kit (George) LAM
#include <bits/stdc++.h>
using namespace std;
#define DEBUG_ENABLED 0
namespace jam{
  typedef long long LL;
  struct Jam {
    Jam(unsigned int seed) {
      srand(seed);
      cout.precision(9);
    }
  };
#if DEBUG_ENABLED
  #define DEBUG(...) \
    (cout << "DEBUG:" << __LINE__ << ": (" << #__VA_ARGS__ \
          << ") = " << make_tuple(__VA_ARGS__) << endl)
  template <size_t I, class... Types> struct TuplePrinter {
    void print(ostream& out, const tuple<Types...>& x) const {
      TuplePrinter<I-1, Types...>().print(out, x);
      out << ", " << get<I-1>(x);
    }
  };
  template <class... Types> struct TuplePrinter<1, Types...> {
    void print(ostream& out, const tuple<Types...>& x) const {
      out << get<0>(x);
    }
  };
  template <class... Types>
  ostream& operator<<(ostream& out, const tuple<Types...>& x) {
    out << "(";
    TuplePrinter<sizeof...(Types), Types...>().print(out, x);
    return out << ")";
  }
  template <class T1, class T2>
  ostream& operator<<(ostream& out, pair<T1, T2> x) {
    return out << tuple<T1, T2>(x);
  }
  template <class T, class Alloc>
  ostream& operator<<(ostream& out, const deque<T, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& v : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << v;
    }
    return out << "}";
  }
  template <class T, class Compare, class Alloc>
  ostream& operator<<(ostream& out, const set<T, Compare, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& v : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << v;
    }
    return out << "}";

  }
  template <class Key, class T, class Compare, class Alloc>
  ostream& operator<<(ostream& out, const map<Key, T, Compare, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& kv : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << kv->first << ": " << kv->second;
    }
    return out << "}";
  }
#else
  #define DEBUG(...)
#endif
} // namespace jam
using namespace jam;
Jam JAM(/*seed*/ 0);

LL Hd, Ad, Hk, Ak, B, D;

LL f(LL d, LL b) {
  LL hd = Hd, ad = Ad, hk = Hk, ak = Ak;
  for (int count = 1; count <= 800; ++count) {
    DEBUG(hd, ad, hk, ak);
    if (d > 0) {
      if (hd <= ak-D) {
        // Cure
        hd = Hd;
      } else {
        --d;
        ak = max(ak-D, 0LL);
      }
      hd -= ak;
      if (hd <= 0) {
        return 1LL << 40;
      }
    } else if (b > 0) {
      if (hd <= ak) {
        // Cure
        hd = Hd;
      } else {
        --b;
        ad += B;
      }
      hd -= ak;
      if (hd <= 0) {
        return 1LL << 40;
      }
    } else {
      if (hd <= ak && hk > ad) {
        // Cure
        hd = Hd;
      } else {
        hk -= ad;
        if (hk <= 0) {
          return count;
        }
      }
      hd -= ak;
      if (hd <= 0) {
        return 1LL << 40;
      }
    }
  }
  return 1LL << 40;
}

void solve(int T) {
  cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
  
  //f(0,1);
  LL ans = 1LL << 40;
  for (LL d = 0; d<=110; ++d) {
    for (LL b = 0; b<=110; ++b) {
      ans = min(f(d, b), ans);
      if (ans < 1LL << 40) {
        DEBUG(d, b);
      }
    }
  }

  if (ans < 1LL << 40) {
    cout << "Case #" << T << ": " << ans << endl;
  } else {
    cout << "Case #" << T << ": IMPOSSIBLE" << endl;
  }
}
int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
