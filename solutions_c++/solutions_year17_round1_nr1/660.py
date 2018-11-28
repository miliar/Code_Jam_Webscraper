#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main(){

    int cases;
    scanf ("%d", &cases);

    for (int nth_case = 1; nth_case <= cases; nth_case++){

        int n, m;
        scanf ("%d %d", &n, &m);
        char grid[n][m];
        for (int i = 0; i < n; i++){
            scanf ("%s", grid[i]);
        }

        for (int i = 0; i < n; i++){
            char last = 0;
            for (int j = 0; j < m; j++){
                if (grid[i][j] != '?'){
                    int aux = j;
                    while (aux > 0 && grid[i][aux-1] == '?') grid[i][--aux] = grid[i][j];
                    last = grid[i][j];
                }
            }
            if (last == 0) continue;
            int aux = m - 1;
            while (aux >= 0 && grid[i][aux] == '?') grid[i][aux--] = last;
        }

        for (int i = 1; i < n; i++){
            if (grid[i][0] == '?')
                for (int j = 0; j < m; j++)
                    grid[i][j] = grid[i-1][j];
        }


        for (int i = n-2; i >= 0; i--){
            if (grid[i][0] == '?')
                for (int j = 0; j < m; j++)
                    grid[i][j] = grid[i+1][j];
        }
        printf ("Case #%d:\n", nth_case);
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++)
                printf ("%c", grid[i][j]);
            printf ("\n");
        }

    }

    return 0;
}


