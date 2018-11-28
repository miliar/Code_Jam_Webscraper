/*
ID: bob.bra1
PROG:
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <deque>

using namespace std;

string solve(string s){
    int L = s.size();
    //find first non-decreasing num
    int non_dec_index;
    int is_non_dec = 1;
    for (non_dec_index=0; non_dec_index < L-1; non_dec_index++){
        if (s[non_dec_index] > s[non_dec_index+1]) {
            is_non_dec = 0;
            break;
        }
    }
    if (! is_non_dec){
        if (s[non_dec_index] == '1'){
            s ="";
            for (int i =0; i < L-1; i++) s.push_back('9');
        }
        else{
            s[non_dec_index] -=1;
            for (int i=non_dec_index+1; i < L; i++){
                s[i] = '9';
            }
        }
    }
    if (is_non_dec) return s;
    return solve(s);

}

int main()
{
    int T;
    string s;
    cin >> T;
    for (int tc=1; tc <=T; tc++){
        cin >> s;
        s = solve(s);
        cout << "Case #" << tc << ": " << s << endl;
    }

    return 0;
}
