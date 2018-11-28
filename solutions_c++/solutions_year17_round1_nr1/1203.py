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

typedef pair<int,int>II;
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

int n, m;
string s[30], t[30];

void solve(){
    t[0] = "";
    FOR(j,0,m) t[0] += '0';
    t[n+1] = t[0];
    FOR(i,1,n) t[i] = s[i];
    FOR(i,1,n) FOR(j,1,m) if(s[i][j] != '?'){
        /// di ngang
        int L = j, R = j;
        FOR(k,j+1,m) {
            if(s[i][k] == '?') R = k;
            else break;
        }
        FORD(k,j-1,1) {
            if(s[i][k] == '?') L = k;
            else break;
        }
        //if(i == 3 && j == 4) cout << L << " " << R << endl;
        FOR(k,L,R) t[i][k] = s[i][j];
    }

    FOR(i,2,n) FOR(j,1,m) if(t[i][j] == '?'){
        if(t[i-1][j] != '?') t[i][j] = t[i-1][j];
    }

    FORD(i,n-1,1) FOR(j,1,m) if(t[i][j] == '?'){
        if(t[i+1][j] != '?') t[i][j] = t[i+1][j];
    }

    FOR(i,1,n){ //cout << s[i] << endl;
        FOR(j,1,m) cout << t[i][j]; cout << endl;
    }

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
        cin >> n >> m;
        FOR(i,1,n) { cin >> s[i]; s[i] = '0' + s[i]; }
        cout << "Case #" << test << ":\n";
        solve();
    }




    return 0;
}
