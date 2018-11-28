#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);
    int t;
    cin >> t;
    for(int cas = 1; cas <= t; cas++)
    {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        pair<int, char>uni[100];
        uni[0] = {r, 'R'};
        uni[1] = {y, 'Y'};
        uni[2] = {b, 'B'};
        sort(uni, uni + 3);
        printf("Case #%d: ", cas);
        if(uni[2].first > n - uni[2].first)
            printf("IMPOSSIBLE\n");
        else
        {
            while(uni[0].first||uni[1].first||uni[2].first)
            {
                if(uni[2].first > 0)
                {
                    putchar(uni[2].second);
                    uni[2].first--;
                }
                if(uni[0].first <= uni[1].first && uni[1].first > 0)
                {
                    putchar(uni[1].second);
                    uni[1].first--;
                }
                else
                {
                    if(uni[0].first>0)
                    {
                        putchar(uni[0].second);
                        uni[0].first--;
                    }
                }
            }
            printf("\n");
        }
    }
    return 0;
}

