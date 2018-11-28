/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: bernardo
 *
 * Created on April 15, 2017, 2:38 AM
 */

#include <cstdlib>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    cin>>T;
    for (int t = 0; t < T; t++) {
        int R;
        cin>>R;
        int C;
        cin>>C;
        vector<vector<char> > matrix(R);
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                char next;
                cin>>next;
                matrix[i].push_back(next);
            }
        }
        /*
        cout << "first print" << endl;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cout << matrix[i][j];
            }
            cout << endl;
        }
         * */
        int lastDoneRow = -1;
        for (int i = 0; i < R; i++) {
            int start = 0;
            int lastDoneRowCopy = lastDoneRow;
            for (int j = 0; j < C; j++) {
                if (matrix[i][j] != '?') {
                    lastDoneRow = i;
                    char toFill = matrix[i][j];
                    //fill with matrix[i] to right and up
                    int col = start;
                    for (; col < C; col++) {
                        if (matrix[i][col] == '?' || matrix[i][col] == toFill) {
                            for (int row = i; row > lastDoneRowCopy; row--) {
                                matrix[row][col] = matrix[i][j];
                            }
                        } else {
                            break;

                        }
                    }
                    j = col - 1;
                    start = col;
                }
            }
            /*
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    cout << matrix[i][j];
                }
                cout << endl;
            }*/
        }
        for (int i = lastDoneRow + 1; i < R; i++) {
            for (int j = 0; j < C; j++) {
                matrix[i][j] = matrix[lastDoneRow][j];
            }
        }

        //fix first and last rows in case we have multiple letters
        
        cout << "Case #" << t + 1 << ":" << endl;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cout << matrix[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}

