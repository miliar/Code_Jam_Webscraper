#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <iostream>
using namespace std;



int main(int p_Argc, char  **p_Argv)
{
    int nCas;
    cin >> nCas;
    cin.ignore();

    for (int cas = 0; cas < nCas; cas++){
        int R, C;
        cin >> R >> C; cin.ignore();
        vector<string> cake;

        for (int j=0; j < R; j++){
            string s;
            cin >> s;
            cin.ignore();
            cake.push_back(s);
        }

        for (int j=0; j < R; j++){
            for (int k=0; k < C; k++){
                if (cake[j][k] != '?'){
                    int up = j-1;
                    int down = j+1;
                    while (up >= 0 && cake[up][k]=='?'){
                        cake[up][k] = cake[j][k];
                        up--;
                    }
                    while (down < R && cake[down][k]=='?'){
                        cake[down][k] = cake[j][k];
                        down++;
                    }
                }
            }
        }
        for (int j=0; j < R; j++){
            for (int k=0; k < C; k++){
                if (cake[j][k] != '?'){
                    int left = k-1;
                    int right = k+1;
                    while (left >= 0 && cake[j][left]=='?'){
                        cake[j][left] = cake[j][k];
                        left--;
                    }
                    while (right < C && cake[j][right]=='?'){
                        cake[j][right] = cake[j][k];
                        right++;
                    }
                }
            }
        }

        cout << "Case #" << cas + 1 <<": "<<endl;
        for (int j = 0; j < R; j++){
            cout << cake[j] <<endl;
        }
    }
    return 0;
}





