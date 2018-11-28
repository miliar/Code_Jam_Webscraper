#include <bits/stdc++.h>
#define FOR(i,a,b) for (int i=a; i <=b ; i++)
#define FO(i,a,b) for (int i=a; i < b ; i++)
#define FORD(i,a,b) for (int i=a; i >=b ; i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define SET(arr,c) memset(arr,c,sizeof(arr))
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define PI 2 * acos(0.0)
#define debug cout << "#PASS" << endl;
#define sqr(x) (x) * (x)
#define cube(x) (x) * (x) * (x)
using namespace std;

template <class T> int getbit(int i, T X) { return (X & (1<<(i-1))); }
template <class T> T onbit(int i, T X) { return (X | (1<<(i-1))); }
template <class T> T offbit(int i, T X) { return (X | (1<<(i-1)) - (1<<(i-1))); }
template <class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template <class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

int dx[4]={0, 0, -1, 1};
int dy[4]={-1, 1, 0, 0};

typedef pair <ll, ll> II;
typedef pair <int, II> III;

const int inf = 1e9;
const ll linf = 1e18;
const int maxn = 20;
const int MOD = 1e9 + 7;


/***********VAR***********/
int R, C;
string a[100];
/*************************/

void enter() {
    cin >> R >> C;
    FOR(i, 1, R) {
        cin >> a[i];
        a[i] = '0' + a[i];
    }
}

void solve() {

    string pat = "";
    FOR(i, 1, C) pat += '?';
    a[0] = pat;

    FOR(i, 1, R) {
        char last = '?';
        FOR(j, 1, C) if (a[i][j] != '?') {
            last = a[i][j];
            FORD(k, j - 1, 1) {
                if (a[i][k] == '?') {
                    a[i][k] = a[i][j];
                }
                else break;
            }
        }
        FORD(j, C, 1) if (a[i][j] == '?') a[i][j] = last;
        else break;
        if ((last == '?') && (a[i - 1] != pat)) a[i] = a[i - 1];
    }

    FORD(i, R - 1, 1) {
        char last = '?';
        FOR(j, 1, C) if (a[i][j] != '?') {
            last = a[i][j];
            FORD(k, j - 1, 1) {
                if (a[i][k] == '?') {
                    a[i][k] = a[i][j];
                }
                else break;
            }
        }
        FORD(j, C, 1) if (a[i][j] == '?') a[i][j] = last;
        else break;
        if ((last == '?') && (a[i + 1] != pat)) a[i] = a[i + 1];
    }

    FOR(i, 1, R) {
        FOR(j, 1, C) cout << a[i][j];
        cout << endl;
    }
}
int main() {

    #ifndef ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int test;
    cin >> test;
    FOR(t, 1, test) {
        enter();
        cout << "Case #" << t << ":" << endl;
        solve();
    }
    return 0;
}

