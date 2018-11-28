#include <cstdio>

int main() {
    int t;
    long long n, k, tmp, max_leaf, small_leaves, max, min, pow;
    FILE *fin = fopen("input.in", "r");
    fscanf(fin, "%d", &t);

    for (int setn=1; setn<=t; setn++) {
        printf("Case #%d: ", setn);
        fscanf(fin, "%lld %lld", &n, &k);
        tmp = k;
        pow=1;
        while (tmp >= 2) {
            tmp/=2;
            pow*=2;
        }
        //printf("%d <= k(%d)\n", pow, k);
        max_leaf = n/pow;
        //printf("max leaf: %d\n", max_leaf);
        small_leaves = max_leaf*pow-n+pow-1;
        //printf("# of small leaves: %d/%d\n", small_leaves, pow);
        //printf("# of large leaves: %d/%d\n", pow-small_leaves, pow);
        //printf("answer is %d for range %d ~ %d\n", max_leaf, pow, 2*pow-small_leaves-1);

        if (k >= 2*pow-small_leaves) {
            max_leaf -= 1;
        }
        if (max_leaf % 2 == 0) {
            printf("%lld %lld\n", max_leaf/2, max_leaf/2-1);
        } else {
            printf("%lld %lld\n", max_leaf/2, max_leaf/2);
        }
    }

    return 0;
}
