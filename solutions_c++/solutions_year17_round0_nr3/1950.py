#include <cstdio>
#include <algorithm>
using namespace std;

long long getSum(long long n) {
    long long sum = 0;
    while(sum < n){
        sum = (sum+1)*2 -1;
    }
    return (sum+1)/2-1;
}

int main() {
    int tc, tc_;
    scanf("%d", &tc);
    for (int tc_=1; tc_<=tc; tc_++){
        long long n, k, sum;
        scanf("%lld %lld", &n, &k);
        sum = getSum(k);
        long long def = (n-sum)/(sum+1);
        long long add = (n-sum)%(sum+1);
        long long tot = (k-sum) > add ? def : def + 1;
        printf("Case #%d: %lld %lld\n", tc_, tot/2, tot - 1 - tot/2);
    }
    return 0;
}
