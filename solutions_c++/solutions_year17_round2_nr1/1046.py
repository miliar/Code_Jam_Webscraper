#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

double solve(){
    ull D,N;
    double time = 0;
    scanf("%llu %llu\n",&D,&N);
    for(int i=0;i<N;i++){
        ull K,S;
        scanf("%llu %llu\n",&K,&S);
        time = max((double)(D-K)/(double)S,time);
    }
    return D/time;
}

int main() {
    int T;
    scanf("%d\n",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: %.10f\n",i,solve());
    }
    return 0;
}