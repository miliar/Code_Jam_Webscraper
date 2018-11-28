#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int main() {
    int T;
    cin >> T;

    for  (int i = 0; i < T; i++){
        int flip = 0;
        int check[1000];
        for (int j = 0; j < 1000; j++)
            check[j] = 0;
        string line;
        cin >>line;
        for (int q = 0; q < line.length(); q++)
            if (line[q]=='+')
                check[q] = 1;
        int N =line.length();
        int Tsize;
        cin >> Tsize;
        for (int j = 0; j < N-Tsize+1 ; j++ ){
            if (check[j] == 0){
                flip++;
                for (int p = 1; p < Tsize; p++){
                    check[j+p] = 1-check[j+p];
                }
            }
        }
        for (int j = N-Tsize+1; j < N; j++)
            if (check[j]==0) {
                flip = -1;
                break;
            }
        if (flip!=-1)
            cout << "Case #" << i+1 << ": " << flip <<endl;
        else
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" <<endl;
    }
    //fin.close();
    //fout.close();
    return 0;
}