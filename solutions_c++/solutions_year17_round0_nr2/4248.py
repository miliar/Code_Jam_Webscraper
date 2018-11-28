#include<bits/stdc++.h>

using namespace std;

int maxdigit(long long x){
    long long maxd = 0;
    while(x>0){
        maxd = max(maxd,1ll*x%10);
        x/=10;
    }
    return maxd;
}
long long calc(long long x){
    if (x==0) return 0;
    if (x%10<maxdigit(x/10)) 
        x = x/10*10-1;
    long long res = calc(x/10);
    if (res != x/10)
        return res*10+9;
    return res*10+x%10;
}

int main(){
    freopen("B-large.in","r",stdin);
   freopen("B-small-attempt0.out","w",stdout);

    int T, T2;
    cin>>T;
    T2= T;
    while(T--){
        long long x;
        cin>>x;
        printf("Case #%d: %lld\n",T2-T,calc(x));
    }
}

