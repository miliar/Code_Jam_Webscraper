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

int dp[105][105][105][105];
int g[5];

void set_max(int& a, int b)
{
    a = max(a, b);
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
        memset(g, 0, sizeof(g));
        memset(dp, 0, sizeof(dp));

        int n, p;
        scanf("%d%d", &n, &p);
        for(int i=0;i<n;i++)
        {
            int x;
            scanf("%d", &x);
            x %= p;
            g[x]++;
        }
        //for(int i=0;i<p;i++) printf("%d: %d\n", i, g[i]);

        dp[0][0][0][0] = 0;
        for(int g0=0;g0<=g[0];g0++)
            for(int g1=0;g1<=g[1];g1++)
                for(int g2=0;g2<=g[2];g2++)
                    for(int g3=0;g3<=g[3];g3++)
                    {
                        int cur = dp[g0][g1][g2][g3];
                        int left = (g1 + g2*2 + g3*3) % p;
                        bool fresh = left == 0;
                        int next = cur + fresh;
                        //printf("%d %d %d %d: %d %d\n", g0, g1, g2, g3, cur, left);
                        set_max(dp[g0+1][g1][g2][g3], next);
                        set_max(dp[g0][g1+1][g2][g3], next);
                        set_max(dp[g0][g1][g2+1][g3], next);
                        set_max(dp[g0][g1][g2][g3+1], next);
                    }
        int res = dp[g[0]][g[1]][g[2]][g[3]];
        printf("Case #%d: %d\n", test_case, res);
    }
    return 0;
}
