#include <iostream>
#include <vector>

using namespace std;

void alphabetCake(vector<vector<char>>& cake) {
    for(int i=0; i < cake.size(); i++) {
        char cur = '?';
        for(int j=0; j < cake[i].size(); j++) {
            if(cake[i][j] != '?') {
                if(cur == '?') {
                    for(int k=0; k < j; k++) {
                        cake[i][k] = cake[i][j];
                    }
                }

                cur = cake[i][j];
            }
            else {
                cake[i][j] = cur;
            }
        }

        if(cur == '?') {
            if(i > 0) {
                for(int j=0; j < cake[i].size(); j++) {
                    cake[i][j] = cake[i-1][j];
                }
            }
        }
        else {
            if(i > 0 && cake[i-1][0] == '?') {
                for(int k=0; k < i; k++) {
                    for(int j=0; j < cake[k].size(); j++) {
                        cake[k][j] = cake[i][j];
                    }
                }
            }
        }
    }
}

int main() {
    int t;
    cin >> t;
    for(int i=1; i <= t; i++) {
        int r, c;
        cin >> r >> c;
        vector<vector<char>> cake(r, vector<char>(c));
        for(int j=0; j < r; j++)
            for(int k=0; k < c; k++)
                cin >> cake[j][k];

        alphabetCake(cake);
        cout << "Case #" << i << ":" << endl;
        for(int j=0; j < r; j++) {
            for (int k = 0; k < c; k++)
                cout << cake[j][k];
            cout << endl;
        }
    }
}