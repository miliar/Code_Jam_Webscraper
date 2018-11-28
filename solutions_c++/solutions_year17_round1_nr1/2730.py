#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

int r, c;
string grid[30];
bool used[300];

int square[30][30];

void compute_square()
{
    for(int i = 0; i < r; ++i)
    for(int j = 0; j < c; ++j)
    {
        if(grid[i][j] == '?')
        {
            square[i][j] = 0;
        }else
        {
            square[i][j] = 1;
        }
        if(i > 0)
        {
            square[i][j] += square[i-1][j];
        }
        if(j > 0)
        {
            square[i][j] += square[i][j-1];
        }
        if(i > 0 && j > 0)
        {
            square[i][j] -= square[i-1][j-1];
        }
    }
}

int compute_count(int i1, int j1, int i2, int j2)
{
    int i_min, i_max, j_min, j_max;
    i_min = min(i1, i2);
    i_max = max(i1, i2);
    j_min = min(j1, j2);
    j_max = max(j1, j2);
    int ans = 0;
    ans += square[i_max][j_max];
    if(i_min > 0)
    {
        ans -= square[i_min-1][j_max];
    }
    if(j_min > 0)
    {
        ans -= square[i_max][j_min-1];
    }
    if(i_min > 0 && j_min > 0)
    {
        ans += square[i_min-1][j_min-1];
    }
    return ans;
}

int main()
{
    string file_name = "A-small-attempt1";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        f1 >> r >> c;
        for(int i = 0; i < r; ++i)
        {
            f1 >> grid[i];
        }
        memset(used, 0, sizeof(used));
        for(int i1 = 0; i1 < r; ++i1)
        for(int j1 = 0; j1 < c; ++j1)
        {
            if(grid[i1][j1] == '?' || used[grid[i1][j1]])
            {
                continue;
            }
            //cout << grid[i1][j1] << endl;
            used[grid[i1][j1]] = true;
            memset(square, 0, sizeof(square));
            compute_square();

            int best_i2 = i1, best_j2 = j1;
            int max_size=-1, best_i1, best_j1;
            for(int i2 = 0; i2 < r; ++i2)
            for(int j2 = 0; j2 < c; ++j2)
            {
                if(compute_count(best_i2, best_j2, i2, j2) == 1)
                {
                    if((max(best_i2,i2)-min(best_i2,i2)+1) * (max(best_j2,j2)-min(best_j2,j2)+1) > max_size)
                    {
                        max_size = (max(best_i2,i2)-min(best_i2,i2)+1) * (max(best_j2,j2)-min(best_j2,j2)+1);
                        best_i1 = i2;
                        best_j1 = j2;
                        //cout << "hi" << best_i1 << j2<<' ' << max_size << endl;
                    }
                }
            }
            //cout << ' ' << best_i1 << ' ' << best_j1 << endl;

            best_i2 = best_i1;
            best_j2 = best_j1;
            max_size = -1;
            for(int i2 = 0; i2 < r; ++i2)
            for(int j2 = 0; j2 < c; ++j2)
            {
                if(compute_count(best_i2, best_j2, i2, j2) == 1)
                if(min(best_i2,i2) <= i1 && i1 <= max(best_i2,i2))
                if(min(best_j2,j2) <= j1 && j1 <= max(best_j2,j2))
                {
                    if((max(best_i2,i2)-min(best_i2,i2)+1) * (max(best_j2,j2)-min(best_j2,j2)+1) > max_size)
                    {
                        max_size = (max(best_i2,i2)-min(best_i2,i2)+1) * (max(best_j2,j2)-min(best_j2,j2)+1);
                        best_i1 = i2;
                        best_j1 = j2;
                    }
                }
            }

            for(int i = min(best_i2,best_i1); i <= max(best_i2,best_i1); ++i)
            for(int j = min(best_j2,best_j1); j <= max(best_j2,best_j1); ++j)
            {
                grid[i][j] = grid[i1][j1];
            }
        }
        f2 << endl;
        for(int i = 0; i < r; ++i)
        {
            f2 << grid[i] << endl;
        }
    }
    return 0;
}

