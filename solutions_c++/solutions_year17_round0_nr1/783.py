#include <bits/stdc++.h>

const int N = 1e3 + 100;

int n;
char state[N];
int len;

void init() {
    scanf("%s%d", state + 1, &len);
    n = std::strlen(state + 1);
}

void work() {
    int answer = 0;
    for (int i = 1; i + len - 1 <= n; i++) {
        if (state[i] == '-') {
            answer++;
            for (int j = i; j <= i + len - 1; j++) {
                if (state[j] == '-') {
                    state[j] = '+';
                } else {
                    state[j] = '-';
                }
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        if (state[i] == '-') {
            printf("IMPOSSIBLE\n");
            return ;
        }
    }
    std::cout << answer << std::endl;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int testCount;
    std::cin >> testCount;
    for (int i = 1; i <= testCount; i++) {
        printf("Case #%d: ", i);
        init();
        work();
    }

    return 0;
}
