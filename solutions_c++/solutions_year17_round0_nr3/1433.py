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
ll N, K;

/*************************/

void div(ll n, ll &a, ll &b) {
    if (n <= 1) {
        a = 0;
        b = 0;
        return ;
    }

    if (n % 2) {
        a = b = n / 2;
    }
    else {
        b = n / 2;
        a = n - 1 - b;
    }
}

void solve() {
    ll a, b;
    div(N, a, b);
    if (K == 1) {
        cout << max(a, b) << " " << min(a, b) << endl;
        return ;
    }
    ll cnt0 = 1, _cnt0, _cnt1;
    ll cnt1 = 1;
    ll pw = 2;
    ll Count = 3;
    ll number;
    while (1) {
        //cout << a << " " << b << " " << cnt0 << " " << cnt1 << endl;
        if (K <= Count) {
            ll pre = Count - pw;
            ll index = K - pre;
            if (index <= cnt1) number = b;
            else number = a;
            break;
        }
        else {
            if (a != b) {
                ll m;
                if (a % 2) {
                    m = b;
                    div(m, a, b);
                    _cnt0 = cnt0 * 2 + cnt1;
                    _cnt1 = cnt1;
                    cnt0 = _cnt0;
                    cnt1 = _cnt1;
                }
                else {
                    m = a;
                    div(m, a, b);
                    _cnt0 = cnt0;
                    _cnt1 = cnt1 * 2 + cnt0;
                    cnt0 = _cnt0;
                    cnt1 = _cnt1;
                }
            }
            else {
                // cout << "pass" << endl;
                ll m;
                m = a;
                div(m, a, b);
                _cnt0 = cnt0 + cnt1;
                _cnt1 = _cnt0;
                cnt0 = _cnt0;
                cnt1 = _cnt1;
            }

        }
        pw *= 2;
        Count += pw;
    }
    div(number, a, b);
    cout << max(a, b) << " " << min(a, b) << endl;
}

int main() {
    //freopen("C-large.in", "r", stdin);
    // freopen("test.in", "r", stdin);
    //freopen("test.out", "w", stdout);
    int test;
    cin >> test;
    FOR(t, 1, test) {
        cin >> N >> K;
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

