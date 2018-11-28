#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

ifstream in("B.in");
ofstream out("B.out");

int max(vector <int> a, int prev){
    int res = 0;
    for (int i = 0; i < (int) a.size(); i++){
        if (i != prev){
            res = max(res, a[i]);
        }
    }
    return res;
}

int main(){
    int t;
    in >> t;
    vector <int> col(6);
    for (int q = 0; q < t; q++){
        int n;
        in >> n;
        for (int i = 0; i < 6; i++){
            in >> col[i];
        }
        string res = "";
        if (max(col, -1) * 2 > n){
            res = "IMPOSSIBLE";
        }
        else {
            int prev = -1, prior = -1;
            for (int i = 0; i < n; i++){
                if (prev != 0 && col[0] == max(col, prev) && (prior == 0 || col[prior] < col[0] || prev == prior)){
                    col[0]--;
                    res += "R";
                    prev = 0;
                }
                else if (prev != 2 && col[2] == max(col, prev) && (prior == 2 || col[prior] < col[2] || prev == prior)){
                    col[2]--;
                    res += "Y";
                    prev = 2;
                }
                else if (prev != 4 && col[4] == max(col, prev) && (prior == 4 || col[prior] < col[4] || prev == prior)){
                    col[4]--;
                    res += "B";
                    prev = 4;
                }
                if (i == 0){
                    prior = prev;
                }
            }
        }
        out << "Case #" << q + 1 << ": " << res << endl;
    }
}
