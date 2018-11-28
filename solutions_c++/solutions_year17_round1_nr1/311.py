#include <cstdio>
#include <set>

using namespace std;

int t, n, m;
char arr[30][30];

int main() {
    scanf(" %d", &t);
    for (int q = 1; q <= t; q++) {
        scanf(" %d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf(" %c", &arr[i][j]);
            }
        }

        set<int> rows;

        for (int i = 0; i < n; i++) {
            char first = 0;
            for (int j = 0; j < m; j++) {
                if (arr[i][j] != '?') {
                    first = arr[i][j];
                    break;
                }
            }
            if (first == 0) {
                rows.insert(i);
            } else {
                char last = first;
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] == '?') {
                        arr[i][j] = last;
                    } else {
                        last = arr[i][j];
                    }
                }
            }
        }

        int back = 0;
        while (back < n && rows.find(back) != rows.end()) back++;

        for (int i = 0; i < back; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = arr[back][j];
            }
        }

        int last = back;
        for (int i = back; i < n; i++) {
            if (rows.find(i) != rows.end()) {
                for (int j = 0; j < m; j++) {
                    arr[i][j] = arr[last][j];
                }
            } else {
                last = i;
            }
        }

        printf("Case #%d:\n", q);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                printf("%c", arr[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
