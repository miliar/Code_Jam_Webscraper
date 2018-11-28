#include <bits/stdc++.h>

using namespace std;

const int maxN = 720 + 10;
int d[maxN][maxN][2][2];

int must[maxN * 2];

void relax(int& what, int with)
{
    if (what == -1 || what > with)
        what = with;
}

void solve()
{
    int na, nb;
    cin >> na >> nb;
    
    memset(must, -1, sizeof(must));
    for (int guy = 0; guy < 2; guy++)
    {
        for (int i = 0; i < (guy == 0 ? na : nb); i++)
        {
            int x, y;
            cin >> x >> y;
            
            for (int t = x; t < y; t++)
                must[t] = guy;
        }
    }
    
    memset(d, -1, sizeof(d));
    
    d[0][0][0][0] = d[0][0][1][1] = 0;
    for (int i = 0; i <= 720; i++)
        for (int j = 0; j <= 720; j++)
            for (int first = 0; first < 2; first++)
                for (int last = 0; last < 2; last++)
    {
        if (d[i][j][first][last] == -1) continue;
        
        //printf("d %d %d %d %d -> %d\n", i, j, first, last, d[i][j][first][last]);
        
        for (int now = 0; now < 2; now++)
        {
            if (must[i + j] != now && must[i + j] != -1) continue;
            relax(d[i + (now == 0)][j + (now == 1)][first][now], d[i][j][first][last] + (now != last ? 1 : 0));
        }
    }
    
    int answer = -1;
    for (int first = 0; first < 2; first++)
        for (int last = 0; last < 2; last++)
            if (d[720][720][first][last] != -1)
                relax(answer, d[720][720][first][last] + (first != last ? 1 : 0));
            
    assert(answer != -1);
    cout << answer << endl;
}

int main()
{
    int nt;
    cin >> nt;
    
    for (int i = 0; i < nt; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    
    return 0;
}
