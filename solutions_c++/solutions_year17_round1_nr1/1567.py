//
// Created by 강경완 on 2017. 4. 15..
//
#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        char table[30][30] = {0,};
        char DP[100];
        int R, C;
        cin >> R >> C;

        for (int r = 1; r <= R; r++) {
            for (int c = 1; c <= C; c++)
                cin >> table[r][c];
        }


        for (int r = 1; r <= R; r++) {
            for (int c = 1; c <= C; c++) {
                if (table[r][c] == '?') {
                    if (table[r][c - 1] == 0);
                    else
                        table[r][c] = table[r][c - 1];
                }
            }
        }

        for (int r = R; r >= 1; r--) {
            for (int c = C; c >=1; c--) {
                if (table[r][c] == '?') {
                    if (table[r][c + 1] == 0);
                    else
                        table[r][c] = table[r][c + 1];
                }
            }
        }

        for(int r=1; r <=R; r++){
            if(table[r][1]=='?' && table[r-1][1] != 0){
                for(int c=1; c<=C; c++){
                    table[r][c] = table[r-1][c];
                }
            }
        }

        for(int r=R; r >=1; r--){
            if(table[r][1]=='?' && table[r+1][1] != 0){
                for(int c=1; c<=C; c++){
                    table[r][c] = table[r+1][c];
                }
            }
        }

        cout << "Case #" << i+1 << ":" <<endl;
        for (int r = 1; r <= R; r++) {
            for (int c = 1; c <= C; c++)
                cout << table[r][c];
            cout << endl;
        }

    }
}