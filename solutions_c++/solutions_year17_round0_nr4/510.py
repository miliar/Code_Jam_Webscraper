#include <string.h>
#include <vector>
#include <map>
#include <list>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <sstream>

#define _USE_MATH_DEFINES

#include <math.h>

#define pb(a) push_back(a)
#define sz size()
#define ALL(a) a.begin(),a.end()
#define mp(a, b) make_pair(a,b)

typedef long long ll;
typedef long double ld;

template<typename T>
inline void SWAP(T &a, T &b) {
    T tmp = a;
    a = b;
    b = tmp;
}

template<typename T>
inline T ABS(const T &val) {
    return val < 0 ? -val : val;
}

template<typename T>
inline T MAX(const T &a, const T &b) {
    return a > b ? a : b;
}

template<typename T>
inline T MIN(const T &a, const T &b) {
    return a < b ? a : b;
}

#define MSET(d) memset(d,0,sizeof(d))
#define forn(i, n) for(int i=0;i!=n;i++)
#define for1(i, n) for(int i=1;i<=n;i++)
#define forab(i, a, b) for(int i=a;i!=b;i++)
#define for1ab(i, a, b) for(int i=a+1;i<=b;i++)
#define fordab(i, a, b) for(int i=b-1;i>=a;i--)
#define ford1ab(i, a, b) for(int i=b;i!=a;i--)
#define ford(i, n) for(int i=n-1;i!=-1;i--)
#define ford1(i, n) for(int i=n;i!=0;i--)

const int INTinf = 2147483647;
const int nINTinf = 0 - 2147483648;
#define LLinf 9223372036854775807

using namespace std;
typedef pair<int, int> pii;

const int MAX_CNT = 100;
char a[MAX_CNT][MAX_CNT];
//char start[MAX_CNT][MAX_CNT];

bool d1[MAX_CNT * 2 - 1], d2[MAX_CNT * 2 - 1];
bool col[MAX_CNT], row[MAX_CNT];
// '+'=1,'x'=2,'0'=3
char out_c[] = {'.', '+', 'x', 'o'};

void put(char c, int x, int y, int n) {

    if (c != '+') {
//        if (col[y] || row[x]) {
//            cout << "ERROR" << endl;
//        }
        col[y] = 1;
        row[x] = 1;
    }
    if (c != 'x') {
//        if (d1[x + y] || d2[x - y + n - 1]) {
//            cout << "ERROR" << endl;
//        }
        d1[x + y] = 1;
        d2[x - y + n - 1] = 1;
    }
    a[x][y] = c;
}

int getNom(char c) {
    switch (c) {
        case 'x':
            return 2;
        case '+':
            return 1;
        case 'o':
            return 3;
        default:
            return 0;
    }
}

int main() {
//    D-small-attempt0.in
    freopen("D-small-attempt1.in", "r", stdin);
    int t;
    cin >> t;
    for1(p, t) {
        cout << "CASE #" << p << ": ";
        int n, k;
        cin >> n >> k;
        memset(&a[0][0], '.', sizeof(a));
        memset(&d1[0], false, sizeof(d1));
        memset(&d2[0], false, sizeof(d2));
        memset(&col[0], false, sizeof(col));
        memset(&row[0], false, sizeof(row));
        forn(i, k) {
            char c;
            int x, y;
            cin >> c >> x >> y;
//            cout << c << x << y << endl;
            put(c, x - 1, y - 1, n);
        }
//        memcpy(&start[0][0], &a[0][0], sizeof(a));
        vector<pii> vc;
        int sum = 0;
        {
            int x = 0;
            forn(y, n) {
                bool pl = col[y] | row[x];
                bool di = d1[x + y] | d2[x - y + n - 1];
                int val = getNom(a[x][y]);

                val |= (1 - pl) * 2 + (1 - di);
                char smb = '.';
                switch (val) {
                    case 3:
                        smb = 'o';
                        break;
                    case 2:
                        smb = 'x';
                        break;
                    case 1:
                        smb = '+';
                        break;
                }

                if (smb != a[x][y]) {
                    put(smb, x, y, n);
                    vc.pb(pii(x, y));
                }
            }
        }

        forab(x, 1, n) {
            forn(y, n) {
                bool pl = col[y] | row[x];
                bool di = d1[x + y] | d2[x - y + n - 1];
                int val = getNom(a[x][y]);

                val |= (1 - pl) * 2;
                char smb = '.';
                if (val == 3) {
                    val = 2;
                }
                switch (val) {
                    case 3:
                        smb = 'o';
                        break;
                    case 2:
                        smb = 'x';
                        break;
                    case 1:
                        smb = '+';
                        break;
                }

                if (smb != a[x][y]) {
                    put(smb, x, y, n);
                    vc.pb(pii(x, y));
                }
            }
        }

        ford(x, n) {
            forn(y, n) {
                bool pl = col[y] | row[x];
                bool di = d1[x + y] | d2[x - y + n - 1];
                int val = getNom(a[x][y]);

                val |= (1 - di);
                char smb = '.';
                switch (val) {
                    case 3:
                        smb = 'o';
                        break;
                    case 2:
                        smb = 'x';
                        break;
                    case 1:
                        smb = '+';
                        break;
                }
                sum += (val + 1) / 2;

                if (smb != a[x][y]) {
                    put(smb, x, y, n);
                    vc.pb(pii(x, y));
                }
            }
        }

        sort(ALL(vc));
        vc.erase(unique(ALL(vc)), vc.end());
        cout << sum << ' ' << vc.sz << endl;
        forn(i, vc.sz) {
            cout << a[vc[i].first][vc[i].second] << ' ' << vc[i].first + 1 << ' ' << vc[i].second + 1 << endl;
        }

    }

    return 0;
}