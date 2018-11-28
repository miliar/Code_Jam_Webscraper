#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int t;

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        int r, c;
        char cake[25][26];

        scanf("%d %d", &r, &c);
        for (int i = 0; i < r; ++i) {
            scanf("%s", cake[i]);
        }

        for (int i = 0; i < r; ++i) {
            bool row_empty = true;
            int last_end = 0;
            char c_last = '?';

            for (int j = 0; j < c; ++j) {
                if (cake[i][j] != '?') {
                    row_empty = false;
                    c_last = cake[i][j];
                    fill(cake[i]+last_end, cake[i]+j, c_last);
                    last_end = j+1;
                }
            }
            fill(cake[i]+last_end, cake[i]+c, c_last);
            if (i > 0 && row_empty) {
                copy(cake[i-1], cake[i-1]+c, cake[i]);
            }
        }

        for (int i = r-1; i > 0; --i) {
            bool prev_row_empty = true;

            for (int j = 0; j < c; ++j) {
                if (cake[i-1][j] != '?') {
                    prev_row_empty = false;
                }
            }
            if (prev_row_empty) {
                copy(cake[i], cake[i]+c, cake[i-1]);
            }
        }

        printf("Case #%d:\n", tc);
        for (int i = 0; i < r; ++i) {
            puts(cake[i]);
        }
    }
}
