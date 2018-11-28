#include<bits/stdc++.h>
using namespace std;

const int maxn = 30;

#define LL long long

bool reduce(LL &x){
    LL tmp = x;
    if(x < 10) return false;
    int left = tmp % 10;
    tmp /= 10;
    int miner = 1;
    while(tmp){
        int now = tmp % 10;
        tmp /= 10;
        if(now > left){
            tmp = tmp * 10 + now - 1;
            while(miner--){
                tmp = tmp * 10 + 9;
            }
            x = tmp;
            return true;
        }
        left = now;
        miner ++;
    }
    return false;
}

int main(){
    int T;
    scanf("%d",&T);
    int icase = 1;
    LL x;
    while(T-- && ~scanf("%lld",&x)){
        while(reduce(x));
        printf("Case #%d: %lld\n",icase++,x);
    }
    return 0;
}
