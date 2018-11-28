#include <iostream>
#include <cstring>
#include <cstdlib>

char cake[30][30], color[30][30], first[30];
int T, r, c;

using namespace std;

int main()
{
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> r >> c;
        memset(cake, 0, sizeof(cake));
        memset(color, 0, sizeof(color));
        memset(first, 0, sizeof(first));
        for (int i = 0; i < r; ++i)
            cin >> cake[i];
        for (int i = 0; i < c; ++i)
            for (int j = 0; j < r; ++j)
                if (cake[j][i] != '?')
                {
                    first[i] = cake[j][i];
                    break;
                }
        for (int i = 0; i < c; ++i)
            if (first[i])
            {
                char now = first[i];
                for (int j = 0; j < r; ++j)
                {
                    if (cake[j][i] != '?' && cake[j][i] != now)
                        now = cake[j][i];
                    color[j][i] = now;
                }
            }
            else if (i > 0 && color[0][i - 1])
                for (int j = 0; j < r; ++j)
                    color[j][i] = color[j][i - 1];
        for (int i = c - 1; i >=0 ; --i)
            if (!color[0][i])
                for (int j = 0; j < r; ++j)
                    color[j][i] = color[j][i + 1];
        cout << "Case #" << t << ":" << endl;
        for (int i = 0; i < r; ++i)
            cout << color[i] << endl;
    }
    return 0;
}
