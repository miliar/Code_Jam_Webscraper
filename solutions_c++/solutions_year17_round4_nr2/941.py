#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int maxn=1007;

int n,c,m,seat[maxn],b[maxn],p[maxn];
multiset<int> s[maxn];
multiset<int>::iterator it[maxn];

int main(){
//    freopen("input.txt","r",stdin);
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%d%d%d",&n,&c,&m);
        for(int i=1; i<=1000; ++i) s[i].clear(), seat[i]=0;
        for(int i=1; i<=m; ++i){
            scanf("%d%d",&p[i],&b[i]);
            s[b[i]].insert(p[i]);
            ++seat[p[i]];
        }

        int res1 = 0;
        while(1){
            set<pii> mys;
            for(int i=1; i<=c; ++i){
                it[i]=s[i].begin();
                if(it[i]!=s[i].end()) mys.insert(pii(*it[i],i));
            }
            if(mys.empty()) break;
            ++res1;
            for(int v=1; v<=n; ++v){
                while(!mys.empty()){
                    if(mys.begin()->first < v){
                        int idx = mys.begin()->second;
                        it[idx] = s[idx].lower_bound(v);
                        mys.erase(mys.begin());
                        if(it[idx] != s[idx].end()) mys.insert(pii(*it[idx],idx));
                    }else{
                        //found
                        int idx = mys.begin()->second;
                        s[idx].erase(it[idx]);
                        mys.erase(mys.begin());
                        break;
                    }
                }
            }
        }
        int res2=0;
        for(int i=1; i<=n; ++i) if(seat[i]>res1) res2+=seat[i]-res1;

        printf("Case #%d: %d %d\n",tt,res1,res2);
    }
}
