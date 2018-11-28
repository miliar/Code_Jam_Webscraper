#include <iostream>
#include <cstdio>
using namespace std;

const int MAXL = 30;
const int MAXD = 10;

int len;
int num[MAXL];
long long f[MAXD][MAXL];

long long getf(int len)
{
    long long sum = 0;
    for (int i = num[len + 1]; i < num[len]; ++i)
        sum += f[i][len];
    if (num[len + 1] <= num[len])
        sum += getf(len - 1);
    return sum;
}

long long calc(long long number)
{
    memset(num, 0, sizeof(num));
    for (len = 0; number > 0; number /= 10)
        num[++len] = number % 10;

    return getf(len);
}

int main()
{
    int TestCase;

    for (int i = 0; i < 10; ++i)
        f[i][1] = 1;

    for (int l = 2; l < 20; ++l)
        for (int d = 0; d < 10; ++d)
            for (int t = d; t < 10; ++t)
                f[d][l] += f[t][l - 1];

    scanf("%d", &TestCase);

    for (int nowTestCase = 1; nowTestCase <= TestCase; ++nowTestCase)
    {
        long long N;
        cin >> N;

        //<=N --> < N
        ++N;

        long long finalCount = calc(N);

        long long l = 2, r = N;
        long long ans = -1;
        while (l <= r)
        {
            long long mid = (l + r) / 2;

            if (calc(mid) < finalCount)
                l = mid + 1;
            else
            {
                r = mid - 1;
                ans = mid;
            }
        }
        
        printf("Case #%d: ", nowTestCase);
        cout << ans - 1 << endl;
    }

    return 0;
}
