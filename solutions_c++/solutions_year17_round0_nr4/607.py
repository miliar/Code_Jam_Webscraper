#include <bits/stdc++.h>

using namespace std;



int main()
{
    int t; cin >> t;
    for(int tc = 1; tc <= t; tc++)
    {
        int n; cin >> n;
        int m; cin >> m;


        vector<vector<char> > world(n);
        for(int i = 0; i < n; i++) world[i].assign(n, '.');
        for(int i = 0; i < m; i++)
        {
            char model; cin >> model;
            int r, c; cin >> r >> c;
            r--; c--;
            world[r][c] = model;
        }
        if(n == 1)
        {
            if(world[0][0] == 'o')
            {
                printf("Case #%d: 2 0\n", tc);
            }
            else
            {
                printf("Case #%d: 2 1\n", tc);
                printf("o 1 1\n");
            }
            continue;
        }


        bool hasPlace = false;
        bool haso = false;
        bool hasx = false;
        vector<pair<char,pair<int, int> > > moves;
        for(int i = 0; i < n; i++)
        {
            if(world[0][i] == 'x')
            {
                hasPlace = true;
                hasx = true;
            }
            if(world[0][i] == 'o')
            {
                hasPlace = 1;
                haso = 1;
            }
        }
        int col = -1;

        if(!hasPlace)
        {
            world[0][0] = 'o';
            col = 0;
            moves.push_back(make_pair('o',make_pair(1, 1)));
        }


        for(int i = 0; i < n; i++)
        {
            if(world[0][i] == '.') world[0][i] = '+', moves.push_back(make_pair('+',make_pair(1, i+1)));
            else if(world[0][i] == 'x')
            {
                if(!haso)
                {
                   haso = 1;
                   world[0][i] = 'o', moves.push_back(make_pair('o',make_pair(1, i+1))), col = i;
                }
            }
            else if(world[0][i] == 'o')
            {
                col= i;
            }
        }



        int curCol = (world[0][0] == 'o' ? 0 : n-1);
        for(int i = 1; i < n; i++)
        {
            if(curCol ==  col) curCol +=  (world[0][0] == 'o' ? 1 : -1);
            world[i][curCol]= 'x';
            moves.push_back(make_pair('x',make_pair(i+1, curCol+1)));
            curCol +=  (world[0][0] == 'o' ? 1 : -1);
        }
        for(int i =  (world[0][0] == 'o' ? 1 : 0 ); i < n -  (world[0][0] == 'o' ? 0 : 1); i++)
        {
            if(world[n-1][i] != 'x')
            {
                world[n-1][i]= '+';
                moves.push_back(make_pair('+',make_pair(n, i+1)));
            }
        }

        int sum = 0;
/*
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
               cout << world[i][j];
            }
         cout << endl;
        }
        */

        for(int i = 0; i < n; i++)
        {
            for(int j  = 0; j < n; j++)
            {
                if(world[i][j] == 'o') sum+=2;
                else if(world[i][j] != '.') sum +=1;
            }
        }
        printf("Case #%d: %d %d\n",tc,sum,(int)moves.size());

        for(int i = 0; i < moves.size(); i++)
        {
            printf("%c %d %d\n", moves[i].first, moves[i].second.first, moves[i].second.second);
        }

    }
    return 0;
}
