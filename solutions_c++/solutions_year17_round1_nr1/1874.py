#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        string in = "?";
        vector<string> cake;
        vector<string> newcake;
        string row;
        int r, c;
        cin >> r >> c;
        for (int I = 0; I < r; I++){
            cin >> row;
            cake.push_back(row);
        }
        int p = 1;
        int q = 0;
        for (int itr = 0; itr < r; itr++){
            row = "";
            for (int it = 0; it < c; it++){
                q++;
                if (cake[itr][it] != in[0]){
                    for (int Q = 0; Q < q; Q++){
                        row += cake[itr][it];
                    }
                    q = 0;
                }
            }
            if (q == c){
                if (newcake.empty()){
                    p++;
                }
                else{
                    newcake.push_back(newcake[itr-1]);
                }
            }
            else{
                for (int Q = 0; Q < q; Q++){
                    row += row[row.size()-1];
                }
                for (int P = 0; P < p; P++){
                    newcake.push_back(row);
                }
                p = 1;
            }
            q = 0;
        }
        cout << "Case #" << i+1 << ":" << endl;
        for (int itr = 0; itr < r; itr++){
            cout << newcake[itr] << endl;
        }
    }
    return 0;
}
