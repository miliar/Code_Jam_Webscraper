#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstdlib>
#include <ctime>
#include <deque>
using namespace std;

int a[30];

void doit() {
    long long n;
    scanf("%lld", &n);
    for (int i = 1; i <= 20; i++) {
        a[i] = n % 10;
        n /= 10;
    }
    while (true) {
        bool f = false;
        for (int i = 20; i > 1; i--)
            if (a[i] > a[i - 1]) {
                f = true;
                a[i] -= 1;
                for (int j = i - 1; j; j--)
                    a[j] = 9;
                break;
            }
        if (!f)
            break;
    }
    long long ans = 0;
    for (int i = 20; i; i--)
        ans = ans * 10 + a[i];
    printf("%lld\n", ans);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        doit();
    }
}