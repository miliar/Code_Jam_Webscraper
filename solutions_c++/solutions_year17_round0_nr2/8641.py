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

LL n;
int test;

bool is_satify(int n) {
    vector<int> a;
    while (n>0) {
        a.push_back(n % 10);
        n /= 10;
    }
    int last = 9;
    FO(i, 0, sz(a)) {
        if (a[i] <= last) {
            last = a[i];
        }   else {
            return 0;
        }
    }
    return 1;
}

int main()
{
    freopen("b-large.in","r",stdin);
    freopen("b_large.out","w",stdout);

    cin >> test;
    int nTest = 1;
    while (test > 0) {
        test--;
        cin >> n;
        cout << "Case #" << nTest++ << ": ";
        vector<int> a, b;
        int last = -1;
        while (n>0) {
            int tmp = n%10;
            if (last == tmp) {
                b[sz(b)-1] ++;
            }   else {
                a.push_back(tmp);
                b.push_back(1);
                last = tmp;
            }
            n/=10;
        }
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());

        bool printed = false;
        FO (i, 1, sz(a)) {
            if (a[i] < a[i-1]) {
                //decrease
                // print before
                FO (j, 0, i-1) {
                    while (b[j]--) cout << a[j];
                }
                // print middle
                if (a[i-1] > 1) {
                    cout << a[i-1] - 1;
                }
                b[i-1]--;
                while (b[i-1]--) {
                    cout << 9;
                }
                // print after
                FO (j, i, sz(a)) {
                    while (b[j]> 0) {
                        cout << 9;
                        b[j]--;
                    }
                }
                printed = true;
                break;
            }
        }
        if (!printed) {
            FO (i, 0, sz(a))
                FO (j, 0, b[i]) cout << a[i];
        }
        cout << endl;
    }
    return 0;
}