#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>
#include <fstream>
#define MAX 987654321
using namespace std;
typedef long long ll;

int main () {
    ifstream input("/Users/ahnzeus/Desktop/input.in");
    ofstream output("/Users/ahnzeus/Desktop/output.txt");
    
    int T;
    input >> T;
    for(int t=1;t<=T;t++){
        string s;
        input >> s;
        for(int i=(int)s.size()-1;i>=1;i--){
            if(s[i]<s[i-1]){
                s[i-1] -= 1;
                for(int j=i;j<s.size();j++){
                    if(s[j]!='9'){
                        s[j]='9';
                    } else {
                        break;
                    }
                }
            }
        }
        
        output << "Case #" << t <<": ";
        
        
        for(int i=0;i<s.size();i++){
            if(i==0 && s[i] == '0'){
                continue;
            } else {
                output << s[i];
            }
        }
        output << endl;
    }
}
