#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int TC;
long long n;
struct No{
    int len;
    long long p[20];
    long long val;
    No(long long x){
        val = x; len = 0;
        while(x > 0){
            p[len++] = x%10;
            x/=10;
        }
    }
};
bool isAscending(No x){
    for(int i = 0; i+1 < x.len; ++i){
        if(x.p[i] < x.p[i+1]) return false;
    }
    return true;
}
long long p10[19];
long long construct(long long v){
    //printf("conducting %lld\n", v);
    if(v < 10) return v;
    No V(v);
    long long m = 1;
    for(int i = 2; i < V.len; ++i) m = m*10+1;
    //printf("%d - %lld\n", V.len, m*V.p[V.len-1]);
    long long g = v - V.p[V.len-1]*p10[V.len-1];
    if(g >= m*V.p[V.len-1]) return V.p[V.len-1]*p10[V.len-1] + construct(g);
    else{
        //printf("returning %lld\n", (V.p[V.len-1]-1)*p10[V.len-1] + m * 9);
        return (V.p[V.len-1]-1)*p10[V.len-1] + m * 9;
    }
}
int main(){
    p10[0] = 1;
    for(int i = 1; i < 19; ++i) p10[i] = p10[i-1]*10;
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", tc, construct(n));
    }
}
