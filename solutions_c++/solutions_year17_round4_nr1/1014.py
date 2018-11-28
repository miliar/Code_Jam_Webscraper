/*
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▐▐▐▐▐▐░░░░░░░
░░░░░░░░░░▐▐▌▌▌▌▌▌▐▐░░░░░
░░░░░░░░░▐▌▌▌▌▌▌▌▌▌▌▐░░░░
░░░░░░░░▐░░▌◐░▌▌▌◐░░░▐░░░
░░░░░░░░▐░░░░░░░░░░░░▐░░░  
░░░░░░░░▐░░░░░▐░░░░░░▐░░░
░░░░░░░░░▐░░░▐▐▐░░░░░▐░░░
░░░░░░░░░▐░░░░░░░░░░▐░░░░
░░░░░░░░░░▐░░████░░▐░░░░░
запускаем░░▐░░░░░░░▐░░░░░
░░░░Влада░░▐░░░░░░▐░░░░░░
░░░Макеева░░▐░░░░▐░░░░░░░
░░░░░░░░░░░░░▐▐▐▐░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░
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
  
  
#define sz(c) (int)(c).size()
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define left left228
#define right right228
#define next next228
#define rank rank228
#define prev prev228
const int MAXN = 101;


int n, p;
int g[MAXN];
int cnt[4];


inline void kek(int it) {
    writeWord("Case #");
    writeInt(it, ':');
    writeChar(' ');
}


int dp[MAXN][MAXN][MAXN][4];
int dp1[MAXN][MAXN][3];


int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = readInt();
    for (int it = 1; it <= t; it++) {
        n = readInt(), p = readInt();
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; i++) {
            g[i] = readInt();
            g[i] %= p;
            cnt[g[i]]++; 
        }
        if (p == 2) {
            kek(it);
            writeInt(cnt[0] + (cnt[1] + 1) / 2, '\n');
            continue;
        }   
        if (p == 3) {
            kek(it);
            for (int t = 0; t <= cnt[1]; t++){
                for (int t1 = 0; t1 <= cnt[2]; t1++) {
                    for (int ost = 0; ost <= 2; ost++) {
                        dp1[t][t1][ost] = 0;
                    }
                }
            }
            dp1[0][0][0] = cnt[0];
            for (int t = 0; t <= cnt[1]; t++){
                for (int t1 = 0; t1 <= cnt[2]; t1++) {
                    for (int ost = 0; ost <= 2; ost++) {
                        if (t) {
                            int prost = (ost - 1 + 3) % 3;
                            chkmax(dp1[t][t1][ost], dp1[t - 1][t1][prost] + (prost == 0));
                        }
                        if (t1) {
                            int prost = (ost - 2 + 3) % 3;
                            chkmax(dp1[t][t1][ost], dp1[t][t1 - 1][prost] + (prost == 0));
                        }
                    }   
                }
            } 
            int ans = 0;
            for (int ost = 0; ost <= 2; ost++) {
                chkmax(ans, dp1[cnt[1]][cnt[2]][ost]);
            }
            writeInt(ans, '\n');
            continue;
        }
        if (p == 4) {
            kek(it);
            for (int t = 0; t <= cnt[1]; t++){
                for (int t1 = 0; t1 <= cnt[2]; t1++) {
                    for (int t2 = 0; t2 <= cnt[3]; t2++) {
                        for (int ost = 0; ost <= 3; ost++) {
                            dp[t][t1][t2][ost] = 0;
                        }
                    }
                }
            }
            dp[0][0][0][0] = cnt[0];
            for (int t = 0; t <= cnt[1]; t++){
                for (int t1 = 0; t1 <= cnt[2]; t1++) {
                    for (int t2 = 0; t2 <= cnt[3]; t2++) {
                        for (int ost = 0; ost <= 3; ost++) {
                            if (t) {
                                int prost = (ost - 1 + 4) % 4;
                                chkmax(dp[t][t1][t2][ost], dp[t - 1][t1][t2][prost] + (prost == 0));
                            }
                            if (t1) {
                                int prost = (ost - 2 + 4) % 4;
                                chkmax(dp[t][t1][t2][ost], dp[t][t1 - 1][t2][prost] + (prost == 0));
                            }
                            if (t2) {
                                int prost = (ost - 3 + 4) % 4;
                                chkmax(dp[t][t1][t2][ost], dp[t][t1][t2 - 1][prost] + (prost == 0));
                            }
                        }   
                    }
                }
            } 
            int ans = 0;
            for (int ost = 0; ost <= 3; ost++) {
                chkmax(ans, dp[cnt[1]][cnt[2]][cnt[3]][ost]);
            }
            writeInt(ans, '\n');
        }
    }
    return 0;
}

