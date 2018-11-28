#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

std::string readline()
{
	std::string l;
	std::getline(cin, l);
	//cout << l << endl;
	return l;
}

int R, C;
char G[25][25];

void exph(int r, int sc)
{
    for(int c = sc+1; c < C && G[r][c] == '?'; c++)
        G[r][c] = G[r][sc];
    for(int c = sc-1; c >= 0 && G[r][c] == '?'; c--)
        G[r][c] = G[r][sc];
}

void expv(int sr, int c)
{
    for(int r = sr+1; r < R && G[r][c] == '?'; r++)
        G[r][c] = G[sr][c];
    for(int r = sr-1; r >= 0 && G[r][c] == '?'; r--)
        G[r][c] = G[sr][c];
}

void docase(int casenum)
{
    cin >> R >> C;
    readline();

    for(int r = 0; r < R; r++)
    {
        string line = readline();

        for(int c = 0; c < C; c++)
            G[r][c] = line[c];
    }

    for(int r = 0; r < R; r++)
        for(int c = 0; c < C; c++)
            if(G[r][c] != '?')
                exph(r, c);

    for(int r = 0; r < R; r++)
        for(int c = 0; c < C; c++)
            if(G[r][c] != '?')
                expv(r, c);

    printf("Case #%d: \n", casenum+1);

    for(int r = 0; r < R; r++)
    {
        for(int c = 0; c < C; c++)
            printf("%c", G[r][c]);
        printf("\n");
    }
}

int main()
{
    int T;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        docase(i);
    }
	return 0;
}
