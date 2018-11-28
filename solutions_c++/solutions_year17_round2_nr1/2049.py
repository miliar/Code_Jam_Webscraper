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
LL d, n;
LL k[1005], s[1005];
double t[1005];
double res;

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> test;
    while (test--) {
        cin >>d >> n;
        double max_t = -1;
        FOR (i,1,n) {
            cin >> k[i] >> s[i];
            max_t = max(max_t, (double)(d-k[i]) / (double)s[i]);
        }
        res = (double) d / max_t;
        printf("Case #%d: %0.6f\n", ++nTest, res);
        //cout << tN << " " << tN/n << endl;
    }
    return 0;
}
