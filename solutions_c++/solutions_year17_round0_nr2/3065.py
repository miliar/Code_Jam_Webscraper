#include <bits/stdc++.h>
//#define DEBUG
#define si(n) scanf("%d",&n)
#define sl(n) cin>>n
#define sf(n) scanf("%f",&n)
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
#define pln(n) cout<<n<<endl
#define pnl() printf("\n")
#define pls(n) cout<<n<<" "
#define pl(n) cout<<n
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define FORR(i,j,n) for(i=j;i>=n;i--)
#define SORT(n) std::sort(n.begin(),n.end())
#define FILL(n,a) std::fill(n.begin(),n.end(),a)
#define ALL(n) n.begin(),n.end()
#define rsz resize
#define pb push_back
#define MAXINT std::numeric_limits<int>::max()
#define MININT std::numeric_limits<int>::min()
#define gc getchar_unlocked
#define pc putchar_unlocked
#define iOS std::ios_base::sync_with_stdio(false)
#define endl "\n"
#define INF 1000000000000000005LL
#define INFI 1009990000
#ifdef DEBUG
    #define debug(x) cout << #x << " = " << x << endl
#else
    #define debug(x)
#endif
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
const ld eps = 0.0000001L;
/**************** TEMPLATE ENDS HERE *************************/
const int MAXN = 151234;
string myTrim(string s) {
    int n = s.size();
    int i;
    string ret;
    FOR(i,0,n-1) if (s[i] != '0' || i==n-1) break;
    debug(i);
    return (s.substr(i));
}
bool process(string &s) {
    int n = s.size();
    int i,j;
    bool done = true;
    FOR(i,0,n-2) {
        if (s[i] > s[i+1]) {
            s[i]--;
            if (i!=0 && s[i]<s[i-1]) done=false;
            FOR(j,i+1,n-1) s[j] = '9';
        }
    }
    return done;
}
int main() {
    string s;
    int t,tt;
    cin>>t;
    FOR(tt,1,t) {
        cin>>s;
        bool done=false;
        do {
            done = process(s);
        } while(!done);
        cout<<"Case #"<<tt<<": "<<myTrim(s)<<endl;
    }
    return 0;
}
