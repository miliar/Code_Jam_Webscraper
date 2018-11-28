#include <iostream>
#include <cstdio>
#include <string>

using std::cin;
using std::string;

void process(int i, long long n);

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        long long n;
        scanf("%lld", &n);
        process(i, n);
    }
}

void process(int test, long long n) {
    long long res = 0;
    long long base = 1;
    int current = 9;
    while (n > 0) {
        if (current >= n % 10) {
            current = n % 10;
            res += base * (n % 10);
        } else {
            current = n % 10 - 1;
            res = base - 1 + (n % 10 - 1) * base;
        }
        n /= 10;
        base *= 10;
    }
    printf("Case #%d: %lld\n", test, res);
}
