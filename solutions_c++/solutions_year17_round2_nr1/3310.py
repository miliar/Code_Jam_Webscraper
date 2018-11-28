#include <bits/stdc++.h>
using namespace std;

#define FOR(i,f,t) for(int i=f; i<t; i++)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define pb push_back
#define SYNC ios_base::sync_with_stdio(false)
#define inf 2248012
#define mp make_pair
#define sci(x) scanf("%d",&x)
#define scii(x,y) scanf("%d %d",&x,&y)
#define sciii(x,y,z) scanf("%d %d %d",&x,&y,&z)

typedef long long ll;

int main(){
    int t;
    sci(t);
    FOR(g,0,t){
        ll n,k;
        double a,b;
        scanf("%lld%lld",&k,&n);
        double ans = -1;
        FOR(i,0,n){
            scanf("%lf%lf",&a,&b);
            if(a<=k){
                double e= (k-a)/b;
                ans= max(ans,e);
            } 
        }
        ans = k/ans;
        printf("Case #%d: %.12lf\n",g+1,ans);
    }
}