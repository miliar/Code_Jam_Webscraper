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

char buf[1005];
bool a[1005];

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
        int k;
        scanf(" %s%d", buf, &k);
        int n = strlen(buf);
        for(int i=0;i<n;i++)
            a[i] = buf[i] == '+';
        int flips = 0;
        for(int i=0;i<n;i++)
            if(!a[i])
            {
                if (i + k > n)
                {
                    flips = -1;
                    break;
                }
                for(int j=i;j<i+k;j++)
                    a[j] = !a[j];
                flips++;
            }
        printf("Case #%d: ", test_case);
        if (flips == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", flips);
    }
    return 0;
}
