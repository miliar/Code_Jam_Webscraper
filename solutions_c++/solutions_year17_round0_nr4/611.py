#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

struct Cell
{
    int value;
    int R;
    int C;
};

/*
0 -> /
1 -> o
2 -> +
3 -> x
*/

int NR, N, M;
int grid[100][100];
bool rows[100], cols[100], diagUp[199], diagDown[199];
vector<Cell> cells;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> NR;

    for(int q = 0; q < NR; q++)
    {
        cin >> N >> M;

        cells.clear();

        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                grid[i][j] = 0;

        for(int i = 0; i < N; i++)
        {
            rows[i] = false;
            cols[i] = false;
        }

        for(int i = 99 - N + 1; i <= 99 + N - 1; i++)
        {
            diagUp[i] = false;
            diagDown[i] = false;
        }

        char value;
        int R, C;
        for(int i = 0; i < M; i++)
        {
            cin >> value >> R >> C;
            R--; C--;

            switch(value)
            {
            case 'o':
                grid[R][C] = 1;
                rows[R] = true;
                cols[C] = true;
                diagUp[99 + N - 1 - R - C] = true;
                diagDown[99 + R - C] = true;
                break;
            case '+':
                grid[R][C] = 2;
                diagUp[99 + N - 1 - R - C] = true;
                diagDown[99 + R - C] = true;
                break;
            case 'x':
                grid[R][C] = 3;
                rows[R] = true;
                cols[C] = true;
                break;
            }
        }

        int i = -1;
        while(i != N - 1)
        {
            /*
            if(i <= N / 2)
                i = N - 1 - i;
            else
                i = N - i;
            */
            if(i == -1)
                i = N - 1;

            for(int j = 0; j < N; j++) // Each column
            {
                switch(grid[i][j])
                {
                case 1:
                    continue;
                    break;
                case 2:
                    diagUp[99 + N - 1 - i - j] = false;
                    diagDown[99 + i - j] = false;
                    break;
                case 3:
                    rows[i] = false;
                    cols[j] = false;
                    break;
                }

                bool ok_2 = !diagUp[99 + N - 1 - i - j] && !diagDown[99 + i - j];
                bool ok_3 = !rows[i] && !cols[j];
                bool only_1 = grid[i][j] == 2 || grid[i][j] == 3;

                if(ok_2 && ok_3)
                {
                    grid[i][j] = 1;
                    cells.push_back({grid[i][j], i, j});
                }
                else if(ok_2 && !only_1)
                {
                    grid[i][j] = 2;
                    cells.push_back({grid[i][j], i, j});
                }
                else if(ok_3 && !only_1)
                {
                    grid[i][j] = 3;
                    cells.push_back({grid[i][j], i, j});
                }

                switch(grid[i][j])
                {
                case 1:
                    rows[i] = true;
                    cols[j] = true;
                    diagUp[99 + N - 1 - i - j] = true;
                    diagDown[99 + i - j] = true;
                    break;
                case 2:
                    diagUp[99 + N - 1 - i - j] = true;
                    diagDown[99 + i - j] = true;
                    break;
                case 3:
                    rows[i] = true;
                    cols[j] = true;
                    break;
                }
            }

            if(i == N - 1)
                i = 0;
            else
                i++;
        }



        /*
        cout << "DiagUp : ";
        for(int i = 99 - N + 1; i <= 99 + N - 1; i++)
            cout << diagUp[i] << " ";
        cout << endl;

        cout << "DiagDown : ";
        for(int i = 99 - N + 1; i <= 99 + N - 1; i++)
            cout << diagDown[i] << " ";
        cout << endl;*/

        int score = 0;
        for(int i = 0; i < N; i++) // Each row
        {
            for(int j = 0; j < N; j++) // Each column
            {
                int value = grid[i][j];
                switch(value)
                {
                case 1:
                    score += 2;
                    break;
                case 2:
                    score += 1;
                    break;
                case 3:
                    score += 1;
                    break;
                }
            }
        }

        cout << "Case #" << (q + 1) << ": " << score << " " << cells.size() << endl;

        for(Cell c : cells)
        {
            switch(c.value)
            {
            case 1:
                cout << 'o';
                break;
            case 2:
                cout << '+';
                break;
            case 3:
                cout << 'x';
                break;
            }
            cout << " " << (c.R + 1) << " " << (c.C + 1) << endl;
        }
        /*
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < N; j++)
            {
                char value;
                switch(grid[i][j])
                {
                case 0:
                    value = ' ';
                    break;
                case 1:
                    value = 'o';
                    break;
                case 2:
                    value = '+';
                    break;
                case 3:
                    value = 'x';
                    break;
                }
                cout << value;
            }
            cout << endl;
        }
        */
    }
}
