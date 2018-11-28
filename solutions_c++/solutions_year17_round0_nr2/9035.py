#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

bool Judge(int x) {
    int last = 9;
    while(x) {
        int tmp = x % 10;
        if(tmp > last) return false;
        x /= 10, last = tmp;
    }
    return true;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while(T--) {
        int n;
        scanf("%d", &n);
        for(int i = n; i; i--) {
            if(Judge(i)) {
                printf("Case #%d: %d\n", ++cnt, i); break;
            }
        }
    }
}
