#include <cstdio>
#include <cstring>
#include <cstdlib>
long long N;
void solve(){
    scanf("%lld",&N);
    long long t = 1;
    while (N/t>0){
        long long cur = (N/t)%10;
        long long pre = N/(t*10)%10;
        if (pre>cur){
            N = (N/(t*10)) * (t*10) -1;
        }
        t*=10;
    }
    printf("%lld\n", N);
}
int main(){
    int N;
    scanf("%d", &N);
    for (int i=1;i<=N;++i){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
