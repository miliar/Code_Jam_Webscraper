#include <iostream>
#include <stdio.h>
#include <string.h>
#include <assert.h>

using namespace std;

typedef long long ll;
typedef double flt;

const int MAXN = 1e+2 + 10;
int mat[MAXN][MAXN];
int dist[MAXN];
int speed[MAXN];

bool reach[MAXN];
flt minTime[MAXN];

void solve(int test_number)
{
    int n, cnt_queries;
    cin >> n >> cnt_queries;
    
    for (int q = 0; q < n; ++q)
    {
        cin >> dist[q] >> speed[q];
    }
    
    for (int q = 0; q < n; ++q)
    {
        for (int i = 0; i < n; ++i)
        {
            cin >> mat[q][i];
        }
    }
    
    /*
    cout << "MAT BEGIN" << endl;
    for (int q = 0; q < n; ++q)
    {
        for (int i = 0; i < n; ++i)
            cout << mat[q][i] << ' ';
        cout << endl;
    }
    cout << "MAT END" << endl; // */
    
    int a, b;
    cin >> a >> b;
    
    memset(reach, 0, sizeof(reach)); 
    reach[0] = true;
    minTime[0] = 0;
    for (int q = 0; q < n; ++q)
    {
//        cout << "TIME : " << minTime[q] << ' ' << reach[q] << endl;
        assert(reach[q]);
        int dst = 0;
        for (int i = q + 1; i < n; ++i)
        {
            dst += mat[i - 1][i];
//            cout << "DIST : " << dst << ' ' << dist[q] << endl;
            if (dst <= dist[q])
            {
                if (not reach[i])
                {
                    reach[i] = true;
                    minTime[i] = minTime[q] + 1.0 * dst / speed[q];
                }
                else
                    minTime[i] = min(minTime[i], minTime[q] + 1.0 * dst / speed[q]);
            }
            else
                break;
        }
    }
    
    cout.precision(10);
    cout << "Case #" << test_number << ": " << minTime[n - 1] << endl;
}

int main()
{
//  /*
    freopen("ctest.in", "r", stdin);
//  */
    
    int cnt_tests;
    cin >> cnt_tests;
    
    for (int q = 0; q < cnt_tests; ++q)
    {
        solve(q + 1);
    }
    
    return 0;
}
