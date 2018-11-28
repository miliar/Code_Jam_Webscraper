#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int TC;
long long n, k;
pair<long long, long long> construct(long long x1, long long v1, long long x2, long long v2, long long cn){
    //printf("q %lld %lld %lld %lld %lld\n", x1, v1, x2, v2, cn);
    if(cn <= v1) return make_pair((x1-1)/2, (x1-1)/2+(x1-1)%2);
    else{
        if(cn <= v2 + v1) return make_pair((x2-1)/2, (x2-1)/2+(x2-1)%2);
        else{
            if(x1 == 1) return make_pair(0, 0);
            if(x2 == -1){
                if(x1&1) return construct(x1/2, v1*2, -1, -1, cn - v1);
                else return construct(x1/2, v1, x1/2-1, v1, cn - v1);
            }
            else{
                if(x1 & 1) return construct(x1/2, v1*2 + v2, x1/2-1, v2, cn - v1 - v2);
                else return construct(x1/2, v1, x1/2-1, v2*2 + v1, cn - v1 - v2);
            }
        }
    }
}
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%lld %lld", &n, &k);
        auto x = construct(n, 1, -1, 0, k);
        printf("Case #%d: %lld %lld\n", tc, x.second, x.first);
    }
}
