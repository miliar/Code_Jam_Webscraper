// Author: Chi-Kit (George) LAM
#include <bits/stdc++.h>
using namespace std;
#define DEBUG_ENABLED 1
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

void solve(int T) {
  int m, n, p;
  cin >> m >> n;
  char A[25][25];
  for (int i=0; i<m; ++i) {
    for (int j=0; j<n; ++j) {
      cin >> A[i][j];
      if (A[i][j] != '?') {
        p = i;
      }
    }
  }
  
  for (int i=p; i>=0; --i) {
    int k = 0;
    while (k < n && A[i][k] == '?') {
      ++k;
    }
    for (int j=0; j<n; ++j) {
      if (A[i][j] == '?') {
        if (k < n) {
          A[i][j] = A[i][k];
        } else {
          A[i][j] = A[i+1][j];
        }
      } else {
        k = j;
      }
    }
  }
  
  for (int i=p+1; i<m; ++i) {
    for (int j=0; j<n; ++j) {
      A[i][j] = A[i-1][j];
    }
  }
  
  cout << "Case #" << T << ":" << endl;
  for (int i=0; i<m; ++i) {
    for (int j=0; j<n; ++j) {
      cout << A[i][j];
    }
    cout << endl;
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
