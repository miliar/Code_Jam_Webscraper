#pragma comment(linker, "/STACK:102400000,102400000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <complex>
#define LL long long
#define ULL long long
#define ls(x) tree[x].ls
#define rs(x) tree[x].rs
#define maxx(x) tree[x].maxx
#define len(p) (p.R-p.L+1)
#define keytree ch[ch[root][1]][0]
#define dis(x) dis[x.x1][x.y1][x.x2][x.y2][x.dir1][x.dir2]
using namespace std;
const int M = 2e5 + 5, INF = 0x3f3f3f3f, mod = 1e9 + 7;
map<pair<LL,LL>,LL>mp;
pair<LL,LL> get(LL n){
    LL a=(n+1)/2-1,b=n-(n+1)/2;
    return {max(a,b),min(a,b)};
}
int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        LL n,m;
        scanf("%lld %lld",&n,&m);
        mp.clear();
        queue<pair<LL,LL> >Q;
        mp[get(n)]=1;
        Q.push(get(n));
        pair<LL,LL> ans;
        while(!Q.empty()){
            auto now=Q.front();Q.pop();

//            printf("%lld %lld\n",now.first,now.second);
            m-=mp[now];
            if(m<=0){
                ans=now;
                break;
            }
            if(now.first){
                auto a=get(now.first);
                if(!mp[a]){
                    Q.push(a);
                }
                mp[a]+=mp[now];
            }
            if(now.second){
                auto b=get(now.second);
                if(!mp[b]){
                    Q.push(b);
                }
                mp[b]+=mp[now];
            }
        }
        printf("Case #%d: ",cas++);
        printf("%lld %lld\n",max(ans.first,ans.second),min(ans.first,ans.second));
    }
    return 0;
}
