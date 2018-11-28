#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

typedef long long ll;

int num[20];
ll base[20];

int decompose(ll N)
{
    int digits = 0;

    while ( N ) {
        num[digits++] = N%10;
        N /= 10;
    }

    return digits;
}

int main()
{
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Ti = 1; Ti <= T; Ti++) {
        ll N;
        scanf("%lld", &N);

        int digits = decompose(N);

        base[0] = 1;
        for (int di = 1; di < digits; di++)
            base[di] = base[di-1]*10+1;

        ll ans = 0;

        int cnt = 0;

        for (int di = digits-1; di >= 0; di--)
            for (; cnt < 9 && ans+base[di] <= N; cnt++)
                ans += base[di];

        printf("Case #%d: %lld\n", Ti, ans);
    }
}
