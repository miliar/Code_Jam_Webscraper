#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <algorithm>

typedef double flt;
typedef long long ll;

using namespace std;

struct Layer
{
    ll rad, len;
};

const flt PI = acos(-1);
const int MAXN = 1e+3 + 10;
Layer layers[MAXN];

void solve(int test_number)
{
    int n, k;
    cin >> n >> k;
    for (int q = 0; q < n; ++q)
        cin >> layers[q].rad >> layers[q].len;
    
    sort(layers, layers + n, [] (const Layer &a, const Layer &b) {
        return a.rad > b.rad;
    });
    
    flt maxAns = 0;
    for (int q = 0; q < n - k + 1; ++q)
    {
        flt rad = layers[q].rad;
        flt lens = layers[q].len * rad * 2 * PI;
        vector<flt> vec;
        for (int i = q + 1; i < n; ++i)
            vec.push_back(layers[i].len * layers[i].rad * 2 * PI);
        sort(vec.begin(), vec.end(), std::greater<flt>());
        for (int i = 0; i < k - 1; ++i)
            lens += vec[i];
        
//        cout << q << ' ' << (rad * rad * PI) << ' ' << lens << ' ' << (rad * rad * PI + lens) << endl;
        maxAns = max(maxAns, rad * rad * PI + lens);
    }
    
    cout << "Case #" << test_number << ": " << maxAns << endl;
    
}

int main()
{
//  /*
    freopen("atest.in", "r", stdin);
    freopen("atest.out", "w", stdout);
//  */
    
    int cnt_queries;
    cin >> cnt_queries;
    
    cout.precision(15);
    for (int q = 0; q < cnt_queries; ++q)
    {
        solve(q + 1);
    }
    
    return 0;
}
