#include<cstdio>

using namespace std;

void solve(long long int n, long long int k, long long int* y, long long int* z) {
    long long int small, small_num, big, big_num;
    small = (n - 1) / 2;
    big = (n - 1) - small;
    big_num = 1;
    small_num = 1;
    k = k - 1;
    long long int a, a_num, b, b_num, c, c_num, d, d_num;
    while(k > 0) {
        a = b = c = d = 0LL;

        a = (big - 1) / 2; // small
        b = (big - 1) - a; // big

        k -= big_num;
        if(k <= 0) {
            small = a;
            big = b;
            break;
        }

        c = (small - 1) / 2;
        d = (small - 1) - c;
        k -= small_num;
        if(k <= 0) {
            small = c;
            big = d;
            break;
        }

        a_num = b_num = big_num;
        c_num = d_num = small_num;

        big = b;
        small = c;
        big_num = small_num = 0;

        if(a == b) {
            big_num += (a_num + b_num);
        } else {
            big_num += b_num;
            small_num += a_num;
        }

        if(c == d) {
            small_num += (c_num + d_num);
        } else {
            big_num += d_num;
            small_num += c_num;
        }

    }

    *y = big;
    *z = small;
}

int main() {
    int T;
    int cnt = 0;
    long long int N;
    long long int K;

    scanf("%d", &T);

    while(cnt < T) {

        scanf("%lld", &N);
        scanf("%lld", &K);

        long long int y, z;
        solve(N, K, &y, &z);

        cnt++;
        printf("Case #%d: %lld %lld\n", cnt, y, z);
    }
}
