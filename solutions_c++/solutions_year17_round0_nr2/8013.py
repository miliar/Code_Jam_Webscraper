#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int main() {
    int T;
    cin >> T;

    for  (int i = 0; i < T; i++){
        string line;
        int flag = -1;
        cin >> line;
        int N = line.length();
        int check[18];
        for (int j = 0; j < 18; j++)
            check[j] = -1;
        for (int j = 0; j < N;j++) {
            if (flag==-1) {
               // cout << "tou  j = " << j <<endl;
                check[j] = line[j] - '0';
                while (j!=0 && (check[j] < check[j - 1])) {
                        //cout <<"j="<<j<<endl;
                        check[j - 1]--;
                        check[j] = 9;
                        j--;
                        flag = 1;
                }
            }
            else
                check[j] = 9;
        }
        int j = 0;
        while (check[j]==0)
            j++;
        cout << "Case #" << i+1 << ": ";
        for (; j<N; j++)
            cout <<check[j];
        cout <<endl;

        /*
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
          */

    }
    //fin.close();
    //fout.close();
    return 0;
}