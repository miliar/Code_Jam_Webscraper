#include <cstdio>
#include <cstring>

using namespace std;

#define INF 10000000

int a[111];
int n;
int k;
int curr;
int best;

void inc(int l, int r) {
    for (int i = l; i < r; ++i) a[i]++;
}

void dec(int l, int r) {
    for (int i = l; i < r; ++i) a[i]--;
}

bool check() {
    for (int i = 0; i < n; ++i)
        if (a[i] % 2 != 0) return false;

    return true;
}

void attempt(int step) {
    if (step > n - k) {
        if (check()) {
            if (curr < best) best = curr;
        }
        return ;
    }

    for (int i = 0; i < 2; ++i) {
        if (i == 1) {
            inc(step, step + k);
            ++curr;
        }

        attempt(step + 1);

        if (i == 1) {
            dec(step, step + k);
            --curr;
        }
    }
}

int main() {
    int nTest;
    scanf("%d", &nTest);

    for (int test = 0; test < nTest; ++test) {
        scanf("\n");
        char s[11];
        scanf("%s %d", s, &k);

        n = strlen(s);
        for (int i = 0; i < n; i++)
            a[i] = s[i] == '+' ? 0 : 1;

        curr = 0;
        best = INF;
        attempt(0);

        printf("Case #%d: ", test + 1);
        if (best != INF) {
            printf("%d\n", best);
        }
        else {
            printf("IMPOSSIBLE\n");
        }
    }

    return 0;
}
