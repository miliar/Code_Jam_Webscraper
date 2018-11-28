// {{{ written by skyly (using the template modified from shik)
#include <stdio.h>
#ifdef LOCAL_TEST
#include "stdc++.h"
#else
#include <bits/stdc++.h>
#endif
#include <unistd.h>
#define SZ(x) ((int)(x).size())
#define ALL(x) begin(x), end(x)
#define REP(i, n) for (int i = 0; i < int(n); ++i)
#define REP1(i, a, b) for (int i = (a); i <= int(b); ++i)
#define FOR(it, c) for (auto it = begin(c); it != end(c); ++it)
#define MP make_pair
#define PB push_back
using namespace std;

#ifdef LOCAL_TEST
template<typename T>
void _dump(const char* s, T&& head) { cerr << s << " = " << head << endl; }

template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c = 0;
    while (*s != ',' || c != 0) {
        if (*s == '(' || *s == '[' || *s == '{') ++c;
        if (*s == ')' || *s == ']' || *s == '}') --c;
        cerr << *s++;
    }
    cerr << " = " << head << ", ";
    _dump(s + 1, tail...);
}

#define dump(...) do { \
    fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
    _dump(#__VA_ARGS__, __VA_ARGS__); \
} while (false)

template<typename Iter>
ostream& _out(ostream &s, Iter b, Iter e) {
    s << "[";
    for (auto it = b; it != e; ++it) s << (it == b ? "" : " ") << *it;
    s << "]";
    return s;
}

template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A, B> &p) { return s << "(" << p.first << "," << p.second << ")"; }
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) { return _out(s, ALL(c)); }
template<typename T, size_t N>
ostream& operator <<(ostream &s, const array<T, N> &c) { return _out(s, ALL(c)); }
template<typename T>
ostream& operator <<(ostream &s, const set<T> &c) { return _out(s, ALL(c)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const map<A, B> &c) { return _out(s, ALL(c)); }
#else
#define dump(...)
#endif

#ifdef LOCAL_TEST
#define FILEIO(...)
#else
#define FILEIO(name) do { \
    freopen(name ".in", "r", stdin); \
    freopen(name ".out", "w", stdout); \
} while (false)
#endif

template<typename T>
void _RD(T &x) { cin >> x; }
void _RD(int &x) { scanf("%d", &x); }
void _RD(long &x) { scanf("%ld", &x); }
void _RD(long long int &x) { scanf("%" PRId64, &x); }
void _RD(double &x) { scanf("%lf", &x); }
void _RD(char &x) { scanf(" %c", &x); }
void _RD(char *x) { scanf("%s", x); }

void RD() {}
template<typename T, typename... U>
void RD(T& head, U&... tail) {
    _RD(head);
    RD(tail...);
}

template<typename T>
void _WR(const T &x) { cout << x; }
void _WR(const int &x) { printf("%d", x); }
void _WR(const long long int &x) { printf("%" PRId64, x); }
template<typename T>
void _WR(const vector<T> &x) {
    for (auto i = x.cbegin(); i != x.cend(); ++i) {
        if (i != x.cbegin()) putchar(' ');
        _WR(*i);
    }
}

void WR() {}
template<typename T, typename... U>
void WR(const T& head, const U&... tail) {
    _WR(head);
    putchar(sizeof...(tail) ? ' ' : '\n');
    WR(tail...);
}

using LL = long long int;
using PII = pair<int, int>;
using VI = vector<int>;

// }}}

void solve(const int case_id) {
    string s;
    int k;
    RD(s, k);

    int n = SZ(s);
    REP(i, n) {
        if (s[i] == '+') s[i] = 1;
        else s[i] = 0;
    }

    int ans = 0;
    REP(i, n) {
        if (i + k - 1 >= n) break;
        if (s[i] == 0) {
            ans++;
            REP(j, k) s[i + j] ^= 1;
        }
    }

    printf("Case #%d: ", case_id);
    if (count(ALL(s), 0) == 0) {
        printf("%d\n", ans);
    } else {
        printf("IMPOSSIBLE\n");
    }
}

int main() {
    int t;
    RD(t);
    REP(i, t) {
        solve(i + 1);
    }

    return 0;
}
