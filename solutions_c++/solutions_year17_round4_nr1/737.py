#include <iostream>
#include <stdio.h>
#include <assert.h>

using namespace std;

int d[4];

int divUp(int a, int b)
{
    return (a + b - 1) / b;
}

void printAnswer(int tn, int a)
{
    cout << "Case #" << tn << ": " << a << endl;
}

void solve(int test_number)
{
    int n, p;
    cin >> n >> p;
    
    d[0] = d[1] = d[2] = d[3] = 0;
    for (int q = 0; q < n; ++q)
    {
        int x;
        cin >> x;
        d[x % p] += 1;
    }
    
    if (p == 2)
    {
        printAnswer(test_number, d[0] + divUp(d[1], 2));
    }
    else if (p == 3)
    {
        int u = min(d[1], d[2]),
            v = max(d[1], d[2]) - u;
        printAnswer(test_number, d[0] + u + divUp(v, 3));
    }
    else if (p == 4)
    {
        assert(false);
    }
    else
        assert(false);
    
}

int main()
{
//  /*
//    freopen("tmp", "r", stdin);
    freopen("atest.in", "r", stdin);
    freopen("atest.out", "w", stdout);
//  */
    
    int cnt_tests;
    cin >> cnt_tests;
    
    for (int q = 0; q < cnt_tests; ++q)
    {
        solve(q + 1);
    }
    
    
    return 0;
}
