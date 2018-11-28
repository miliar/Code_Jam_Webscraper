#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

struct ColorNum
{
    char color;
    int num;
};

bool operator<(const ColorNum& cn1, const ColorNum& cn2)
{
    return cn1.num > cn2.num;
}

void solve()
{
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    // r, y, b
    ColorNum colors[3];
    colors[0].color = 'R';
    colors[0].num = r;
    colors[1].color = 'Y';
    colors[1].num = y;
    colors[2].color = 'B';
    colors[2].num = b;
    sort(colors, colors + 3);

    if (colors[0].num > (colors[1].num + colors[2].num))
    {
        cout << "IMPOSSIBLE";
        return;
    }

    cout << colors[0].color;
    --colors[0].num;
    int prev = 0;
    while (colors[0].num > 0 || colors[1].num > 0 || colors[2].num > 0)
    {
        int hcount = -1;
        int best = -1;
        for (int i = 0; i < 3; ++i)
        {
            if (i == prev)
                continue;
            if (colors[i].num > hcount) {
                hcount = colors[i].num;
                best = i;
            }
        }
        cout << colors[best].color;
        --colors[best].num;
        prev = best;
    }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}