#include <cstdio>
#include <queue>

using namespace std;
using ll = long long;

int main(){

    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);

    int t;
    scanf("%d", &t);
    int tc = 0;

    while(t--){

        ll n, k;
        scanf("%lld %lld", &n, &k);

        priority_queue < pair<ll,ll> > q;
        q.emplace(n, 1);

        printf("Case #%d: ", ++tc);

        while(!q.empty()){
            pair <ll,ll> f = q.top(); q.pop();
            k -= f.second;
            ll g = f.first>>1;
            if(k <= 0){
                if(f.first&1)printf("%lld %lld\n", g, g);
                else
                    printf("%lld %lld\n", g, g-1);
                break;
            }
            if(f.first&1){
                q.emplace(g, 2LL*f.second);
            }else{
                q.emplace(g, f.second);
                q.emplace(g-1, f.second);
            }
        }

    }

}
