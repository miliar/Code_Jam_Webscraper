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
    int k, n;
    string s;
    input>>tests;
    for (int test=1;test<=tests;test++){
        output<<"Case #"<<test<<": ";
        n = 0;
        input>>s>>k;
        for (int i=0;i<s.size()-k+1;i++){
            if (s[i] == '-'){
                n++;
                for (int j=i;j<i+k;j++){
                    if (s[j] == '+'){
                        s[j] = '-';
                    }
                    else s[j] = '+';
                }
            }
        }
        for (int i=0;i<s.size();i++){
            if (s[i] == '-'){
                output<<"IMPOSSIBLE";
                break;
            }
            if (i == s.size()-1){
                output<<n;
            }
        }
        output<<"\n";
    }
    
    return 0;
}
