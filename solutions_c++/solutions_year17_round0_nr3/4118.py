/*
*/
//#include "/Users/priya/Desktop/competitiveProgrammingDocuments/VP/Header.h"
#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
//using namespace __gnu_pbds;
//freopen ("/Users/priya/Desktop/B-small-attempt1.in","r",stdin);
//freopen ("/Users/priya/Desktop/B-small-attempt1.out","w",stdout);
using namespace std;
#define ll long long int
#define ull unsigned long long
#define ul unsigned long
#define ld long double  //LF
#define ios ios::sync_with_stdio(false);cin.tie(NULL);
#define X first
#define Y second
#define pb push_back
#define eps 1e-4
#define PI acos(-1.0)
#define inf 1e18 //9999999999 //1e14 //1e18
#define printarray(a,n)   for(ll i=1;i<=n;i++) cout<<a[i]<<" ";
#define DBN1(a)           cerr<<#a<<"="<<(a)<<"\n"
#define DBN2(a,b)         cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<"\n"
#define DBN3(a,b,c)       cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<", "<<#c<<"="<<(c)<<"\n"
#define DBN4(a,b,c,d)     cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<", "<<#c<<"="<<(c)<<", "<<#d<<"="<<(d)<<"\n"
#define DBN5(a,b,c,d,e)   cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<", "<<#c<<"="<<(c)<<", "<<#d<<"="<<(d)<<", "<<#e<<"="<<(e)<<"\n"
#define DBN6(a,b,c,d,e,f) cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<", "<<#c<<"="<<(c)<<", "<<#d<<"="<<(d)<<", "<<#e<<"="<<(e)<<", "<<#f<<"="<<(f)<<"\n"
#define DA(a,n) cerr<<#a<<"=["; printarray(a,n); cerr<<"]\n"
#define mid(l, r) 	       ((l + r) >> 1)
#define all(a)             a.begin(),a.end()
#define FOR(i,a,b) for(ll i=a;i<b;i++)

/** Interface */

inline int readChar();
template <class T = int> inline T readInt();
template <class T> inline void writeInt( T x, char end = 0 );
inline void writeChar( int x );
inline void writeWord( const char *s );

/** Read */

static const int buf_size = 4096;

inline int getChar() {
    static char buf[buf_size];
    static int len = 0, pos = 0;
    if (pos == len)
        pos = 0, len = fread(buf, 1, buf_size, stdin);
    if (pos == len)
        return -1;
    return buf[pos++];
}

inline int readChar() {
    int c = getChar();
    while (c <= 32)
        c = getChar();
    return c;
}

template <class T>
inline T readInt() {
    int s = 1, c = readChar();
    T x = 0;
    if (c == '-')
        s = -1, c = getChar();
    while ('0' <= c && c <= '9')
        x = x * 10 + c - '0', c = getChar();
    return s == 1 ? x : -x;
}

/** Write */

static int write_pos = 0;
static char write_buf[buf_size];

inline void writeChar( int x ) {
    if (write_pos == buf_size)
        fwrite(write_buf, 1, buf_size, stdout), write_pos = 0;
    write_buf[write_pos++] = x;
}

template <class T>
inline void writeInt( T x, char end ) {
    if (x < 0)
        writeChar('-'), x = -x;
    
    char s[24];
    int n = 0;
    while (x || !n)
        s[n++] = '0' + x % 10, x /= 10;
    while (n--)
        writeChar(s[n]);
    if (end)
        writeChar(end);
}

inline void writeWord( const char *s ) {
    while (*s)
        writeChar(*s++);
}

struct Flusher {
    ~Flusher() {
        if (write_pos)
            fwrite(write_buf, 1, write_pos, stdout), write_pos = 0;
    }
} flusher;
//ll some_primes[10] = {100271, 500179, 1000003, 2000227, 5000321, 98765431}
//ll some_primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199};
const int INF = 0x3ffffff;
const int N = 1000200;
const int mod = 1000000007;
//const int MAX = 100000128;
//const int MAX1 = 200;
//const int MAXN = 10000;
//const int maxN = 10000;
//const int C = 1000000000;
//const int MOD = 1000000009;
const int SN = 1 << 18;
//pow(n,floor(log(x)/log(n)) -> smallest power of n than given number
ll tt;
ll n;
ll k;
int main(){
    freopen ("/Users/priya/Desktop/C-small-2-attempt0.in","r",stdin);
    freopen ("/Users/priya/Desktop/C-small-2-attempt0.txt","w",stdout);
    cin >> tt;
    for(ll t = 1; t <= tt; t ++){
        cout << "Case #" << t << ": ";
        cin >> n >> k;
        set< ll > st;
        map< ll , ll > mp;
        ll lo , hi;
        st.insert(n);
        mp[n] = 1;
        for(ll i = 1; i <= k; i ++){
            ll val = *(--(st.end()));
            mp[val] --;
            if(mp[val] == 0) st.erase(val);
            if(val & 1){
                lo = (val - 1) / 2;
                hi = (val - 1) / 2;
                st.insert(lo);
                mp[lo] += 2;
            }
            else{
                lo = val / 2;
                hi = val / 2 - 1;
                st.insert(lo);
                st.insert(hi);
                mp[lo] ++;
                mp[hi] ++;
            }
        }
        cout << lo << " " << hi << endl;
    }
    return 0;
}
