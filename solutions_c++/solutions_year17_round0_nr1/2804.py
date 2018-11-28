#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <stdlib.h>
#include <cmath>
#include <math.h>
#include <fstream>
#include <bitset>
using namespace std;
string s;
int t, n;
int main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> n;
    for (int i=0;i<n;i++){
        in >> s >> t;
        int ans = 0;
        for (int j=0;j<s.size() - t + 1;j++){
            if (s[j] == '+') continue;
            for (int k=j;k<j+t;k++){
                if (s[k] == '+') s[k] = '-';
                else s[k] = '+';
            }
            ans ++;
        }
        for (int j=0;j<s.size();j++){
            if (s[j] == '-'){
                ans = -1;
                break;
            }
        }
        out << "Case #" << i+1 << ": ";
        if (ans == -1){
            out << "IMPOSSIBLE";
        }
        else out << ans;
        out << endl;
    }
    out.close();
    return 0;
}
