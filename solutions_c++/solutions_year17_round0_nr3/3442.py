#include "bits/stdc++.h"
//#include "ext/pb_ds/tree_policy.hpp"
//#include "ext/pb_ds/assoc_container.hpp"
#define PB push_back
#define PF push_front
#define LB lower_bound
#define UB upper_bound
#define fr(x) freopen(x,"r",stdin)
#define fw(x) freopen(x,"w",stdout)
#define iout(x) printf("%d\n",x)
#define lout(x) printf("%lld\n",x)
#define REP(x,l,u) for(ll x = l;x<u;x++)
#define RREP(x,l,u) for(ll x = l;x>=u;x--)
#define complete_unique(a) a.erase(unique(a.begin(),a.end()),a.end())
#define mst(x,a) memset(x,a,sizeof(x))
#define all(a) a.begin(),a.end()
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define MP make_pair
#define sqr(x) ((x)*(x))
#define lowbit(x) (x&(-x))
#define lson (ind<<1)
#define rson (ind<<1|1)
#define se second
#define fi first
#define dbg(x) cout<<#x<<" = "<<(x)<<endl;
#define sz(x) ((int)x.size())
#define EX0 exit(0);

typedef  long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ld;
using namespace std;
const int block_size = 320;
typedef complex<ll> point;
const ll mod = 1e9+7;
const ld eps = 1e-9;
const int inf = mod;
const db PI = atan(1)*4;
template<typename T>
inline int sign(const T&a){if(a<0)return -1;if(a>0)return 1;return 0;}


template<typename T> inline void in(T &x){
    x = 0; T f = 1; char ch = getchar();
    while (!isdigit(ch)) {if (ch == '-') f = -1; ch = getchar();}
    while (isdigit(ch))  {x = x * 10 + ch - '0'; ch = getchar();}
    x *= f;
}

ll twop(int x){return 1LL<<x;}

template<typename A,typename B > inline void in(A&x,B&y){in(x);in(y);}
template<typename A,typename B,typename C>inline void in(A&x,B&y,C&z){in(x);in(y);in(z);}
template<typename A,typename B,typename C,typename D> inline void in(A&x,B&y,C&z,D&xx){in(x);in(y);in(z);in(xx);}




template <class T>
void upd(T&a,T b) {
    a = max(a,b);
}
int occupy[1010];
struct foo{
    int l,r,pos;
    
    bool operator<(const foo&o)const{
        if(min(l,r)!=min(o.l,o.r)){
            return min(l,r)>min(o.l,o.r);
        }
        if(max(l,r)!=max(o.l,o.r)){
            return max(l,r)>max(o.l,o.r);
        }
        return pos<o.pos;
    }
    void output(){
        cout<<l<<' '<<r<<' '<<pos<<endl;
    }
};
int l[1010],r[1010];

void solve(int n){
    mst(occupy,0);
    occupy[0] = occupy[n+1] = 1;
    vector<foo>v;
    REP(i,0,n){
        REP(i,0,n+1){
            if(occupy[i]){
                l[i] = i;
            }else{
                l[i] = l[i-1];
            }
        }
        RREP(i,n+1,0){
            if(occupy[i]){
                r[i] = i;
            }else{
                r[i] = r[i+1];
            }
        }

        REP(j,1,n+1){
            if(!occupy[j]){
                v.PB((foo){static_cast<int>(j-l[j]-1),static_cast<int>(r[j]-j-1),static_cast<int>(j)});
            }
        }
        sort(all(v));
        v[0].output();
        occupy[v[0].pos] = 1;
        v.clear();
    }

    
}

void add(ll len,ll size,deque<PLL>&v){
    if(!len)return;
    if(sz(v)&&v.back().fi==len)v.back().se+=size;
    else v.PB(MP(len,size));
}
void calc(ll n,ll k){
    deque<PLL>v;
    v.PB(MP(n,1));
    ll ans = 0;
    while(k>0){
        auto f = v.front();
        v.pop_front();
        k-=f.se;
        if(k<=0)ans = f.fi;
        add(f.fi/2, f.se, v);
        add((f.fi-1)/2, f.se, v);
    }
    cout<<(ans)/2<<' '<<(ans-1)/2<<endl;
}

int main(){
    fr("/Users/zhangqingchuan/Desktop/C-large.in");
    fw("/Users/zhangqingchuan/Desktop/做题/做题/output.txt");
    int t;cin>>t;
    REP(i,1,t+1){
        printf("Case #%lld: ",i);ll n,k;cin>>n>>k;calc(n, k);
    }
    return 0;
}
