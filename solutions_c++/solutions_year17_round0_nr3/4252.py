#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <fstream>

using namespace std;


#define LL long long
#define N 5000002
#define M 400100
#define MP make_pair
#define Pi acos(-1.0)
#pragma comment(linker,"/STACK:1024000000,1024000000")
#define ls (rt << 1)
#define rs (ls | 1)
#define md ((ll+rr)/2)
#define lson ll, md, ls
#define rson md+1, rr, rs
#define mod 1000000007
#define inf 0x3f3f3f3f
#define sqr(x) ((x)*(x))
#define eps 1e-6
#define uLL unsigned long long
#define ui unsigned int
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
#define F(x) ((x)/3+((x)%3 == 1 ? 0 : tb))
#define G(x) ((x)<tb ? (x)*3+1 : ((x) - tb)*3+2)
#define lowbit(x) ((x)&(-x))
#define fi first
#define se second
#define Pii pair<int,int>
#define pli pair<LL,int>
#define pb push_back
#define MP make_pair
LL gcd(LL x,LL y){
    while(y){
        LL t = x % y;
        x = y;
        y = t;
    }
    return x;
}

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
struct node{
    long long mi,mx;
    bool operator < (const node &b) const{
        if(mi != b.mi) return mi > b.mi;
        return mx > b.mx;
    }
    bool operator > (const node &b) const{
        if(mi != b.mi) return mi < b.mi;
        return mx < b.mx;
    }
};

LL n, k;

map<node,LL> mp;
priority_queue<node,vector<node>,greater<node> > q;

void make(){
    mp.clear();

    if(n&1)
        q.push((node){(n-1)/2,(n-1)/2});
    else
        q.push((node){n/2-1,n/2});
    
    mp[q.top()] = 1;
    while(!q.empty()){
        node cur = q.top(); q.pop();
        
        if(cur.mi){
            if(cur.mi&1){
                node nxt = (node){(cur.mi-1LL)/2LL,(cur.mi-1LL)/2LL};
                if(!mp.count(nxt)){
                    q.push(nxt);
                }
                mp[nxt] += mp[cur];
            }else{
                node nxt = (node){cur.mi/2LL-1LL,cur.mi/2LL};
                if(!mp.count(nxt)){
                    q.push(nxt);
                }
                mp[nxt] += mp[cur];
            }
        }
        if(cur.mx){
            if(cur.mx&1){
                node nxt = (node){(cur.mx-1LL)/2LL,(cur.mx-1LL)/2LL};
                if(!mp.count(nxt)){
                    q.push(nxt);
                }
                mp[nxt] += mp[cur];
            }else{
                node nxt = (node){cur.mx/2LL-1LL,cur.mx/2LL};
                if(!mp.count(nxt)){
                    q.push(nxt);
                }
                mp[nxt] += mp[cur];
            }
        }
    }
}

void solve(){
    make();
    long long acc = 0;
    for(auto it = mp.begin(); it != mp.end();it++){
        acc += it->second;
        if(acc >= k) {
            printf("%lld %lld\n", it->first.mx ,it->first.mi);
            return;
        }
    }
}



char s[1010];

int main()
{
    freopen("C-small-2-attempt0.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    int casi = 0;
    T = read();
    while(T--)
    {
        
        
        scanf("%lld%lld",&n, &k);
        
    
        printf("Case #%d: ",++casi);
        
        solve();
        
    }
    return 0;
}


