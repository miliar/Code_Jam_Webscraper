#include <iostream>
#include <stdio.h>
#include <iterator>
#include <vector>
#include <algorithm>

typedef double flt;
typedef long long ll;

using namespace std;

void solve(int test_number)
{
    int n, k;
    cin >> n >> k;
    
    flt u;
    cin >> u;
    vector<flt> vec;
    for (int q = 0; q < n; ++q)
        vec.push_back(*istream_iterator<flt>(cin));
    
    sort(vec.begin(), vec.end());
    vec.push_back(1);
    for (int q = 0; q < n; ++q)
    {
        flt diff = vec[q + 1] - vec[q];
        flt sumadd = min(u, diff * (q + 1)), add = sumadd / (q + 1);
//        cout << diff << ' ' << sumadd << ' ' << add << endl;
        for (int i = 0; i <= q; ++i)
            vec[i] += add;
        u -= sumadd;
    }
    
    flt mul = 1;
    for (flt x : vec)
        mul *= x;
    
    cout.precision(15);
    cout << "Case #" << test_number << ": " << mul << endl;
}

int main()
{
//  /*
    freopen("ctest.in", "r", stdin);
    freopen("ctest.out", "w", stdout);
//  */
    
    int cnt_tests;
    cin >> cnt_tests;
    
    for (int q = 0; q < cnt_tests; ++q)
    {
        solve(q + 1);
    }
    
    return 0;
}
