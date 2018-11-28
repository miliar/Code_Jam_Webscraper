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
bool can[MAXN][MAXN][MAXN][3][3];


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int it = 1; it <= t; it++) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        for (int cntr = 0; cntr <= r; cntr++) {
            for (int cntb = 0; cntb <= b; cntb++) {
                for (int cnty = 0; cnty <= y; cnty++) {
                    for (int last = 0; last < 3; last++) {
                        for (int f = 0; f < 3; f++) {
                            can[cntr][cntb][cnty][last][f] = 0;
                            if (last == 0 && cntr == 0) {
                                continue;
                            }
                            if (last == 1 && cntb == 0) {
                                continue;
                            }
                            if (last == 2 && cnty == 0) {
                                continue;
                            }
                            if (f == 0 && cntr == 0) {
                                continue;
                            }
                            if (f == 1 && cntb == 0) {
                                continue;
                            }
                            if (f == 2 && cnty == 0) {
                                continue;
                            }
                            if (cntr + cntb + cnty == 1) {
                                can[cntr][cntb][cnty][last][f] = 1;
                                continue;
                            }
                            int ncntr = cntr;
                            int ncntb = cntb;
                            int ncnty = cnty;
                            if (last == 0) {
                                ncntr--;
                            } else {
                                if (last == 1) {
                                    ncntb--;
                                } else {
                                    if (last == 2) {
                                        ncnty--;
                                    }
                                }
                            }
                            for (int plast = 0; plast < 3; plast++) {
                                if (last == plast) {
                                    continue;
                                }
                                if (can[ncntr][ncntb][ncnty][plast][f]) {
                                    can[cntr][cntb][cnty][last][f] = 1;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
        int last, fs;
        last = -1;
        for (int j = 0; j < 3; j++) {
            for (int f = 0; f < 3; f++) {
                if (f == j) {
                    continue;
                }
                if (can[r][b][y][j][f]) {
                    last = j;
                    fs = f;
                    break;
                }
            }
        }
        if (last == -1) {
            printf("Case #%d: IMPOSSIBLE\n", it);
            continue;
        }
        string ans;
        while (r + b + y > 0) {
            if (last == 0) {
                r--;
                ans += 'R';
            } else {
                if (last == 1) {
                    b--;
                    ans += 'B';
                } else {
                    if (last == 2) {
                        y--;
                        ans += 'Y';
                    }
                }
            }
            for (int plast = 0; plast < 3; plast++) {
                if (last == plast) {
                    continue;
                }
                if (can[r][b][y][plast][fs]) {
                    last = plast;
                    break;
                }
            }
        } 
        reverse(all(ans));
        cout << "Case #" << it << ": ";
        cout << ans << '\n';
    }
    return 0;
}
