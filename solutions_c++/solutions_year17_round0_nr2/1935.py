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

long long solve(long long n)
{
    int len = to_string(n).size();

    string s(len, ' ');
    for(int i=0; i<len; ++i){
        for(char c='9'; ; --c){
            for(int j=i; j<len; ++j)
                s[j] = c;
            if(s <= to_string(n))
                break;
        }
    }

    return stoll(s);
}

int main()
{
    int tMax;
    cin >> tMax;

    for(int t=1; t<=tMax; ++t){
        long long n;
        cin >> n;
        long long ans = solve(n);
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}