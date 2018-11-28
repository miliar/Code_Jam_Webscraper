#include<stdio.h>
#include<string.h>
#include<math.h>

int nums[18];
long long int resolv(long long int N) {
    int digits = 0;
    while(N > 0) {
        nums[digits] = N % 10l;
        N = N / 10l;
        ++digits;
    }
    for(int i = 0; i < digits - 1; ++i) {
        if (nums[i+1] > nums[i]) {
            --nums[i+1];
            for (int j = i; j >= 0; --j){
                nums[j] = 9;
            }
        }
    }
    N = 0;
    for(int i = digits - 1; i >= 0; --i) {
        N = N * 10l + nums[i];
    }
    return N;
}

int main() {
    long long int N;
    int T;
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for(int i = 0; i < T;++i) {
        scanf("%lld", &N);
        printf("Case #%d: %lld\n", i+1, resolv(N));
    }

    return 0;
}