#include <bits/stdc++.h>
using namespace std;
long long msb(long long x){
    long long b=1;
    x/=2;
    while(x>0){
        x/=2;
        b*=2;
    }
    return b;
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out", "w", stdout);
    int teesee;
    long long temp, tmep, tpem;
    scanf("%d", &teesee);
    for(int asd=0; asd<teesee; asd++){
        scanf("%lld%lld", &temp, &tmep);
        if(tmep==1){
            printf("Case #%d: %lld %lld\n", asd+1, temp/2, (temp-1)/2);
            continue;
        }
        tpem = msb(tmep);
        temp-=tmep;
        temp-=(temp%tpem);
        temp = temp/tpem;
        temp++;
        printf("Case #%d: %lld %lld\n", asd+1, temp/2, (temp-1)/2);
    }
}
