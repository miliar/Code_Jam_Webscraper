#include <cstdio>
#include <string>
#include <queue>
#include <map>
#include <utility>
#include <iostream>

using namespace std;

bool isTidy(int n) {
    return n < 100 ? n/10 <= n%10 : (n%100)/10 <= n%10 && isTidy(n/10);
}

int main() {
    int t, n, cases=0;

    scanf("%d", &t);

    while (t--) {
        scanf("%d", &n);

        while(!isTidy(n)) n--;

        printf("Case #%d: %d\n", ++cases, n);
    }

    return 0;
}

