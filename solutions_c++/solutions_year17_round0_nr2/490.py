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

int main() {
//    freopen("input.txt", "r", stdin);
    int t;
    cin >> t;
    string s;

    for1(x, t) {
        cout << "Case #" << x << ": ";
        cin >> s;
        int k = s.sz;
        fordab(i, 1, s.sz) {
            if (s[i - 1] > s[i]) {
                --s[i - 1];
                k = i;
            }
        }
        forab(i, k, s.sz) {
            s[i] = '9';
        }
        k = 0;
        while (k < s.sz && s[k] == '0') {
            ++k;
        }
        if (k == s.sz) {
            --k;
        }
        forab(i, k, s.sz) {
            cout << s[i];
        }
        cout << endl;
    }
    return 0;
}