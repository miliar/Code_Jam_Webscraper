#include <iostream>
#include <vector>
using namespace std;
int main() {
    int t, r, c, begin, end;
    string cake[123];
    cin >> t;
    for(int i = 0; i < t; ++ i) {
        cin >> r >> c;

        vector<int> ridx;
        for(int j = 0; j < r; ++ j) {
            cin >> cake[j];
            // solve cols
            vector<int> idx;
            for(int k = 0; k < c; ++ k)
                if(cake[j][k] != '?')
                    idx.push_back(k);

            if(idx.size() != 0) {
                ridx.push_back(j);
                for(int k = 0; k < idx[0]; ++ k)
                    cake[j][k] = cake[j][idx[0]];
                for(int k = 0; k < idx.size(); ++ k) {
                    begin = idx[k];
                    end = c;
                    if(k + 1 < idx.size())
                        end = idx[k+1];
                    for(int m = begin; m < end; ++ m)
                        cake[j][m] = cake[j][idx[k]];
                }
            }
        } 
        // solve rows
        if(ridx.size() > 0) {
            for(int j = 0; j < ridx[0]; ++ j)
                cake[j] = cake[ridx[0]];
            for(int j = 0; j < ridx.size(); ++ j) {
                begin = ridx[j];
                end = r;
                if(j + 1 < ridx.size())
                    end = ridx[j+1];
                for(int k = begin; k < end; ++ k) {
                    cake[k] = cake[ridx[j]];
                }
            }
        }
        cout << "Case #" << (i + 1) << ":" << endl;
        for(int j = 0; j < r; ++ j)
            cout << cake[j] << endl;
    }
    return 0;
}
