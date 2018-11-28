#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int MAXN = 26;
int T, R, C;
char grid[MAXN][MAXN];

void go()
{
    for (int i = 0; i < R; i++)
    {
        char c = '$';
        for (int j = 0; j < C; j++)
        {
            if (grid[i][j] == '?')
            {
                if (c != '$')
                    grid[i][j] = c;
            }
            else
                c = grid[i][j];
        }
        c = '$';
        for (int j = C - 1; j >= 0; j--)
        {
            if (grid[i][j] == '?')
            {
                if (c != '$')
                    grid[i][j] = c;
            }
            else
                c = grid[i][j];
        }
    }

    for (int i = 0; i < R; i++)
        if (grid[i][0] != '?')
            for (int j = i + 1; j < R; j++)
            {
                if (grid[j][0] == '?')
                    memcpy(grid[j], grid[i], sizeof(grid[i]));
                else
                    break;
            }

    for (int i = R - 1; i >= 0; i--)
        if (grid[i][0] != '?')
            for (int j = i - 1; j >= 0; j--)
            {
                if (grid[j][0] == '?')
                    memcpy(grid[j], grid[i], sizeof(grid[i]));
                else
                    break;
            }
}

int main()
{
	ios::sync_with_stdio(0);

    freopen("A.in", "r", stdin);
    freopen("Aout.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> R >> C;
        for (int i = 0; i < R; i++)
            cin >> grid[i];

        go();
        cout << "Case #" << t << ":" << "\n";
        for (int i = 0; i < R; i++)
            cout << grid[i] << "\n";
    }

	return 0;
}
