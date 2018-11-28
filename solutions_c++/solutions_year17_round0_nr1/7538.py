#include <bits/stdc++.h>
using namespace std;

#define xx                   first
#define yy                   second
#define problem              void __()
#define REP(i, n)            FOR(i, 0, n - 1)
#define VEC(e, v)            for (auto &e: v)
#define FOR(i, a, b)         for (int i = a; i <= b; ++i)
#define ROF(i, a, b)         for (int i = a; i >= b; --i)
#define ios                  ios::sync_with_stdio(0), cin.tie(0)
#define all(x)               (x).begin(), (x).end()
#define num(x)               ((int)(x).size())
typedef pair<int, int>       pii;
typedef vector<int>          vi;
typedef long long            ll;
#define oo                   INT_MAX
#define pf                   printf
#define endl                 '\n'

////////////////////////////////////////////////////////////////////////////////

template<class A, class B> ostream& operator<<(ostream& os, const pair<A, B>& p)
  { return os << "(" << p.xx << ", " << p.yy << ")"; }

template<class I> ostream& __o(ostream& os, I a, I b) { os << "{";
  for (; a != b;) { os << *a++, cerr << (a == b ? "" : " "); }
  return os << "}"; }

template<class I> ostream& __d(ostream& os, I a, I b) { os << "{\n";
  for (I c = a; a != b; ++a) os << "  " << distance(c, a) << ": " << *a << endl;
  return os << "}"; }

template<class... T> void __e(T&&... a)
  { int t[] = {(cerr << forward<T>(a), 0)...}; (void)t; cerr << endl; }

#define OO(A) template<class... T> \
  ostream& operator<<(ostream& os, const A<T...>& x) { return __o(os, all(x)); }

OO(vector) OO(deque) OO(set) OO(multiset) OO(map) OO(multimap)

#define DD(x)   (cerr << #x ": ", __d(cerr, all(x)) << endl)
#define EE(...) (__e(__VA_ARGS__))

////////////////////////////////////////////////////////////////////////////////

int T;

problem {
    cin >> T; REP(t, T) {
        int K, R = 0;
        string S; vi P;
        
        cin >> S >> K;
        
        REP(i, num(S)) {
            if (S[i] == '+') P.push_back(1);
            else             P.push_back(0);
        }

        REP(i, num(S) - K + 1) {
            if (P[i] == 0) {
                REP(j, K) P[i + j] ^= 1;
                R++;
            }
        }

        //EE("---");
        int Y = 0; VEC(e, P) if (e == 0) Y++;

        if (Y == 0)
            pf("Case #%d: %d\n", t + 1, R);
        else
            pf("Case #%d: IMPOSSIBLE\n", t + 1);
    }
}

int main() { ios; __(); return 0; }
