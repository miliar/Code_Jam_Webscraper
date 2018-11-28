#pragma warning(disable:4996)

#include "bits/stdc++.h"

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
#define max(a, b) ((a)>(b)?(a):(b))
#define min(a, b) ((a)<(b)?(a):(b))
#define MOD 1000000007
#define MAXINT 0x3f3f3f3f
#define ERR 1e-10

int caseNum, totalCaseNum;

void process()
{
    char ss[1001];
    bool s[1001];
    int n, k, i, j, cnt = 0;

    scanf("%s %d", ss, &k);
    n = strlen(ss);
    for (i = 0; i < n; ++i) s[i] = (ss[i] == '+');

    for (i = 0; i < n - k + 1; ++i)
    {
        if (!s[i])
        {
            ++cnt;
            for (j = i; j < i + k; ++j) s[j] = !s[j];
        }
    }

    for (i = n - k + 1; i < n; ++i)
    {
        if (!s[i])
        {
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    printf("%d\n", cnt);
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &totalCaseNum);
    for (caseNum = 1; caseNum <= totalCaseNum; ++caseNum)
    {
        printf("Case #%d: ", caseNum);
        process();
    }

    return 0;
}