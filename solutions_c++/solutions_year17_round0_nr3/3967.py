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

struct cmp
{
    bool operator()(pll &a, pll &b)
    {
        return a.first < b.first || a.first == b.first && a.second > b.second;
    }
};

void process()
{
    ll n, k, i;
    ll n0, p0, n1, n2, p1, p2;
    pll a;
    priority_queue<pll, vector<pll>, cmp> q;
    scanf("%lld %lld", &n, &k);

    q.push(make_pair(n, 0LL));

    for (i = 0; i < k; ++i)
    {
        a = q.top();
        q.pop();
        n0 = a.first;
        p0 = a.second;

        p1 = p0;
        p2 = p1 + ((n0 - 1LL) >> 1LL);
        n1 = p2 - p1;
        n2 = n0 - n1 - 1LL;

        q.push(make_pair(n1, p1));
        q.push(make_pair(n2, p2));
    }

    printf("%lld %lld\n", n2, n1);
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