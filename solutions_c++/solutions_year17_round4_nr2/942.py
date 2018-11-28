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
const int MAXN = 1001;




inline void kek(int it) {
    writeWord("Case #");
    writeInt(it, ':');
    writeChar(' ');
}

int n, c, m;
vector<pair<int, int> > t;
vector<int> v[MAXN];
bool was[MAXN][MAXN];
bool used[MAXN][MAXN];
int cnt;


bool get(int x) {
    cnt = 0;
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < n; j++) {
            was[i][j] = 0;
        }
        for (int j = 0; j < c; j++) {
            used[i][j] = 0;
        }
    }
    for (auto y: t) {
        bool good = 0;
        for (int i = 0; i < x; i++) {
            if (!used[i][y.second]) {
                if (!was[i][y.first]) {
                    good = 1;
                    was[i][y.first] = 1;
                    used[i][y.second] = 1;
                    break;
                }
            }
        }
        if (good) {
            continue;
        }
        for (int i = 0; i < x; i++) {
            if (!used[i][y.second]) {
                for (int t = 0; t < y.first; t++) {
                    if (!was[i][t]) {
                        good = 1;
                        was[i][t] = 1;
                        used[i][y.second] = 1;
                        cnt++;
                        break;
                    }
                }
                if (good) {
                    break;
                }
            }
        }
        if (!good) {
            return 0;
        }
    }
    return 1;
}



int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ts = readInt();
    for (int it = 1; it <= ts; it++) {
        n = readInt(), c = readInt(), m = readInt();
        for (int i = 0; i < c; i++) {
            v[i].clear();
        }
        t.clear();
        for (int i = 0; i < m; i++) {
            int p = readInt(), b = readInt();
            v[b - 1].push_back(p - 1);
            t.push_back(make_pair(p - 1, b - 1));
        }   
        sort(all(t));
        int l = 0;
        for (int i = 0; i < c; i++) {
            l = max(l, sz(v[i]));
        }
        int r = m;
        while (l != r) {
            int mid = (l + r) >> 1;
            if (get(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        get(l);
        kek(it);
        writeInt(l, ' ');
        writeInt(cnt, '\n');
    }
    return 0;
}

