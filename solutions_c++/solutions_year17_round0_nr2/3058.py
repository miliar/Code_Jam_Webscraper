#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cstring>
#include <cmath>
#include <climits>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <bitset>
#include <ctime>
#include <iomanip>

using namespace std;

//#define I64_IO

#define ARGS_NUM(...) ARGS_NUM_IMPL_((0,__VA_ARGS__,5,4,3,2,1))
#define ARGS_NUM_IMPL_(arg) ARGS_NUM_IMPL arg
#define ARGS_NUM_IMPL(_0,_1,_2,_3,_4,_5, N,...) N
#define FUNC_CALL(func, ...) FUNC_CALL_NUM(func, ARGS_NUM(__VA_ARGS__))
#define FUNC_CALL_NUM(func, args) FUNC_CALL_NUM_(func, args)
#define FUNC_CALL_NUM_(func, args) FUNC_CALL_NUM__(func, args)
#define FUNC_CALL_NUM__(func, args) func ## args


// i/o defines
#define read_int1(v) scanf("%d", &v)
#define read_int2(v1, v2) scanf("%d%d", &v1, &v2)
#define read_int3(v1, v2, v3) scanf("%d%d%d", &v1, &v2, &v3)
#define read_int4(v1, v2, v3, v4) scanf("%d%d%d%d", &v1, &v2, &v3, &v4)
#define read_int(...) FUNC_CALL(read_int, __VA_ARGS__)(__VA_ARGS__)
#ifdef I64_IO
#define read_ll1(v) scanf(MODE ? "%lld" : "%I64d", &v)
#define read_ll2(v1, v2) scanf(MODE ? "%lld%lld" : "%I64d%I64d", &v1, &v2)
#define read_ll3(v1, v2, v3) scanf(MODE ? "%lld%lld%lld" : "%I64d%I64d%I64d", &v1, &v2, &v3)
#define read_ll4(v1, v2, v3, v4) scanf(MODE ?"%lld%lld%lld%lld" : "%I64d%I64d%I64d%I64d", &v1, &v2, &v3, &v4)
#define print_ll(v) printf(MODE ? "%lld" : "%I64d", v)
#else
#define read_ll1(v) scanf( "%lld" , &v)
#define read_ll2(v1, v2) scanf( "%lld%lld" , &v1, &v2)
#define read_ll3(v1, v2, v3) scanf( "%lld%lld%lld" , &v1, &v2, &v3)
#define read_ll4(v1, v2, v3, v4) scanf("%lld%lld%lld%lld", &v1, &v2, &v3, &v4)
#define print_ll(v) printf("%lld" , v)
#endif
#define read_ll(...) FUNC_CALL(read_ll, __VA_ARGS__)(__VA_ARGS__)
#define read_str(v) scanf("%s", v)
#define print_str(v) printf("%s", v)
#define read_f(v) scanf("%f", &v)
#define print_f(v, prec) printf("%.*f", prec, v)
#define read_lf1(v) scanf("%lf", &v)
#define read_lf2(v1, v2) scanf("%lf%lf", &v1, &v2)
#define read_lf3(v1, v2, v3) scanf("%lf%lf%lf", &v1, &v2, &v3)
#define read_lf(...) FUNC_CALL(read_lf, __VA_ARGS__)(__VA_ARGS__)
#define print_lf(v, prec) printf("%.*lf", prec, v)
#define print_int(v) printf("%d", v)

//short defines
#define ll long long
#define ull unsigned long long
#define uchar unsigned char
#define pi 3.141592653589793238462643383279
#define eps (1e-8)
#define minn(a, b) a = min((a), (b))
#define maxx(a, b) a = max((a), (b))
#define all(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define ln putchar('\n')
#define space putchar(' ')
#define pii pair <int, int>
#define pll pair <ll,ll>


// debug defines
#define PRINT1(a) cout << #a << " = " << (a) << "\n"
#define PRINT2(a,b) cout << #a << " = " << (a) << "," << #b << " = " << (b) << "\n"
#define PRINT3(a,b,c) cout << #a << " = " << (a) << "," << #b << " = " << (b) << "," << #c << " = " << (c) << "\n"
#define PRINT4(a,b,c,d) cout << #a << " = " << (a) << "," << #b << " = " << (b) << "," << #c << " = " << (c) << "," << #d << " = " << (d) << "\n"
#ifdef VELTER
#define PRINT(...) FUNC_CALL(PRINT, __VA_ARGS__)(__VA_ARGS__)
#define BP break_point()
#define LINE printf("-------------------------------\n")
#define LOG(...) printf(__VA_ARGS__)
#else
#define PRINT(...) ;
#define BP ;
#define LINE ;
#define LOG(...) ;
#endif


// useful functions
int break_point(){ char c; while ((c = getchar()) != '\n'); return 0; }
template <typename T> void read_integer(T &r){ bool sign = 0; r = 0; char c; while (1){ c = getchar(); if (c == '-'){ sign = 1; break; }if (c != ' ' && c != '\n'){ r = c - '0'; break; } }while (1){ c = getchar(); if (c == ' ' || c == '\n')break; r = r * 10 + (c - '0'); }if (sign)r = -r; }
ll binpow(ll a, ll b){ll ret = 1;while(b){if(b & 1)ret = ret * a;a *= a;b >>= 1;}return ret;}
ll binpow(ll a, ll b, int mod){ll ret = 1;while(b){if(b & 1)ret = (ret * a) % mod;a = (a * a) % mod;b >>= 1;}return ret;}
inline int getbit(int x, int b){ return (x >> b) & 1; }
inline int setbit(int x, int b){ return x | (1 << b); }
inline void _setbit(int &x, int b){ x = setbit(x, b); }
inline ll setbit(ll x, int b){ return x | (1ll << b); }
inline void _setbit(ll &x, int b){ x = setbit(x, b); }
inline int unsetbit(int x, int b){ return x & (INT_MAX - (1 << b)); }
inline void _unsetbit(int &x, int b){ x = unsetbit(x, b); }
inline int countbit(int x){ x = x - ((x >> 1) & 0x55555555); x = (x & 0x33333333) + ((x >> 2) & 0x33333333); return ((x + (x >> 4) & 0xF0F0F0F) * 0x1010101) >> 24; }
inline ll countbit(ll x){ return countbit(int(x & INT_MAX)) + countbit(int(x >> 32) & INT_MAX); }
inline void printbit(int x, int len){ for (int i = len - 1; i >= 0; i--) print_int(getbit(x, i)); }
int gcd(int a, int b){ return b == 0 ? a : gcd(b, a%b); }
ll gcd(ll a, ll b){ return b == 0 ? a : gcd(b, a%b); }

template <typename A, typename B> ostream& operator<<(ostream& stream, const pair <A, B> &p){ stream << "{" << p.first << "," << p.second << "}"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const vector <A> &v){ stream << "["; for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " "; stream << "]"; return stream; }
template <typename A, typename B> ostream& operator<<(ostream &stream, const map <A, B> &v){ stream << "["; for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " "; stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const set <A> &v){ stream << "["; for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " "; stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const stack <A> &v){ stack <A> st = v; stream << "["; while (!st.empty()){ stream << st.top() << " "; st.pop(); }stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const priority_queue <A> &v){ priority_queue <A> q = v; stream << "["; while (!q.empty()){ stream << q.top() << " "; q.pop(); }stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const queue <A> &v){queue <A> q = v;stream << "[";while (!q.empty()){stream << q.front() << " ";q.pop();}stream << "]";return stream;}
template <typename A> ostream& operator<<(ostream &stream, const deque <A> &v){deque <A> q = v;stream << "[";while (!q.empty()){stream << q.front() << " ";q.pop_front();}stream << "]";return stream;}


void run();

//#define FILES "distance3"

int main()
{
    srand(time(NULL));
#ifdef FILES
    freopen(FILES".in", "r", stdin);
    freopen(FILES".out", "w", stdout);
#endif
#ifdef MULTITEST
    do
    {
#endif
        run();
#ifdef MULTITEST
        LINE;
        LINE;
    } while (MODE);
#endif
    return 0;
}

#define time sgdtoe
#define tm sdofrhg
#define x1 dgjd
#define y1 dsgtjm
#define up fsdghj

//----------------------------------
//----------------------------------

const int mod = 0;
const int N = 0;

ll n;
ll res;

void go(ll x, int len)
{
    if(x > n)
        return;
    maxx(res, x);
    if(len < 18)
    {
        int d = x % 10;
        for(int i = max(1, d); i <= 9; ++i)
            go(x * 10 + i, len + 1);
    }
}

ll solve(ll num)
{
    n = num;
    res = 0;
    go(0, 0);
    return res;
}

void run()
{
    int T;
    read_int(T);
    for(int test = 1; test <= T; ++test)
    {
        ll num;
        read_ll(num);
        ll ans = solve(num);
        printf("Case #%d: ", test);
        print_ll(ans);ln;
    }
}
