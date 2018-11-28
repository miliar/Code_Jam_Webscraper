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

pair<int, int> getNum(int r, int q)
{
    pair<int, int> ans;
    ans.first = (10 * q + (11 * r - 1)) / (11 * r);
    ans.second = (10 * q) / (9 * r);
    return ans;
}

int solve(const vector<int>& r, vector<vector<int> > q)
{
    int n = q.size();    //材料の個数
    int p = q[0].size(); //パッケージの個数

    for(int i=0; i<n; ++i)
        sort(q[i].begin(), q[i].end());

    int ans = 0;
    vector<int> index(n, p-1);
    for(;;){
        vector<pair<int, int> > v(n);
        pair<int, int> range(INT_MIN, INT_MAX);
        for(int i=0; i<n; ++i){
            v[i] = getNum(r[i], q[i][index[i]]);
            range.first = max(range.first, v[i].first);
            range.second = min(range.second, v[i].second);
        }

        if(range.first <= range.second){
            ++ ans;
            for(int i=0; i<n; ++i){
                -- index[i];
                if(index[i] < 0)
                    return ans;
            }
        }
        else{
            int i = max_element(v.begin(), v.end()) - v.begin();
            -- index[i];
            if(index[i] < 0)
                return ans;
        }
    }
}

int main()
{
    int tMax;
    cin >> tMax;

    for(int t=1; t<=tMax; ++t){
        int n, p;
        cin >> n >> p;
        vector<int> r(n);
        for(int i=0; i<n; ++i)
            cin >> r[i];
        vector<vector<int> > q(n, vector<int>(p));
        for(int i=0; i<n; ++i){
            for(int j=0; j<p; ++j){
                cin >> q[i][j];
            }
        }

        int ans = solve(r, q);
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
