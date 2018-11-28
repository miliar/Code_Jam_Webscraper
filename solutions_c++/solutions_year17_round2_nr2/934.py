#include <cstdio>
#include <string>
#include <algorithm>

std::string q;

char wyn[1007];

bool isCompatibile(char a, char b) {
    if (a == b)
        return false;
    if (a == 'R') {
        return b != 'O' && b != 'V';
    } else if (a == 'O') {
        return b == 'B';
    } else if (a == 'Y') {
        return b != 'O' && b != 'G';
    } else if (a == 'G') {
        return b == 'R';
    }
    return b != 'V' && b != 'G';
}

void print(char a, char b, int count, bool& isFirst) {
    if (isFirst) {
        isFirst = false;
        for (int i = 0; i < count; i++) {
            printf("%c%c", a, b);
            q = q + a;
            q = q + b;
        }
    }
    printf("%c", a);
    q = q + a;
}

int main() {
    int T;
    scanf("%d", &T);
    int N, R, O, Y, G, B, V;
    bool firstR, firstY, firstB;
    for (int t = 1; t <= T; t++) {
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        for (int i = 0; i < N; i++)
            wyn[i] = 0;
        q = "";
        int sum = R + O + Y + G + B + V;
        firstB = firstR = firstY = true;
        if (R > G || G == 0) {
            R -= G;
        } else if (R == G) {
            if (sum - R - G == 0) {
                printf("Case #%d: ", t);
                for (int i = 0; i < R; i++) {
                    printf("RG");
                }
                printf("\n");
                continue;
            } else {
                printf("Case #%d: Impossible\n", t);
                continue;
            }
        } else {
            printf("Case #%d: Impossible\n", t);
            continue;
        }

        if (Y > V || V == 0) {
            Y -= V;
        } else if (Y == V) {
            if (sum - Y - V == 0) {
                printf("Case #%d: ", t);
                for (int i = 0; i < Y; i++) {
                    printf("YV");
                }
                printf("\n");
                continue;
            } else {
                printf("Case #%d: Impossible\n", t);
                continue;
            }
        } else {
            printf("Case #%d: Impossible\n", t);
            continue;
        }

        if (B > O || O == 0) {
            B -= O;
        } else if (B == O) {
            if (sum - B - O == 0) {
                printf("Case #%d: ", t);
                for (int i = 0; i < B; i++) {
                    printf("BO");
                }
                printf("\n");
                continue;
            } else {
                printf("Case #%d: Impossible\n", t);
                continue;
            }
        } else {
            printf("Case #%d: Impossible\n", t);
            continue;
        }

        std::pair<int, char> tab[] = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
        std::sort(tab, tab + 3);

        int smallCount = tab[0].first;

        if (tab[2].first > R + Y + B - tab[2].first) {
            printf("Case #%d: Impossible\n", t);
            continue;
        } else {
            for (int i = 0; i < tab[2].first; i++)
                wyn[i * 2] = tab[2].second;
            for (int i = 0; i < tab[1].first; i++)
                wyn[i * 2 + 1] = tab[1].second;
            for (int i = 0; i < R + Y + B; i++)
                if (wyn[i] == 0 && wyn[i - 1] != tab[0].second) {
                    wyn[i] = tab[0].second;
                    smallCount--;
                } else if (wyn[i] == 0)
                    break;
        }
        printf("Case #%d: ", t);
        char last = tab[0].second;
        int test = R + Y + B - smallCount;
        for (int i = 0; i < test; i++) {
            if (last != tab[0].second && smallCount != 0) {
                if (tab[0].second == 'R') {
                    print('R', 'G', G, firstR);
                } else if (tab[0].second == 'Y') {
                    print('Y', 'V', V, firstY);
                } else {
                    print('B', 'O', O, firstB);
                }
                smallCount--;
            }
            if (wyn[i] == 'R') {
                print('R', 'G', G, firstR);
                last = 'R';
            } else if (wyn[i] == 'Y') {
                print('Y', 'V', V, firstY);
                last = 'Y';
            } else {
                print('B', 'O', O, firstB);
                last = 'B';
            }
        }
        printf("\n");
        if (!isCompatibile(q[0], q[N - 1])) {
            printf("Oops\n");
            continue;
        }
        if (q.length() != N) {
            printf("Oops\n");
            continue;
        }
        for (int i = 1; i < N; i++) {
            if (!isCompatibile(q[i], q[i - 1])) {
                printf("Oops\n");
                continue;
            }
        }
    }
    return 0;
}