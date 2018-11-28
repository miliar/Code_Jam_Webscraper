#include <bits/stdc++.h>
using namespace std;

bool isTidy(long long N){
    int last_digit=10;
    while (N>0){
        if (N%10>last_digit)
            return false;
        last_digit=N%10;
        N/=10;
    }
    return true;
}

long long count_last_tidy(long long &N){
    while (!isTidy(N)){
        N--;
    }
    return N;
}

int main() {
    int T;
    long long N;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        scanf("%lld", &N);
        printf("Case #%d: %lld\n", i, count_last_tidy(N));
    }
}
