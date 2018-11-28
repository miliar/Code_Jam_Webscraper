#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
#include <complex>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef complex<double> cpx;
const int INF = numeric_limits<int>::max();

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
        int n, C, t;
        scanf("%d%d%d", &n, &C, &t);
        int s[n+1];
        memset(s, 0, sizeof(s));
        int c[C+1];
        memset(c, 0, sizeof(c));
        int maxPerCust = 0;
        for(int i=0;i<t;i++)
        {
            int p, b;
            scanf("%d%d", &p, &b);
            s[p]++;
            c[b]++;
            maxPerCust = max(maxPerCust, c[b]);
        }
        int rides = 0;
        for(int i=1, cur=0;i<=n;i++)
        {
            cur += s[i];
            rides = max(rides, (cur + i-1) / i);
        }
        rides = max(rides, maxPerCust);

        int promotions = 0;
        for(int i=1;i<=n;i++)
        {
            promotions += max(0, s[i] - rides);
        }
        printf("Case #%d: %d %d\n", test_case, rides, promotions);
    }
    return 0;
}
