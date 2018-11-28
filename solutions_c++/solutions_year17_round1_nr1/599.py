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

char a[30][30];

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
        int R, C;
        scanf("%d%d", &R, &C);
        for(int r=0;r<R;r++)
            scanf(" %s", a[r]);
        bool first = true;
        for(int r=0;r<R;r++)
        {
            char cur = 0;
            for(int c=0;c<C;c++)
            {
                if(a[r][c] != '?')
                {
                    if (!cur)
                    {
                        for(int cc=0;cc<c;cc++)
                            a[r][cc] = a[r][c];
                    }
                    cur = a[r][c];
                }
                if (cur)
                {
                    a[r][c] = cur;
                }
            }
            if (first && cur)
            {
                first = false;
                for(int rr=0;rr<r;rr++)
                    for(int c=0;c<C;c++)
                        a[rr][c] = a[r][c];
            }
            if (!first && !cur)
            {
                for(int c=0;c<C;c++)
                    a[r][c] = a[r-1][c];
            }
        }
        printf("Case #%d:\n", test_case);
        for(int r=0;r<R;r++) printf("%s\n", a[r]);
    }
    return 0;
}
