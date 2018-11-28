#include<bits/stdc++.h>

using namespace std;

char maze[30][30];
bool visited[30][30];

int main()
{
    freopen("out.txt","w+",stdout);
    int T;
    int R,C;
    scanf("%d",&T);
    for(int caseNum = 1;caseNum <= T;caseNum++)
    {
        scanf("%d%d",&R,&C);
        for(int i = 0;i < R;i++)
            for(int j = 0;j < C;j++)
                scanf(" %c",&maze[i][j]),visited[i][j] = false;

        int blankRow = 0;
        for(int i = 0;i < R;i++)
        {
            bool first = true;
            bool meet = false;
            for(int j = 0;j < C;j++)
            {
                if(maze[i][j] != '?' && !visited[i][j])
                {
                    meet = true;
                    char now = maze[i][j];
                    int b = j;
                    while(b - 1 >= 0 && maze[i][b - 1] == '?')
                        maze[i][--b] = now;

                    int e = j + 1;
                    while(e < C && maze[i][e] == '?')
                        maze[i][e] = now,e++;

                    if(blankRow)
                    {
                        for(int r = i - 1;r >= i - blankRow;r--)
                            for(int c = b;c < e;c++)
                                maze[r][c] = now;
                    }

                    for(int delta = 1;i + delta < R;delta++)
                    {
                        bool can = true;
                        for(int c = b;c < e;c++)
                        {
                            if(maze[i + delta][c] != '?')
                            {
                                can = false;
                                break;
                            }
                        }

                        if(!can)
                            break;
                        for(int c = b;c < e;c++)
                            maze[i + delta][c] = now,visited[i + delta][c] = true;
                    }

                    j = e - 1;
                }
                else if(maze[i][j] != '?' && visited[i][j])
                    meet = true,first = false;
            }
            if(!meet)
                blankRow++;
            else
                blankRow = 0;
        }

        printf("Case #%d:\n",caseNum);
        for(int i = 0;i < R;i++)
        {
            for(int j = 0;j < C;j++)
                putchar(maze[i][j]);
            putchar('\n');
        }
    }
    return 0;
}
