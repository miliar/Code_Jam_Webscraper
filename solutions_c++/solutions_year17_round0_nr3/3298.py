//
//  main.cpp
//  17_qual_C
//
//
//
//

#include <iostream>
#include <cstdio>

int main() {
    freopen("C-large.in.txt", "r", stdin);
    freopen("C-large.out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    long long n, k, a, b, x, y;
    for(int i=1; i<=t; i++){
        scanf("%lld %lld", &n, &k);
        a=b=n;
        x=1;
        y=0;
        while(k>x+y){
            k-=x+y;
            if(a%2==1){
                a/=2;
                if(b%2==1){
                    b=a;
                    x=2*x+2*y;
                    y=0;
                }else{
                    b=a-1;
                    x=2*x+y;
                }
            }else{
                a/=2;
                if(b%2==1) y=x+2*y;
                else x=y=x+y;
                b=a-1;
            }
        }
        printf("Case #%d: ", i);
        if(k<=x) printf("%lld %lld\n", a/2, (a-1)/2);
        else printf("%lld %lld\n", b/2, (b-1)/2);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
