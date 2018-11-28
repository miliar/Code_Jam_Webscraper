#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long ll;

int toDigitTable(ll n, int c[]) {

    int m = 0;

    while (n > 0) {

        c[m++] = n % 10;
        n /= 10;
    }

    return m;
}

ll fromDigitTable(int c[], int m) {

    ll n = 0;

    for (int i = m - 1; i >= 0; --i)
        n = n * 10 + c[i];

    return n;
}

void propagateNines(int c[], int i) {

    while (i >= 0)
        c[i--] = 9;
}

void propagateDecrementation(int c[], int i, int m) {

    while (i < m && !c[i])
        c[i++] = 9;
}

ll lastTidy(ll n) {

    static const int MAXLEN = 30;

    int c[MAXLEN] = {0};
    int m = toDigitTable(n, c);

    for (int i = m - 2; i >= 0; --i) {

        if (c[i + 1] > c[i]) {

            c[i + 1]--;
            propagateNines(c, i);

            i = m - 1;
        }
    }

    return fromDigitTable(c, m);
}

int main() {

    int t;
    ll n;

    scanf("%d", &t);

    for (int l = 1; l <= t; ++l) {

        scanf("%lld", &n);
        printf("Case #%d: %lld\n", l, lastTidy(n));
    }
}
