/*
СТРОИМ СТЕНУ РАБОТЯГИ!
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═█
█═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
*/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <numeric>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <cmath>
#include <bitset>
#include <cassert>
#include <queue>
#include <stack>
#include <deque>
 
  
  
using namespace std;
  
  
template<typename T1, typename T2>inline void chkmin(T1 &x, T2 y) { if (x > y) x = y; }
template<typename T1, typename T2>inline void chkmax(T1 &x, T2 y) { if (x < y) x = y; }
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
    if (pos == len) {
        pos = 0, len = fread(buf, 1, buf_size, stdin);
    }
    if (pos == len) {
        return -1;
    }
    return buf[pos++];
}
  
inline int readChar() {
    int c = getChar();
    while (c <= 32) {
        c = getChar();
    }
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
  
inline void writeWord( const char *s ) {     while (*s)
writeChar(*s++); }
  
struct Flusher {
    ~Flusher() {
        if (write_pos)
            fwrite(write_buf, 1, write_pos, stdout), write_pos = 0;
    }
} flusher;
  
using namespace std;


#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define left left228
#define right right228
#define next next228
#define rank rank228
#define prev prev228
const int MAXN = 1002;


int t;
int d;
int k[MAXN], s[MAXN];
vector<pair<int, int> > g;


bool good(long double x) {
    vector<pair<long double, int> > gt;
    for (auto xx: g) {
        gt.push_back(make_pair((long double)(xx.first), xx.second));
    }
    long double curpos = 0.0;
    while (sz(gt)) {
        long double curp = 1e12;
        int where = -1;
        for (int i = 0; i < sz(gt) - 1; i++) {
            if (gt[i + 1].second < gt[i].second) {
                long double time = (gt[i + 1].first - gt[i].first) / (gt[i].second - gt[i + 1].second);
                if (curp > time) {
                    curp = time;
                    where = i;
                }
            }
        }
       // cout << curp << endl;
        if (where == -1) {
            if (gt[0].second >= x) {
                return 1;
            }
            //cout << gt[0].first << ' ' << gt[0].second << endl;
            long double time = (gt[0].first - curpos) / (x - gt[0].second);
            if (time >= (d - curpos) / x) {
                return 1;
            }
            return 0;
        }
        if (gt[0].second >= x) {
            if ((d - curpos) / x <= curp) {
                return 1;
            }
            curpos += x * curp;
            vector<pair<long double, int> > gt1;
            for (int i = 0; i < sz(gt); i++) {
                if (where == i) {
                    continue;
                }
                gt1.push_back(make_pair(gt[i].first + gt[i].second * curp, gt[i].second));
            }
            gt = gt1;
            continue;
        }
        long double time = (gt[0].first - curpos) / (x - gt[0].second);
        if (time > curp) {
            curpos += x * curp;
            vector<pair<long double, int> > gt1;
            for (int i = 0; i < sz(gt); i++) {
                if (where == i) {
                    continue;
                }
                gt1.push_back(make_pair(gt[i].first + gt[i].second * curp, gt[i].second));
            }
            gt = gt1;
            continue;
        }
        if (time >= (d - curpos) / x) {
            return 1;
        }
        return 0;
    }
    return 1;
}
 

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int it = 1; it <= t; it++) {
        int n;
        cin >> d >> n;
        g.clear();
        for (int i = 0; i < n; i++) {
            cin >> k[i] >> s[i];
            g.push_back(make_pair(k[i], s[i]));
        }
        sort(all(g));
        long double l = 1.0;
        long double r = 1e18;
        for (int i = 0; i < 300; i++) {
            long double mid = (l + r) / 2.0;
           // cout << mid << ' ' << good(mid) << endl;
            if (good(mid)) {
                l = mid; 
            } else {
                r = mid;
            }
        }
        printf("Case #%d: %.10lf\n", it, (double)l);
    }
    return 0;
}
