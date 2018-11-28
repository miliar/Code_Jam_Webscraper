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


int div_ceil(int a, int b)
{
    return (a+b-1)/b;
}

int go()
{
    int n,p;
    scanf("%d%d", &n, &p);
    int r[n];
    for(int i=0;i<n;i++)
        scanf("%d", r+i);
    int q[n][p];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<p;j++)
            scanf("%d", &q[i][j]);
        sort(q[i], q[i]+p);
    }
    vector<int> m1[n], m2[n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<p;j++)
        {
            m1[i].push_back(div_ceil(q[i][j] * 10, 11 * r[i]));
            m2[i].push_back(q[i][j] * 10 / (9 * r[i]));
            //printf("%d %d %d\n", q[i][j], m1[i].back(), m2[i].back());
            if(m2[i] < m1[i])
            {
                m1[i].pop_back();
                m2[i].pop_back();
            }
        }
    }
        
    int cur[n];
    for(int i=0;i<n;i++)
        cur[i] = 0;
    int count = 0;
    while(true)
    {
        int M1 = 0, M2 = INF;
        int ii = 0;
        for(int i=0;i<n;i++)
        {
            if (cur[i] == m1[i].size()) return count;
            if (m2[i][cur[i]] < M2) ii = i;
            M1 = max(M1, m1[i][cur[i]]);
            M2 = min(M2, m2[i][cur[i]]);
        }
        if (M1 <= M2)
        {
            count++;
            for(int i=0;i<n;i++) cur[i]++;
        }
        else
        {
            ++cur[ii];
        }
    }
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
        printf("Case #%d: %d\n", test_case, go());
    }
    return 0;
}
