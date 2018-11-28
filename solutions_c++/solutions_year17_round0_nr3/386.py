#include<stdio.h>

typedef long long ll;

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        ll k, n;
        scanf("%I64d%I64d", &n, &k);
        printf("Case #%d: ", kase);
        for(ll i=1, a=n, b=1; ; i<<=1){
            if(k <= i){
                if(k <= b){
                    printf("%I64d %I64d\n", a/2, (a-1)/2);
                }else{
                    printf("%I64d %I64d\n", (a-1)/2, a/2-1);
                }
                break;
            }
            if(a&1){
                b += i;
            }
            a >>= 1; k -= i;
        }
    }
    return 0;
}
