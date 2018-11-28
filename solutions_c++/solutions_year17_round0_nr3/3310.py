#include<cstdio>

struct result final {
    size_t max;
    size_t min;
};

result count(size_t n, size_t k) {
    if (n == 1) {
        return {0, 0};
    }
    if (k == 1)
        return {n / 2, n / 2 - 1 + (n % 2)};
    if (n % 2 == 1) {
        return count(n / 2, (k - 1) / 2 + (k - 1) % 2);
    } else {
        if ((k - 1) % 2 == 0) {
            return count(n / 2 - 1, (k - 1) / 2);
        } else {
            return count(n / 2, (k - 1) / 2 + 1);
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);
    int case_no = 0;
    do {
        ++case_no;
        size_t k, n;
        scanf("%lu %lu", &n, &k);
        result res = count(n, k);
        printf("Case #%d: %lu %lu\n", case_no, res.max, res.min);
    } while (case_no != t);
    return 0;
}
