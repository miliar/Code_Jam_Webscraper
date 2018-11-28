#include <cstdio>

unsigned long long getTidyRoot(unsigned long long n) {
    if (n<10) {
        return n;
    }
    unsigned long long tidyPrefix = n;
    bool untidy = false;

    while (n>=10) {
        unsigned lastDigits = n%100;
        if (lastDigits/10 > lastDigits%10) {
            untidy = true;
            tidyPrefix = n/10;
        }
        n/=10;
    }
    if (untidy) {
        return getTidyRoot(tidyPrefix-1);
    }
    return tidyPrefix;
}

unsigned long long lastTidy(unsigned long long n) {

    unsigned long long t = getTidyRoot(n);

    while (t<n/10) {
        t *= 10;
        t += 9;
    }

    return t;
}

int main(int argc, char **argv) {

    unsigned T;
    scanf("%u\n",&T);
    for (unsigned i=0; i<T; ++i) {
        unsigned long long N;

        scanf("%llu\n",&N);

        printf("Case #%u: %llu\n",i+1,lastTidy(N));
    }

    return 0;
}







