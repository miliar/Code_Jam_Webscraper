#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

#define MAXN 100
//#define PRINTMAP

int N, M;
bool init_rook[MAXN][MAXN], init_bishop[MAXN][MAXN];
bool rook[MAXN][MAXN], bishop[MAXN][MAXN];

void clear_maps()
{
    for(int x = 0; x < N; x++)
        for(int y = 0; y < N; y++)
            init_rook[x][y] = init_bishop[x][y] = rook[x][y] = bishop[x][y] = 0;
}

void solve_rook()
{
#define map rook
    bool free_row , free_col;
    for(int r = -1, c = -1; r < N and c < N;)
    {
        free_row = false;
        free_col = false;
        while(not free_row and r < N)
        {
            r++;
            free_row = true;
            for(int y = 0; y < N; y++)
                if(map[r][y])
                {
                    free_row = false;
                    break;
                }
        }
        while(not free_col and c < N)
        {
            c++;
            free_col = true;
            for(int x = 0; x < N; x++)
                if(map[x][c])
                {
                    free_col = false;
                    break;
                }
        }

        if(r < N)  // and c < N
            map[r][c] = 1;
    }
#undef map  // rook
}

void solve_bishop()
{
#define map bishop
    map[0][0] = 1;
    for(int x = 1; x < N - 1; x++)
        map[0][x] = map[N - 1][x] = 1;
    map[0][N - 1] = 1;
#undef map  // bishop
}

void solve()
{
    std::cin >> N >> M;
    clear_maps();
    
    while(M--)
    {
        char m;
        int x, y;
        std::cin >> m >> x >> y;
        x--; y--;
        init_rook[x][y]   = rook[x][y]   = (m != '+');
        init_bishop[x][y] = bishop[x][y] = (m != 'x');
    }

    solve_rook();
    solve_bishop();

    //output
    int ans_y = 0, ans_z = 0;
    for(int x = 0; x < N; x++)
        for(int y = 0; y < N; y++)
        {
            ans_y += rook[x][y] + bishop[x][y];
            ans_z += ((rook[x][y] ^ init_rook[x][y]) or
                      (bishop[x][y] ^ init_bishop[x][y]));
        }
    std::cout << ans_y << ' ' << ans_z;
    for(int x = 0; x < N; x++)
    {
#ifdef PRINTMAP
        putchar('\n');
#endif
        for(int y = 0; y < N; y++)
#ifndef PRINTMAP
            if((rook[x][y] ^ init_rook[x][y]) or
               (bishop[x][y] ^ init_bishop[x][y]))
#endif
            {
                char m = '.';
                if(rook[x][y] and bishop[x][y]) m = 'o';
                else if(rook[x][y]) m = 'x';
                else if(bishop[x][y]) m = '+';

#ifdef PRINTMAP
                putchar(m);
#endif

#ifndef PRINTMAP
                if(m != '.') printf("\n%c %d %d", m, x + 1, y + 1);
#endif
            }
    }


}

int main()
{
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }

    return 0;
}
