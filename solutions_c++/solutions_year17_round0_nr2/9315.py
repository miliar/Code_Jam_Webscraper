#include <cstdio>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    int i, j, tcase, len, digits[20];
    long long int N, sol, div, ndiv;
    scanf("%d", &T);

    for (tcase = 1; tcase <= T; ++tcase) {
        scanf("%lld", &N);
        div = 1;
        len = 0;

        while (div <= N) {
            div *= 10;
        }

        while (div >= 10) {
            digits[len++] = (N % div) / (div / 10);
            div /= 10;
        }

        for (i = 1; i < len; ++i) {
            if (digits[i] < digits[i - 1]) {
                for (j = i; j < len; ++j) {
                    digits[j] = 9;
                }
                for (j = i - 1; j >= 0; --j) {
                    if (j == 0) {
                        digits[j] = digits[j] - 1;
                        continue;
                    }
                    if (digits[j] - 1 < digits[j - 1]) {
                        digits[j] = 9;
                    }
                    else {
                        --digits[j];
                        break;
                    }
                }
            }
        }

        sol = digits[0];
        for (i = 1; i < len; ++i) {
            sol = sol * 10 + digits[i];
        }

        /*
        sol = N;

        prevdig = (N % div) / (div / 10);
        div /= 10;
        --len;
        while (div >= 10) {
            curdig = (N % div) / (div / 10);
            if (curdig < prevdig) {
                sol = N / div;
                ndiv = 10;
                while (sol / ndiv != 0) {
                    curdig = (sol % ndiv) / (ndiv / 10);
                }
                sol = sol * 10 + (prevdig - 1);
                while (len > 0) {
                    sol = sol * 10 + 9;
                    --len;
                }
                break;
            }
            div /= 10;
            --len;
            prevdig = curdig;
        }
        */

        printf("Case #%d: %lld\n", tcase, sol);
    }
    return 0;
}
