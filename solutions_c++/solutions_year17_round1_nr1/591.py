#include <cstdio>
#include <cassert>
#include <algorithm>

const int MAXN = 101;

int T, n, m;
char s[MAXN][MAXN];

std::pair<int, char> getCount(int x1, int y1, int x2, int y2) {    
    int counter = 0;
    char flag = ' ';
    for (int i = x1; i <= x2; i++)
        for (int j = y1; j <= y2; j++)
            if (s[i][j] != '?') {
                counter++;
                flag = s[i][j];
            }
    return std::make_pair(counter, flag);
}

void divide(int x1, int y1, int x2, int y2) {
    std::pair<int, char> now = getCount(x1, y1, x2, y2);
    assert(now.first > 0);
    if (now.first == 1) {
        for (int i = x1; i <= x2; i++)
            for (int j = y1; j <= y2; j++)
                s[i][j] = now.second;
        return;
    }
    for (int i = x1; i < x2; i++) {
        std::pair<int, char> left = getCount(x1, y1, i, y2);
        std::pair<int, char> right = getCount(i + 1, y1, x2, y2);
        if (left.first > 0 && right.first > 0) {
            divide(x1, y1, i, y2);
            divide(i + 1, y1, x2, y2);
            return;
        }
    }
    for (int i = y1; i < y2; i++) {
        std::pair<int, char> left = getCount(x1, y1, x2, i);
        std::pair<int, char> right = getCount(x1, i + 1, x2, y2);
        if (left.first > 0 && right.first > 0) {
            divide(x1, y1, x2, i);
            divide(x1, i + 1, x2, y2);
            return;
        }
    }
    assert(false);
}

int main() {
    freopen("A.in", "r", stdin);
    scanf("%d", &T);
    for (int cs = 1; cs <= T; cs++) {
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++) {
            scanf("%s", s[i] + 1);
        }
        divide(1, 1, n, m);
        printf("Case #%d:\n", cs);
        for (int i = 1; i <= n; i++)
            printf("%s\n", s[i] + 1);
    }
}
