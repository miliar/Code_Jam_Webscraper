#include <stdio.h>

int T;
long long n;
long long k;

int i;
int top;
long long num[10];
long long count[10];

void add(long long x, long long c)
{
    if (x == 0) {
        return;
    }
    if (c == 0) {
        return;
    }

    for (int j = i; j < top; j = (j + 1) % 10) {
        if (num[j] == x) {
            count[j] += c;
            return;
        }
    }
    num[top] = x;
    count[top] = c;
    top = (top + 1) % 10;
}

int main()
{
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        scanf("%lld%lld", &n, &k);

        int i = 0;
        top = 1;
        num[0] = n;
        count[0] = 1;
        k--;

        for (; k > 0; i = (i + 1) % 10) {
            //printf("==== debug %d %d ====\n", i, k);
            //for (int x = i; x != top; x = (x + 1) % 10) {
            //    printf("debug: %lld %lld\n", num[x], count[x]);
            //}

            if (i == top) {
                break;
            }

            if (count[i] > k) {
                add(num[i] / 2, k);
                add((num[i] - 1) / 2, k);

                count[i] -= k;
                k = 0;
                break;
            } else {
                //printf("    debug: %d %d %d\n", num[i], count[i], k);
                //printf("    debug: %d %d\n", num[i] / 2, (num[i] - 1) / 2);
                add(num[i] / 2, count[i]);
                add((num[i] - 1) / 2, count[i]);
                k -= count[i];
                count [i] = 0;
            }
        }

        //printf("==== debug %d %d ====\n", i, k);
        //for (int x = i; x != top; x = (x + 1) % 10) {
        //    printf("debug: %lld %lld\n", num[x], count[x]);
        //}

        printf("Case #%d: %lld %lld\n", z, num[i] / 2, (num[i] - 1) / 2);
    }
    
	return 0;
}

