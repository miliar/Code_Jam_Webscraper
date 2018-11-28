#include<cstdio>
using namespace std;
typedef unsigned long long ll;
ll t,n;
int main() {
    scanf("%llu", &t);
    for(ll i=1;i<=t;i++) {
        scanf("%llu", &n);
        for(ll k=1;n/(k*10);k*=10)
            if(n/(k*10)%10 > n/k%10) n = (n/(k*10)-1)*k*10+k*10-1;
        printf("Case #%llu: %llu\n", i, n);
    }
    return 0;
}
