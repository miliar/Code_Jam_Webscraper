#include<cstdio>

int main() {
    int t;
    scanf("%d", &t);
    int case_no = 0;
    do {
        ++case_no;
        int n, r, o, y, g, b, v;
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        if (r > b + y || b > r + y || y > r + b) {
            printf("Case #%d: IMPOSSIBLE\n", case_no);
        } else {
            printf("Case #%d: ", case_no);
            int count[3];
            count[0] = r;
            count[1] = b;
            count[2] = y;
            char ch[3];
            ch[0] = 'R';
            ch[1] = 'B';
            ch[2] = 'Y';
            int first = -1;
            int but = -1;
            while (1) {
                int max = 0;
                if (but == 0) {
                    max = 1;
                }
                if ((count[1] > count[max] || (count[1] == count[max] && first == 1))&& but != 1) {
                    max = 1;
                }
                if ((count[2] > count[max] || (count[2] == count[max] && first == 2))&& but != 2) {
                    max = 2;
                }
                if (count[max] == 0) {
                    break;
                }
                printf("%c", ch[max]);
                --count[max];
                but = max;
                if (first == -1) {
                    first = max;
                }
            }
            printf("\n");
        }
    } while (case_no != t);
    return 0;
}
