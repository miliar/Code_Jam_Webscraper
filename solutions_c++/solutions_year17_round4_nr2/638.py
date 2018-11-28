#include <cstdio>
#include <algorithm>
using namespace std;

const int maxN = 1024;
int cnt_c[maxN];
int cnt_p[maxN];

int n, c, m;

void prog() {
    scanf("%d%d%d", &n, &c, &m);
    for(int i = 1; i <= n; ++i) cnt_p[i] = 0;
    for(int i = 1; i <= c; ++i) cnt_c[i] = 0;
    for(int p, cl, i = 0; i < m; ++i) {
        scanf("%d%d", &p, &cl);
        cnt_p[p]++;
        cnt_c[cl]++;
    }
    int rolls = 0, sum = 0;
    for(int i = 1; i <= n; ++i) {
        sum += cnt_p[i];
//         printf(">>%d\n", (sum + i - 1) / i);
        rolls = max(rolls, (sum + i - 1) / i);
    }
    for(int i = 1; i <= c; ++i) {
//         printf("%d\n", cnt_c[i]);
        rolls = max(rolls, cnt_c[i]);
    }
//     printf("ROLLZ = %d\n", rolls);
    sum = 0;
    for(int i = 1; i <= n; ++i) sum += max(0, cnt_p[i] - rolls);
    printf("%d %d\n", rolls, sum);
}

int main() {
    int _;
    scanf("%d", &_);
    for(int i = 1; i <= _; ++i) {
        printf("Case #%d: ", i);
        prog();
    }
}