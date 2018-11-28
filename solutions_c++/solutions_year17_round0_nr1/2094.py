#include <iostream>
#include <stdio.h>
#include <string>

typedef long long ll;
typedef float flt;

using namespace std;

const int MAXN = 1e+3 + 10;
bool face[MAXN];

void solve(int test_number)
{
    string str;
    int k;
    cin >> str >> k;
    int n = str.size();
    for (int q = 0; q < n; ++q)
    {
        face[q] = str[q] == '+';
    }
    
    int res = 0;
    for (int q = 0; q <= n - k; ++q)
    {
        if (not face[q])
        {
            ++res;
            for (int i = q; i < q + k; ++i)
                face[i] = not face[i];
        }
    }
    
    /*
    for (int q = 0; q < n; ++q)
        cout << face[q] << ' ';
    cout << endl; // */
    
    for (int q = n - k + 1; q < n; ++q)
    {
        if (not face[q])
        {
            cout << "Case #" << test_number << ": " << "IMPOSSIBLE" << endl;
            return;
        }
    }
    
    cout << "Case #" << test_number << ": " << res << endl;
}

int main()
{
  /*
    freopen("atest.in", "r", stdin);
    freopen("atest.out", "w", stdout);
//  */
    
    int cnt_queries;
    cin >> cnt_queries;
    for (int _q = 0; _q < cnt_queries; ++_q)
    {
        solve(_q + 1);
    }
    
    return 0;
}
