/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: bernardo
 *
 * Created on April 7, 2017, 11:33 PM
 */

#include <cstdlib>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>

using namespace std;
const int MULT = 1;
const int PLUS = -1;
const int OU = 2;
const int EMPTY = 0;

/*
 * 
 */

int getStylePoints(const vector<vector<int > > & matrix, int N) {
    int score = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (matrix[i][j] == PLUS || matrix[i][j] == MULT) {
                score++;
            } else if (matrix[i][j] == OU) {
                score += 2;
            }
        }
    }
    return score;

}

int main(int argc, char** argv) {
    int T;
    cin>>T;
    for (int t = 0; t < T; t++) {
        int N, M;
        cin>>N;
        cin>>M;

        vector<vector<int> > matrix;
        for (int i = 0; i < N; i++) {
            matrix.push_back(vector<int>(N, EMPTY));
        }

        for (int i = 0; i < M; i++) {
            char model;
            cin>>model;
            int type = OU;
            switch (model) {
                case '+':
                    type = PLUS;
                    break;
                case 'x':
                    type = MULT;
                    break;
            }
            int r, c;
            cin>>r;
            cin>>c;
            r--;
            c--;
            matrix[r][c] = type;

        }

        vector<vector< int > > bestSolution;
        int fixedOuOrX = 0;
        for(int i=0;i<N;i++) {
            if(matrix[0][i]==OU || matrix[0][i]==MULT) {
                fixedOuOrX = i;
            }
        }
        for (int i = 0; i < N; i++) {
            bestSolution.push_back(vector<int>(N, EMPTY));
        }
        bestSolution[0][fixedOuOrX] = OU;
        for (int i = 0; i < N; i++) {
            if(i!=fixedOuOrX) {
                bestSolution[0][i] = PLUS;
            }
        }
        for (int i = 1; i < N - 1; i++) {
            bestSolution[N - 1][i] = PLUS;
        }
        for (int i = fixedOuOrX+1, j=1; i < N; i++, j++) {
            bestSolution[j][i] = MULT;
        }
        for (int i = 0;i<fixedOuOrX;i++) {
            bestSolution[N-1-i][i] = MULT;
        }

        int bestStylePoints = getStylePoints(bestSolution, N);


        int counter = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (bestSolution[i][j] != matrix[i][j]) {
                    counter++;
                }
            }
        }

        cout << "Case #" << t + 1 << ": " << bestStylePoints << " " << counter << endl;
        /*
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (bestSolution[i][j] == OU) {
                    cout << 'o';
                } else if (bestSolution[i][j] == PLUS) {
                    cout << '+';
                } else if (bestSolution[i][j] == MULT) {
                    cout << 'x';
                } else {
                    cout << " ";
                }
            }
            cout << endl;

        }
        cout<<endl;
        */
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (bestSolution[i][j] != matrix[i][j]) {
                    if (bestSolution[i][j] == OU) {
                        cout << 'o';
                    } else if (bestSolution[i][j] == PLUS) {
                        cout << '+';
                    } else {
                        cout << 'x';
                    }
                    cout << " " << i+1 << " " << j+1 << endl;
                }
            }
        }

    }
    return 0;
}