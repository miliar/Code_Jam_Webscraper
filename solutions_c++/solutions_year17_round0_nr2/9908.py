#include<bits/stdc++.h>
using namespace std;
int main(){
    unsigned long long t,n;
    scanf("%llu",&t);
    for(int i=1;i<=t;i++){
        scanf("%llu",&n);
        while((n/1000)>(n/100%10)||(n/100%10)>(n/10%10)||(n/10%10)>(n%10))
            n--;
        printf("Case #%d: %llu\n",i,n);
    }
    return 0;
}
