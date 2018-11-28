#include <cstdio>
#include <set>
using namespace std;
set<long long> s;
void gen(long long n){
    if(n > 1e18)
        return;
    s.insert(n);
    for(long long i = n % 10ll; i < 10ll; i++){
        gen(10ll*n + i);
    }
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    for(long long i = 1ll; i < 10ll; i++){
        gen(i);
    }
    int t;
    scanf("%d",&t);
    long long n;
    for(int i = 1; i <= t; i++){
        scanf("%lld",&n);
        printf("Case #%d: %lld\n",i,*(--s.upper_bound(n)));
    }
    return 0;
}
