#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int maxn=55;

int q[maxn][maxn],r[maxn],n,p,it[maxn],L[maxn],R[maxn];

int mulAtMost(ll v, ll des){
    ll l=1, r=oo, mid, mul = -1;
    while(l<=r){
        mid = (l+r)/2;
        if(mid * v * 90 <= des * 100){
            mul = mid;
            l = mid + 1;
        }else {
            r = mid - 1;
        }
    }
    return mul;
}

int mulAtLeast(int v, int des){
    ll l=1, r=oo, mid, mul = -1;
    while(l<=r){
        mid = (l+r)/2;
        if(mid * v * 110 >= des * 100){
            mul = mid;
            r = mid - 1;
        }else {
            l = mid + 1;
        }
    }
//    if(!(mid * v * 90 <= des * 100 && des * 100 <= mid * v * 110)){
//        cout << v << ' ' << des << ' ' << mul << ' ' << mulAtMost (v, des) << endl;
//    }
    return mul;
}



int tryToMake() {
    for(int i=1; i<=n; ++i){
        while(it[i]<=p){
            L[i] = mulAtLeast(r[i], q[i][it[i]]);
            R[i] = mulAtMost(r[i], q[i][it[i]]);
            if(L[i]!=-1 && R[i]!=-1) break;
            ++it[i];
        }
        if(it[i]>p) return 0;
    }
    while(true){
        int lBound = 0, rBound = oo;
        for(int i=1; i<=n; ++i){
            lBound = max(lBound, L[i]);
            rBound = min(rBound, R[i]);
        }
        if(lBound <= rBound) return 1;
        for(int i=1; i<=n; ++i){
            if(R[i] < lBound) {
                ++it[i];
                if (it[i]>p) return 0;
                L[i] = mulAtLeast(r[i], q[i][it[i]]);
                R[i] = mulAtMost(r[i], q[i][it[i]]);
            }
        }
    }
}

int main(){
//    freopen("input.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%d%d",&n,&p);
        for(int i=1; i<=n; ++i) scanf("%d",&r[i]);
        for(int i=1; i<=n; ++i){
            for(int j=1; j<=p; ++j) scanf("%d",&q[i][j]);
            sort(q[i]+1,q[i]+p+1);
            it[i]=1;
        }
        int res=0;
        while(tryToMake()) {
            ++res;
            for(int i=1; i<=n; ++i) ++it[i];
        }
        printf("Case #%d: %d\n",tt,res);

    }
}
