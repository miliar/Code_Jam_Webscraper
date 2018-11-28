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
int n;
int main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> n;
    for (int i=0;i<n;i++){
        out << "Case #" << i + 1 << ": ";
        s = "";
        in >> s;
        bool go = false;
        for (int j=0;j<s.size();j++){
            if (s[j] != '1' && s[j] != '0') break;
            if (s[j] == '0'){go = true; break;}
        }
        if (go){
            for (int j=0;j<s.size() - 1;j++){
                out << "9";
            }
            out << endl;
        }
        else{
            for (int j=1;j<s.size();j++){
                if (s[j] < s[j - 1]){
                    for (int k=j;k>=1;k--){
                        if (s[k] < s[k-1]) {s[k-1] --; s[k] = '9';}
                    }
                    for (int k=j;k<s.size();k++){
                        s[k] = '9';
                    }
                    break;
                }
            }
            out << s << endl;
        }
    }
    out.close();
    return 0;
}
