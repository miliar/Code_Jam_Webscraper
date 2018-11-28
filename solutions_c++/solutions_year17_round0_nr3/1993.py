#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
#include <iterator>
using namespace std;

pair<long long, long long> solve(long long n, long long k)
{
    for(long long i=1; ; i*=2){
        n -= i;
        if(i < k){
            k -= i;
        }
        else{
            long long len = n / i;
            long long rest = n % i;
            if(rest < k)
                return make_pair((len+1)/2, len/2);
            else
                return make_pair((len+2)/2, (len+1)/2);
        }
    }
}

int main()
{
    int tMax;
    cin >> tMax;

    for(int t=1; t<=tMax; ++t){
        long long n, k;
        cin >> n >> k;
        auto ans = solve(n, k);
        cout << "Case #" << t << ": " << ans.first << ' ' << ans.second << endl;
    }

    return 0;
}