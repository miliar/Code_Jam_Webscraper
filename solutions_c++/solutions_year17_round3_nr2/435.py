#include <iostream>
#include <stdio.h>
#include <string.h>

typedef double flt;
typedef long long ll;

using namespace std;

const int MAXN = 720 * 2;
const int NEED = 720;
int pos[MAXN][MAXN][2];

bool white[MAXN];
bool black[MAXN];

void update(int row, int col)
{
    int other = 1 - col;
    for (int q = other; q < MAXN; ++q)
    {
        // consider pos[row][q][col]
        pos[row][q][col] = pos[row - 1][q - other][col];
        if (pos[row - 1][q - other][1 - col] != -1 and (pos[row][q][col] == -1 or pos[row - 1][q - other][1 - col] < pos[row][q][col]))
            pos[row][q][col] = pos[row - 1][q - other][1 - col] + 1;
    }
}

void solve(int test_number)
{
    int u, v;
    cin >> u >> v;
    
    memset(white, 0, sizeof(white));
    memset(black, 0, sizeof(black));
    for (int q = 0; q < u; ++q)
    {
        int a, b;
        cin >> a >> b;
        for (int i = a; i < b; ++i)
            white[i] = true;
    }
    
    for (int q = 0; q < v; ++q)
    {
        int a, b;
        cin >> a >> b;
        for (int i = a; i < b; ++i)
            black[i] = true;
    }
    
    /*
    for (int q = 0; q < MAXN; ++q)
        cout << white[q];
    cout << endl;
    for (int q = 0; q < MAXN; ++q)
        cout << black[q];
    cout << endl; // */
    
    int minAns = MAXN * 2;
    if (not white[0])
    {
        memset(pos, -1, sizeof(pos));
        pos[0][1][0] = 0;
        for (int q = 1; q < MAXN; ++q)
        {
            if (white[q])
                update(q, 1);
            else if (black[q])
                update(q, 0);
            else
            {
                update(q, 0);
                update(q, 1);
            }
        }
        
        if (pos[MAXN - 1][NEED][0] != -1)
            minAns = min(minAns, pos[MAXN - 1][NEED][0]);
        if (pos[MAXN - 1][NEED][1] != -1)
            minAns = min(minAns, pos[MAXN - 1][NEED][1] + 1);
    }
    if (not black[0])
    {
        memset(pos, -1, sizeof(pos));
        pos[0][0][1] = 0;
        for (int q = 1; q < MAXN; ++q)
        {
            if (white[q])
                update(q, 1);
            else if (black[q])
                update(q, 0);
            else
            {
                update(q, 0);
                update(q, 1);
            }
        }
        
        /*
        for (int q = 0; q < MAXN; ++q)
            cout << pos[q][0][1] << ' ';
        cout << endl; // */
        
        
        if (pos[MAXN - 1][NEED][0] != -1)
            minAns = min(minAns, pos[MAXN - 1][NEED][0] + 1);
        if (pos[MAXN - 1][NEED][1] != -1)
            minAns = min(minAns, pos[MAXN - 1][NEED][1]);
    }
    
    
    cout << "Case #" << test_number << ": " << minAns << endl;
}

int main()
{
//  /*
    freopen("btest.in", "r", stdin);
    freopen("btest.out", "w", stdout);
//  */
    
    int cnt_tests;
    cin >> cnt_tests;
    
    for (int q = 0; q < cnt_tests; ++q)
    {
        solve(q + 1);
    }
    
    return 0;
}
