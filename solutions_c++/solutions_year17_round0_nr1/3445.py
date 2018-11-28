#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int maxN = 1010;

#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define ll long long

int test, res, k, n;
char s[maxN];

void flip(int p) {
    foru(i, 1, k)
        s[p + i - 1] = (s[p + i - 1] == '-') ? '+' : '-';
}

int main() {
    scanf("%d\n", &test);
    foru(t, 1, test) {
        scanf("%s %d\n", s, &k);
        n = strlen(s);
        res = 0;
        repu(i, n - k + 1)
            if (s[i] == '-') flip(i), ++res;
        repu(i, n)
            if (s[i] == '-') res = -1;
        printf("Case #%d: ", t);
        if (res == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", res);
    }
}
