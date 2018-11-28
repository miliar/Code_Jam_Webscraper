#include <iostream>
#include <stdio.h>

using namespace std;

int r,c;
char grid[27][27];

int main()
{
    //freopen("input.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int cases;
    char prev = ' ';
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        cin >> r >> c;


        for (int j = 0; j < r; j++) {
            prev = ' ';
            for (int k = 0; k < c; k++) {
                cin >> grid[j][k];

                if (grid[j][k] != '?') {
                    prev = grid[j][k];

                    for (int l = k-1; l >= 0; l--) {
                        if (grid[j][l] == '?')
                            grid[j][l] = prev;
                        else
                            break;
                    }
                }
                else if (prev != ' ')
                    grid[j][k] = prev;
            }
        }


        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {

                if (grid[j][k] == '?') {
                    for (int jj = j-1; jj >= 0; jj--) {
                        if (grid[jj][k] != '?') {
                            grid[j][k] = grid[jj][k];
                            break;
                        }
                    }
                }
                if (grid[j][k] == '?') {
                    for (int jj = j+1; jj < r; jj++) {
                        if (grid[jj][k] != '?') {
                            grid[j][k] = grid[jj][k];
                            break;
                        }
                    }
                }
            }
        }
        cout << "Case #" << (i+1) << ":" << endl;
        for (int row = 0; row < r; row++) {
            for (int col = 0; col < c; col++)
                printf("%c",grid[row][col]);
            printf("\n");
        }

    }

}
