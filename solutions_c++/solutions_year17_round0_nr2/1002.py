#include <bits/stdc++.h>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
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

LL n, cnt;
int ans[maxn];

LL toNum(string s){
    LL ans = 0;
    FO(i,0,s.size()) ans = ans*10 + s[i]-48;
    return ans;
}

string toString(LL n){
    string ans = "";
    while(n){
        ans = char(n%10+48) + ans;
        n /= 10;
    }
    return ans;
}

int check(string s){
    FO(i,0,s.size()-1) if(s[i] > s[i+1]) return 0;
    return 1;
}

void solve(){
    if(n < 10) { cout << n << endl; return; }
    string s = toString(n);
    cnt = s.size();
    if(check(s)) {cout << s << endl; return; }

    FORD(i,s.size()-2,0){
        if(s[i] > '0'){
            string t = s;
            t[i] = s[i]-1;
            FOR(j,i+1,t.size()-1) t[j] = '9';
            if(t[0] == '0') t.erase(0,1);
            if(check(t)) { cout << t << endl; return; }

        }

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
    FOR(test, 1, sotest){
        cin >> n;
        cout << "Case #" << test << ": ";
        solve();
    }



    return 0;
}
