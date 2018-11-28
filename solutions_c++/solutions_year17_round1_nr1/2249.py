#include <cstdio>
#include <queue>
using namespace std;

int r, c, tc;
char s[25][25];

int main() {
    scanf("%d", &tc);
    for (int tcase = 1; tcase <= tc; tcase++) {
        scanf("%d %d", &r, &c);
        queue<int> emp;
        for (int i = 0; i < r; i++) {
            char line[25];
            scanf("%s", line);
            int last_index = 0;
            char last_ch = '?';
            for (int j = 0; j < c; j++) {
                if (line[j] != '?') {
                    for (int k = last_index; k <= j; k++) {
                        s[i][k] = line[j];
                    }
                    last_index = j + 1;
                    last_ch = line[j];
                }
            }
            if (last_index == 0) {
                emp.push(i);
            } else if (last_index < c) {
                for (int k = last_index; k <= c; k++) {
                    s[i][k] = last_ch;
                }
            }
        }
        printf("Case #%d:\n", tcase);
        for (int i = 0; i < r; i++) {
            int select = i, cnt = 0;
            while (!emp.empty() && emp.front() == i + cnt) {
                cnt++;
                emp.pop();
            }
            select = i+cnt == r? i - 1 : i + cnt;
            cnt = i+cnt == r? cnt : cnt + 1;
            i = cnt? i + cnt - 1 : i;
            while (cnt) {
                for (int j = 0; j < c; j++) {
                    printf("%c", s[select][j]);
                }
                cnt--;
                printf("\n");
            }
        }
    }
    return 0;
}
