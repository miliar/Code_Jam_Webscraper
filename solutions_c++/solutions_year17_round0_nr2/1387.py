#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int main (){
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    vector < int64_t > ones(19);
    vector < int64_t > tens(19);
    ones[0] = 0;
    for (int i = 1; i <= 18; ++i) 
        ones[i] = ones[i-1] * 10 + 1;
    tens[0] = 1;

    for (int i = 1; i <= 18; ++i)
        tens[i] = tens[i-1] * 10;

    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas){
        int64_t n;
        cin >> n; 
        int64_t res = 0;
        int prev = 0;
        for (int i = 17; i >= 0; --i){
            for (int j = 9; j >= prev; --j){
                int64_t to = res +  j * ones[i + 1];
                
                if (to <= n){
                    res = res + j * tens[i];
                    prev = max (prev, j);
                    break;
                }
            }
        }
        cout << "Case #" << cas <<": "<< res << endl;
    } 
    return 0;
}






