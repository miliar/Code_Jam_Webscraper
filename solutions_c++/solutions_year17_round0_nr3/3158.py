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
    #define debugHello() cout << "Hello" << endl
#else
    #define debugHello()
#endif
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
ll getSize(string path, ll n) {
    int l = path.size();
    int i;
    FOR(i,0,l-1) {
        if(path[i] == 'L') {
            if (n&1LL) {
                n = ((n-1LL)>>1LL); 
            } else {
                n = ((n>>1LL) - 1LL);
            }
        } else {
            if (n&1LL) {
                n = ((n-1LL)>>1LL); 
            } else {
                n = (n>>1LL);
            }
        }
    }
    return n;
}
void printAns(int tt, ll n) {
    ll ls = getSize("L", n);
    ll rs = getSize("R", n);
    cout<<"Case #"<<tt<<": "<<max(ls,rs) << " " <<min(ls,rs)<<endl;
}
int getLevel(ll k) {
    int ret =0;
    while(k>1LL) {
        ret++;
        k>>=1LL;
    }
    return ret;

}
pair < pll ,pll > getNextCnt(pair< pll, pll > p) {
    pair < pll ,pll > ret;
    if (p.first.second == -1LL) {
        if (p.first.first & 1LL) {
            ret.first.first = ((p.first.first-1LL)>>1LL);
            ret.second.first = (p.second.first<<1LL);
            ret.first.second = p.first.second;
            ret.second.second = p.second.second;
        } else {
            debugHello();
            ret.first.first = (p.first.first>>1LL) - 1LL;
            ret.first.second = ret.first.first + 1LL;
            ret.second.first = p.second.first;
            ret.second.second = p.second.first;
            debug(ret.first.first);
            debug(ret.first.second);
            debug(ret.second.first);
            debug(ret.second.second);
        }
        return ret;
    }
    if (p.first.first & 1LL) {
        ret.first.first = ((p.first.first-1LL)>>1LL); 
        ret.first.second = ret.first.first + 1LL;
        ret.second.first = ((p.second.first<<1LL)+ p.second.second);
        ret.second.second = p.second.second;
    } else {
        ret.first.first = ((p.first.first)>>1LL) - 1LL; 
        ret.first.second = ret.first.first + 1LL;
        ret.second.first = p.second.first;
        ret.second.second = ((p.second.second<<1LL)+ p.second.first);
    }
    return ret;
}
ll getSize(ll k, ll n) {
    int lev = getLevel(k);
    debug(lev);
    int i;
    pair < pll, pll > p;
    p.first.first = n;
    p.first.second = -1LL;
    p.second.first = 1LL;
    p.second.second = -1LL;
    FOR(i,1,lev) {
        p = getNextCnt(p);
    }
    debug(p.first.first);
    debug(p.first.second);
    debug(p.second.first);
    debug(p.second.second);
    ll fillInThisLevel = k-(1LL<<lev) + 1LL; 
    debug(k);
    debug((1LL<<lev));
    debug(fillInThisLevel);
    if (fillInThisLevel <= p.second.second) return p.first.second;
    return p.first.first;
}
int main() {
    int t,tt;
    ll n,k,sz;
    cin>>t;
    string path;
    FOR(tt,1,t) {
        cin>>n>>k;
        sz = getSize(k,n);
        printAns(tt, sz);
    }
    return 0;
}
