#include <cstdio>
#include <algorithm>
using namespace std;

int cnt[10];
int n, p;

void two() {
    for(int a, i = 0; i < n; ++i) {
        scanf("%d", &a);
        cnt[a&1]++;
    }
    cnt[1]++;
    printf("%d\n", cnt[0] + cnt[1] / 2);
}

void three() {
    for(int a, i = 0; i < n; ++i) {
        scanf("%d", &a);
        cnt[a % 3] ++;
    }
    int res = cnt[0];
    if(cnt[1] > cnt[2]) swap(cnt[1], cnt[2]);
    res += cnt[1];
    cnt[2] -= cnt[1];
    printf("%d\n", res + (cnt[2] + 2) / 3);
}

void four() {
    for(int a, i = 0; i < n; ++i) {
        scanf("%d", &a);
        cnt[a & 3]++;
    }
    int res = cnt[0];
    res += cnt[2] / 2;
    cnt[2] %= 2;
    if(cnt[1] > cnt[3]) swap(cnt[1], cnt[3]);
    res += cnt[1];
    cnt[3] -= cnt[1];
    if(cnt[2] && cnt[3] >= 2) {
        res++;
        cnt[3] -= 2;
    }
    printf("%d\n", res + (cnt[3] + 3) / 4);
}

void prog() {
    cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0;
    scanf("%d%d", &n, &p);
    if(p == 2) two();
    if(p == 3) three();
    if(p == 4) four();
}

int main() {
    int _;
    scanf("%d", &_);
    for(int i = 1; i <= _; ++i) {
        printf("Case #%d: ", i);
        prog();
    }
}