#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

long long process(long long N) {
    char num[23];
    sprintf(num, "%lld", N);

    while (true) {
        bool updated = false;
        int L = strlen(num);
        for (int i = 0; i + 1 < L; i ++) {
            if (num[i] > num[i + 1]) {
                for (int j = i + 1; j < L; j ++) {
                    num[j] = '9';
                }
                num[i] --;
                updated = true;
                break;
            }
        }
        if (!updated){
            break;
        }
    }

    sscanf(num, "%lld", &N);
    return N;
}

int main() {
    int T;
    scanf("%d", &T);
    
    for (int test = 1; test <= T; test ++) {
        long long N;
        scanf("%lld", &N);

        printf("Case #%d: %lld\n", test, process(N));
    }
    return 0;
}
