#include<cstdio>

int main() {
    int t;
    scanf("%d", &t);
    int case_no = 0;
    do {
        ++case_no;

        int d, n;
        int l = 0;
        int m = 0;
        scanf("%d %d", &d, &n);
        for (int i = 0; i < n; ++i) {
            int k, s;
            scanf("%d %d", &k, &s);
            int ll = d - k;
            if (i == 0 || (long long)ll * m > (long long)l * s) {
                l = ll;
                m = s;
            }
        }

        printf("Case #%d: %.6f\n", case_no, (double)d * m / l);
    } while (case_no != t);
    return 0;
}
