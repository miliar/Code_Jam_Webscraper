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
        printf("Case #%d: ", test_case);
        ll n, p;
        scanf("%lld%lld", &n, &p);
        map<ll, ll> q;
        q[n] = 1;
        while(true)
        {
            auto it = --q.end();
            ll s = it->first, f = it->second;
            q.erase(it);
            ll s1 = (s-1)/2, s2 = (s-1) - s1;
            if(p <= f)
            {
                printf("%lld %lld\n", s2, s1);
                break;
            }
            p -= f;
            if(s1) q[s1] += f;
            if(s2) q[s2] += f;
        }
    }
    return 0;
}
