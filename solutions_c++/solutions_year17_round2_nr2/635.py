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

int n, R, O, Y, G, B, V;
int a[1005], b[1005], xet[maxn];

string process(){
    string ans = "", tmp = "";
    int pre = b[3]-(b[1]-b[2]);
    FOR(i,1,pre) ans += "123";
    FOR(i,1,b[2]-pre) ans += "12";
    FOR(i,1,b[1]-b[2]) ans += "13";
    return ans;
    //cout << ans << endl;
}

int cmp(int i, int j){
    return a[i] > a[j];
}

void solve(){
    if(R > Y+B || Y > R+B || B > R+Y){
       cout << "IMPOSSIBLE" << endl;
       return;
    }
    vector<int> id = { 0, 1, 2, 3, 4, 5 };
    sort(id.begin(), id.end(), cmp);


    vector<int> ans;
    int x = id[0];
    int y = id[1];
    int z = id[2];
    for (int i = 0; i < a[x]; ++i) {
        ans.pb(x);
        if (i < a[y]) ans.pb(y);
        if (i >= a[x] - a[z]) ans.pb(z);
    }
    string s = "ROYGBV";
    for (int i = 0; i < n; ++i)  cout << s[ans[i]];
    cout << endl;
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
        cin >> n;
        FOR(i,0,5) cin >> a[i];
        R = a[0];
        Y = a[2];
        B = a[4];
        cout << "Case #" << test << ": ";
        solve();
    }



    return 0;
}
