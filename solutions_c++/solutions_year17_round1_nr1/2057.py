#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <vector>
using namespace std;

int R, C;

void Fill(vector<string> &cake, int row, int index, int sum) {
    for (int k = index+sum; k >= 0 && k < cake[row].size(); k = k + sum) {
        if (cake[row][k] == '?')
            cake[row][k] = cake[row][index];
        else
            break;
    }
}

void Print(vector<string> &cake) {
    for (int i = 0; i < R; i++){
        for (int j = 0; j < cake[i].size(); j++)
            cout << cake[i] << endl;
    }
    cout << "****" << endl;
}

vector<string> SolveProblem(ifstream &fin) {
    fin >> R >> C;
    vector<string> cake(R);
    for (int i = 0; i < R; i++)
        fin >> cake[i];
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < cake[i].size(); j++) {
            if (cake[i][j] != '?') {
                Fill(cake, i, j, 1);
                Fill(cake, i, j, -1);
            }
        }
    }

    bool exit = false;
    int e = 0;
    while (!exit) {
        e++;
        //Print(cake);
        exit = true;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < cake[i].size(); j++) {
                if (cake[i][j] == '?') {
                    exit = false;
                    if (i > 0 && cake[i-1][j] != '?') cake[i][j] = cake[i - 1][j];
                    else if(i<R) cake[i][j] = cake[i + 1][j];
                    else cout << "mmm problema";
                }
            }
        }
    }
    return cake;
}

int main()
{
    int T;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin >> T;
    for (int test = 0; test < T; test++)
    {
        cout << "Case #" << test + 1 << endl;
        vector<string> ret = SolveProblem(fin);
        fout << "Case #" << test + 1 << ": " << endl;
        for (int i = 0; i < R; i++) {
            fout << ret[i] << endl;
        }

    }
    return 0;
}

