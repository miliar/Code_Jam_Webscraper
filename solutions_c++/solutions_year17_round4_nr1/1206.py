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

int n, k;
int a[maxn];
int dem[10];

void solve(){
    memset(dem,0,sizeof(dem));
    FOR(i,1,n) dem[a[i]%k]++;
    int ans = 0;

    if(k == 2){
        ans += dem[0];
        ans += (dem[1]+1)/2;
    }
    else if(k == 3){
        ans += dem[0];
        int tmp = min(dem[1], dem[2]);
        ans += tmp;
        dem[1] -= tmp;
        dem[2] -= tmp;
        ans += (dem[1]+2)/3 + (dem[2]+2)/3;
    }
    else if(k == 4){
        ans += dem[0];
        ans += dem[2]/2;
        ans += min(dem[1], dem[3]);
        int d1 = max(dem[1], dem[3]) - min(dem[1], dem[3]);
        int d2 = dem[2] % 2;
        if(d2 == 0) ans += (d1+3)/4;
        else{
            ans += (d1+5)/4;
        }
    }
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
        cin >> n >> k;
        FOR(i,1,n) cin >> a[i];

        cout << "Case #" << test << ": ";
        solve();
    }



    return 0;
}
