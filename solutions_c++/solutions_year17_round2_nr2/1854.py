#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <deque>
#include <bitset>
#include <cctype>
#include <utility>

#define ULL unsigned long long
#define LL long long
#define FOR(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define FO(i,a,b) for(int i = (a); i < (int)(b); i++)
#define FORD(i,a,b) for(int i= (a); i >= (int)(b); i--)
#define FOD(i,a,b) for(int i= (a); i > (int)(b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define SET(a,c) memset(a, c, sizeof(a))
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define eps 1e-5
#define infi 1e9
#define PI 2*acos(0.0)
#define debug(k,F,n) FOR(i,1,n){FOR(j,1,n) cout << setw(k) << F[i][j]  ; cout << endl;}
using namespace std;

typedef pair<int,int>II;
typedef pair<int,II>PII;
typedef vector<int> VI;
typedef vector<II> VII;
typedef set<int> SI;
typedef map<string,int> MSI;
typedef map<int,int> MII;

template<class T> T gcd(T a, T b) {
    T r;
    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}
template<class T> T lcm(T a, T b) {
    return a / gcd(a, b) * b;
}
template<class T> T sqr(T x) {
    return x * x;
}
template<class T> T cube(T x) {
    return x * x * x;
}
template<class T> int getbit(T s, int i) {
    return (s >> i) & 1;
}
template<class T> T onbit(T s, int i) {
    return s | (T(1) << i);
}
template<class T> T offbit(T s, int i) {
    return s & (~(T(1) << i));
}
template<class T> T togglebit(T s, int i) {
    return s ^ (T(1) << i);
}
template<class T> int cntbit(T s) {
    return s == 0 ? 0 : cntbit(s >> 1) + (s & 1);
}
#define maxn  305
#define MOD 1000000005

int test, nTest = 0;
int n, r, o, y, g, b, v;
int deg[10];
int Free[1005], x[1005];
bool found;
int a[10], ori[10];

struct myclass {
  bool operator() (pair<int,int> a,pair<int,int> b) {
      if (a.second > b.second) {
        return true;
      }
      if (a.second == b.second) {
        return ori[a.first] > ori[b.first];
      }
      return false;
  }
} myobject;

void attempt(int i, int a[]) {
//    cout << i <<  endl;
//    FOR (j,1,n) cout << x[j]; cout << endl;
//    FOR (j,1,n) cout << a[j];
//    cout << endl;

    if (found) return;

    // chon dinh bat ki
    if (i == n+1) {
        //kiem tra voi x[1]
        if (x[1] != x[n]) {
            found = true;
            printf("Case #%d: ", ++nTest);
            FOR (j,1,n) {
                switch (x[j]) {
                case 1:
                    cout << 'R';
                    break;
                case 2:
                    cout << 'O';
                    break;
                case 3:
                    cout << 'Y';
                    break;
                case 4:
                    cout << 'G';
                    break;
                case 5:
                    cout << 'B';
                    break;
                case 6:
                    cout << 'V';
                    break;
                }
            }
            cout << endl;
        }
        return;
    }
    // chon dinh co so luong nhieu nhat
    vector<pair<int,int> > v;
    FOR (j,1,6) {
        if ((j != x[i-1]) && (a[j]>0)) {
            v.push_back(mp(j, a[j]));
        }
    }
    sort(v.begin(), v.end(), myobject);

    FO (j,0,v.size()) {
            x[i] = v[j].first;
            a[v[j].first]--;
            attempt(i+1, a);
            return;
            //a[v[j].first]++;
    }


//    FOR (j,1,6) {
//        if (j != x[i-1] && a[j]>0) {
//            x[i] = j;
//            a[j]--;
//            attempt(i+1, a);
//            if (found) return;
//            a[j]++;
//        }
//    }
}

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> test;
    int tt = 0;
    while (test--) {
        tt++;
        //cout << tt << endl;
        cin >> n >> r >> o >> y >> g >> b >> v;
        deg[1] = o + y + g + b + v;
        deg[2] = r + y + g + b + v;
        deg[3] = r + o + g + b + v;
        deg[4] = r + o + y + b + v;
        deg[5] = r + o + y + g + v;
        deg[5] = r + o + y + g + b;
        bool impos = false;
        FOR (i,1,5)
            if ((double)deg[i] < (double)n/2.0) {
                printf("Case #%d: IMPOSSIBLE\n", ++nTest);
                impos = true;
                break;
            }
        if (impos) {
            continue;
        }

        // init
        found = false;
        a[0] = 0;
        a[1] = r;
        a[2] = o;
        a[3] = y;
        a[4] = g;
        a[5] = b;
        a[6] = v;
        FOR (i,1,6) ori[i] = a[i];

        int max_j = 1;
        FOR (i,2,6)
            if (a[i] >  a[max_j]) {
                max_j = i;
            }

//        FOR (i,2,6) {
//            if (a[i] > 0) {
//                a[i]--;
//                x[1] = i;
//                attempt(2, a);
//                break;
//            }
//        }
        a[max_j]--;
        x[1] = max_j;
        attempt(2, a);
        if (found == false) {
                printf("Case #%d: IMPOSSIBLE\n", ++nTest);
        }

    }
    return 0;
}
