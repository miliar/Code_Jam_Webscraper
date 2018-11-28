#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>

using namespace std;

struct cell_t
{
    cell_t() {}
    cell_t(int x, int y) : x1(x), y1(y), x2(x + 1), y2(y + 1) {}
    int x1, y1, x2, y2;
};
map<char, cell_t> cells;

void caser(int casen)
{
    int r, c;
    scanf("%d %d", &r, &c);
    char grid[r][c + 1];

    for(int y = 0; y < r; y++)
    {
        scanf("%s", &grid[y][0]);
        for(int x = 0; x < c; x++)
            cells[grid[y][x]] = cell_t(x, y);
    }

    bool anotherRound;
    do
    {
        anotherRound = false;
        for(int y = 0; y < r; y++)
            for(int x = 0; x < c; x++)
            {
                if(grid[y][x] == '?')
                {
                    if(y > 0 && grid[y - 1][x] != '?')
                    {
                        char c = grid[y - 1][x];
                        cell_t &cell = cells[c];
                        if(cell.y2 != y || cell.x1 > x || cell.x2 <= x)
                            printf("ASSERT1 %d %d %d %d %d %d\n", cell.x1, cell.x2, cell.y1, cell.y2, x, y);
                        int x2;
                        for(x2 = cell.x1; x2 < cell.x2; x2++)
                        {
                            if(grid[y][x2] != '?')
                                break;
                        }
                        if(x2 == cell.x2)
                        {
                            for(x2 = cell.x1; x2 < cell.x2; x2++)
                                grid[y][x2] = c;
                            cell.y2++;
                            continue;
                        }
                    }
                    if(y != r - 1 && grid[y + 1][x] != '?')
                    {
                        char c = grid[y + 1][x];
                        cell_t &cell = cells[c];
                        if(cell.y1 != y + 1 || cell.x1 > x || cell.x2 <= x)
                            printf("ASSERT2\n");
                        int x2;
                        for(x2 = cell.x1; x2 < cell.x2; x2++)
                        {
                            if(grid[y][x2] != '?')
                                break;
                        }
                        if(x2 == cell.x2)
                        {
                            for(x2 = cell.x1; x2 < cell.x2; x2++)
                                grid[y][x2] = c;
                            cell.y1--;
                            continue;
                        }
                    }
                    if(x > 0 && grid[y][x - 1] != '?')
                    {
                        char c = grid[y][x - 1];
                        cell_t &cell = cells[c];
                        if(cell.x2 != x || cell.y1 > y || cell.y2 <= y)
                            printf("ASSERT3\n");
                        int y2;
                        for(y2 = cell.y1; y2 < cell.y2; y2++)
                        {
                            if(grid[y2][x] != '?')
                                break;
                        }
                        if(y2 == cell.y2)
                        {
                            for(y2 = cell.y1; y2 < cell.y2; y2++)
                                grid[y2][x] = c;
                            cell.x2++;
                            continue;
                        }
                    }
                    if(x != c - 1 && grid[y][x + 1] != '?')
                    {
                        char c = grid[y][x + 1];
                        cell_t &cell = cells[c];
                        if(cell.x1 != x + 1 || cell.y1 > y || cell.y2 <= y)
                            printf("ASSERT4 %d %d %d %d %d %d\n", cell.x1, cell.x2, cell.y1, cell.y2, x, y);
                        int y2;
                        for(y2 = cell.y1; y2 < cell.y2; y2++)
                        {
                            if(grid[y2][x] != '?')
                                break;
                        }
                        if(y2 == cell.y2)
                        {
                            for(y2 = cell.y1; y2 < cell.y2; y2++)
                                grid[y2][x] = c;
                            cell.x1--;
                            continue;
                        }
                    }
                    anotherRound = true;
                }
            }
    }
    while(anotherRound);

    printf("Case #%d:\n", casen);
    for(int y = 0; y < r; y++)
        printf("%s\n", &grid[y][0]);
}

int main()
{
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++)
        caser(i);
    return 0;
}