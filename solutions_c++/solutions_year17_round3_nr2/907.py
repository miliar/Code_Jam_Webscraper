#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream in("C.in");
ofstream out("C.out");

int main(){
    int t;
    in >> t;
    for (int q = 0; q < t; q++){
        int c, j;
        in >> c >> j;
        vector <pair <int, int> > a(c + j);
        for (int i = 0; i < c + j; i++){
            in >> a[i].first >> a[i].second;
        }
        sort(a.begin(), a.end());
        int res;
        if (c <= 1 && j <= 1){
            res = 2;
        }
        else {
            if (min(1440 - a[1].first + a[0].second, a[1].second - a[0].first) <= 720){
                res = 2;
            }
            else {
                res = 4;
            }
        }
        out << "Case #" << q + 1 << ": " << res << endl;
    }
}
