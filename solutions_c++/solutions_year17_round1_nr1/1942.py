#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <ctime>
#include <cmath>
// #include <tuple> // c++11
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int MAX_N = 26;
int R, C;
char field[MAX_N][MAX_N];
bool empty[MAX_N];

void solve()
{
    fill(empty, empty + R, true);
    for (int i = 0; i < R; ++i)
    {
        int s = 0;
        for (int j = 0; j < C; ++j) 
        {
            if (field[i][j] != '?') {
                empty[i] = false;
                while (s <= j) field[i][s++] = field[i][j];
            }
        }
        while (!empty[i] && s < C) {
            field[i][s] = field[i][s - 1]; ++s;
        }
        if (empty[i] && i > 0 && !empty[i-1])
        {
            empty[i] = false;
            for (int j = 0; j < C; ++j)
            {
                field[i][j] = field[i-1][j];
            }
        }
    }
    for (int i = R - 2; i >= 0; i--)
    {
        if (empty[i])
        {
            for (int j = 0; j < C; ++j)
            {
                field[i][j] = field[i+1][j];
            }
        }
    }
    for (int i = 0; i < R; ++i)
    {
        for (int j = 0; j < C; ++j)
        {
            printf("%c", field[i][j]);
        }
        printf("\n");
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) scanf(" %c", &field[i][j]);
        printf("Case #%d:\n", t);
        
        solve();
    }

    return 0;
}
