#define TXTOUT
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
char a[32];
char answer[32];
LL Solve() {
    int la = strlen(a);
    int id = -1;
    for (int i = 0; i + 1 < la; i++) {
        if (a[i] > a[i + 1]) {
            id = i;
            break;
        }
    }
    strcpy(answer, a);
    if (id != -1) {
        while (id - 1 >= 0 && a[id - 1] == a[id]) id--;
        answer[id]--;
        for (int i = id + 1; i < la; i++) {
            answer[i] = '9';
        }
    }
    LL result;
    sscanf(answer, "%lld", &result);
    return result;
}
int main() {
    #ifdef TXTOUT
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    #endif // TXTOUT
    int t;
    scanf("%d", &t);
    int cas = 1;
    while (t--) {
        int n;
        scanf("%s", a);
        printf("Case #%d: %lld\n", cas++, Solve());
    }
    return 0;
}

/**

4
132
1000
7
111111111111111110

*/
