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

ll print(vector<int>& d)
{
    for (int di : d)
        printf("%d", di);
    printf("\n");
}

ll solve(ll n)
{
    vector<int> d;
    while(n)
    {
        d.push_back(n%10);
        n /= 10;
    }
    reverse(d.begin(), d.end());

    bool change;
    do
    {
        change = false;
        for(int i=0;i<d.size()-1;i++)
            if(d[i]>d[i+1])
            {
                change=true;
                d[i]--;
                for(int j=i+1;j<d.size();j++)
                    d[j] = 9;
            }
    } while(change);

    ll res = 0;
    for(int di : d)
        res = res * 10 + di;
    return res;
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
        ll n;
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", test_case, solve(n));
    }
    return 0;
}
