#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <fstream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <bitset>
#define ull unsigned long long
#define ll long long
#define inf 10000000000000
#define bil 1000000000

using namespace std;

ifstream input;
ofstream output;



int main(int argc, char *argv[]){
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    input.sync_with_stdio(false);
    output.sync_with_stdio(false);
    input.open("/users/jihan/Academic/Algorithmic Programming/Codeforces/CFTemplate/in.txt");
    output.open("/users/jihan/Academic/Algorithmic Programming/Codeforces/CFTemplate/out.txt");
    
    int tests;
    input>>tests;
    int biggest[20];
    
    
    
    string s;
    for (int test=1;test<=tests;test++){
        output<<"Case #"<<test<<": ";

        input>>s;
        for (int i=s.size()-1;i>=0;i--){
            biggest[0] = 0;
            for (int j=0;j<s.size();j++){
                biggest[j+1] = max(biggest[j], s[j]-'0');
                if (s[j] - '0' < biggest[j]){
                    s[j] = '9';
                    for (int k=j-1;k>=0;k--){
                        if (s[k] != '0'){
                            s[k]--;
                            break;
                        }
                        s[k] = '9';
                    }
                    for (int k=j+1;k<s.size();k++){
                        s[k] = '9';
                    }
                    break;
                }
            }/*
            if (s[i]-'0' < biggest[i]){
                s[i] = '9';
                for (int j=i-1;j>=0;j--){
                    if (s[j] != '0'){
                        s[j]--;
                        break;
                    }
                    s[j] = '9';
                }
                i = s.size();
            }*/
        }
        for (int i=0;i<s.size();i++){
            if (s[i] != '0'){
                s = s.substr(i);
                break;
            }
        }
        output<<s;
        output<<"\n";
    }
    
    return 0;
}
