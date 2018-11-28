#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef double LF;

const int maxN = 1000 + 5;

int T;
int R, O, Y, G, B, V, N;

struct ES {
    int num;
    char col;
    ES() {}
    ES(char c, int n): col(c), num(n) {}
} A[15];

bool Cmp(ES e1, ES e2) {
    if (e1.num == e2.num) return e1.col < e2.col;
    return e1.num < e2.num;
}

int main() {
    //freopen("2.in", "r", stdin);
    //freopen("2.txt", "w", stdout);
    scanf("%d", &T);
    for (int testCase = 1; testCase <= T; ++testCase) {
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        printf("Case #%d: ", testCase);
        A[1] = ES('R', R); A[2] = ES('Y', Y); A[3] = ES('B', B);
        sort(A + 1, A + 3 + 1, Cmp);
        if (A[1].num + A[2].num < A[3].num) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for (int i = 1; i <= A[3].num; ++i) {
            printf("%c", A[3].col);
            if (i <= A[1].num) printf("%c", A[1].col);
            if (A[3].num - i + 1 <= A[2].num) printf("%c", A[2].col);
        }
        printf("\n");
    }
    return 0;
}
