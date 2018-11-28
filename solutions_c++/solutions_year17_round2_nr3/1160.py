#include<cstdio>

int main() {
    int t;
    scanf("%d", &t);
    int case_no = 0;
    double r[101];
    int d[101], e[101], s[101];
    do {
        ++case_no;
        int n, q;
        scanf("%d %d", &n, &q);
        for (int i = 0; i < n; ++i) {
            scanf("%d %d", &e[i], &s[i]);
        }
        int dist;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                scanf("%d", &dist);
                if (j == i + 1)
                    d[i] = dist;
            }
        }

        int start, end;
        scanf("%d %d", &start, &end);
        --start;
        --end;

        for (int i = 0; i < n; ++i)
            r[i] = -100;

        for (int i = n - 2; i >= 0; --i) {
            double time = 0.0;
            e[i] -= d[i];
            time += (double)d[i] / s[i];
            for (int j = i + 1; j < n && e[i] >= 0; ++j) {
                if (j == n - 1) {
                    if (r[i] < 0.0 || r[i] > time)
                        r[i] = time;
                }
                if (r[j] > 0.0 && (r[i] > (time + r[j]) || r[i] < 0.0)) {
                    r[i] = time + r[j];
                }
                e[i] -= d[j];
                time += (double)d[j] / s[i];
            }
        }

        printf("Case #%d: %.6f\n", case_no, r[0]);
    } while (case_no != t);
    return 0;
}
