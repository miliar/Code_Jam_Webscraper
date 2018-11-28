#include <bits/stdc++.h>
using namespace std;
long long t,n,k,awal,c,tempc,temp,xin;
int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d %d", &n, &k);
        printf("Case #%d: ", i);
        awal = 1; c = 0; temp = n;
        while (awal<<1 <= k) {
            awal <<= 1;
            c++;
        }
        tempc = c;
        k -= awal;
        while (tempc){
            temp -= 1;
            temp /= 2;
            tempc--;
        }
        xin = temp;
        while (tempc < c){
            temp *= 2;
            temp++;
            tempc++;
        }
        if (k < n-temp){
            xin++;
        }
        printf("%lld %lld\n", (xin-1)%2+(xin-1)/2, (xin-1)/2);

    }
}
