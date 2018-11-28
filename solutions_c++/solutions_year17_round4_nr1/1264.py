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

map<pair<int, vector<int> >, int> memo;

int dfs(int rest, vector<int>& v)
{
    if(memo.find(make_pair(rest, v)) != memo.end())
        return memo[make_pair(rest, v)];

    int p = v.size();
    if(v == vector<int>(p, 0))
        return 0;

    int ans = 0;
    for(int i=1; i<p; ++i){
        if(v[i] > 0){
            -- v[i];
            ans = max(ans, dfs((rest + i) % p, v));
            ++ v[i];
        }
    }
    if(rest == 0)
        ++ ans;

    return memo[make_pair(rest, v)] = ans;
}

int solve(int p, const vector<int>& g)
{
    int n = g.size();
    vector<int> v(p);
    for(int i=0; i<n; ++i)
        ++ v[g[i]%p];

    int ans = v[0];
    v[0] = 0;

    memo.clear();
    ans += dfs(0, v);
    return ans;
}
 
int main()
{
    int T;
    cin >> T;
    for(int t=1; t<=T; ++t){
        int n, p;
        cin >> n >> p;
        vector<int> g(n);
        for(int i=0; i<n; ++i)
            cin >> g[i];

        int ans = solve(p, g);
        cout << "Case #" << t << ": " << ans << endl;
    }
 
    return 0;
}