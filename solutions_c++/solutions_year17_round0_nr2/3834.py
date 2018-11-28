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
    char a[20], b[20];
    int i, n;

    scanf("%s", a);
    n = strlen(a);

    b[n-1] = a[n-1];
    for (i = 0; i < n - 1; ++i)
    {
        if (a[i] > a[i + 1])
        {
            b[i] = a[i] - 1;
            break;
        }
        b[i] = a[i];
    }
    for (++i; i < n; ++i) b[i] = '9';

    for (i = n - 1; i > 0; --i)
    {
        if (b[i - 1] > b[i])
        {
            b[i] = '9';
            --b[i - 1];
        }
    }

    b[n] = NULL;
    for (i = 0; i < n; ++i)
    {
        if (b[i] != '0') break;
    }

    printf("%s\n", b + i);
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