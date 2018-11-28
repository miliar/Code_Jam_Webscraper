#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>


void solve()
{
    long long N, K;
    std::cin >> N >> K;
    int p = -1;
    {
        long long copyK = K;
        while(copyK)
        {
            copyK >>= 1; 
            p++;
        }
    }

    long long rest = (N - (1 << p) + 1);
    long long div = rest >> p, mod = rest & ((1 << p) - 1);
    if(K - (1 << p) >= mod)
        div--;

    printf("%lld %lld", (div + 1) / 2, div / 2);
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }

    return 0;
}
