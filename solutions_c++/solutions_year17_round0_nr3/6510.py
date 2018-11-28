// C: Bathroom Stalls

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include <queue>

using namespace std;

int main(int argc, char *argv[]) {
    unsigned int T;
    unsigned long long N, K;
    scanf("%u", &T);
    for (unsigned int i = 0; i < T; i++) {
        scanf("%llu %llu", &N, &K);

        priority_queue<unsigned long long> stalls;
        stalls.push(N);
        unsigned long long stall;
        for (uint64_t client = 0; client < K; client++) {
            stall = stalls.top() - 1;
            stalls.pop();
            stalls.push(stall / 2);
            stalls.push(stall - stall / 2);
        }

        printf("Case #%u: ", i + 1);
        printf("%llu %llu", stall - stall / 2, stall / 2);
        printf("\n");
    }
}
