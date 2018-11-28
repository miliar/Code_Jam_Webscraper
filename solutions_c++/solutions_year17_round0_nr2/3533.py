#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

int main(){

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    set <ll> v;
    v.insert(0);
    for(auto &e : v){
        int x = e%10;
        for(int i=x; i<=9; i++){
            ll y = e*10LL+i;
            if(y <= 1e+18){
                v.insert(e*10LL+i);
            }else{
                break;
            }
        }
    }

    int t;
    scanf("%d", &t);

    int tc = 0;

    while(t--){
        ll n;
        scanf("%lld", &n);

        printf("Case #%d: ", ++tc);

        set <ll> ::iterator it = v.lower_bound(n);
        if(*it != n)it--;
        printf("%lld\n", *it);
    }

}
