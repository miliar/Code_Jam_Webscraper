#include <bits/stdc++.h>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl

using namespace std;

typedef pair<double,double>point;
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcount(s);}
template<class T> T gcd(T a, T b){ T r; while (b != 0) { r = a % b; a = b; b = r; } return a;}

const long double PI = 2*acos(0.0);
const long double eps = 1e-15;
const int infi = 1e9;
const LL Linfi = 1e18;
const LL MOD = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 100005

int n, D;
int K[1005], S[1005];


void solve(){
    double t = 0;
    FOR(i,1,n){
        t = max(t, 1.0*(D-K[i])/S[i]);
    }
    FOR(i,1,n) FOR(j,i+1,n) if(S[i] != S[j]){
        double tmp = -1.0*(K[i]-K[j]) / (S[i]-S[j]);
        double giao = K[i] + tmp*S[i];
        if(giao < D){
            tmp += 1.0*(D-giao) / min(S[i], S[j]);
            t = max(t, tmp);
        }
    }
    double ans = 1.0*D/t;
    cout << fixed << setprecision(9);
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int sotest;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> D >> n;
        FOR(i,1,n) cin >> K[i] >> S[i];
        cout << "Case #" << test << ": ";
        solve();
    }



    return 0;
}
