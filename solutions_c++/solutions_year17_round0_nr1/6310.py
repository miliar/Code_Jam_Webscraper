#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t, k, i, j, len, ct;
    cin >> t;
    for(int l=1; l<=t; l++){
        ct = 0;
        string s;
        cin >> s >> k;
        len = s.length();
        for(i=0; i<len; i++){
            if(s[i]=='-'){
                ct++;
                for(j=i; j<len && j<i+k; j++){
                    if(s[j]=='-'){
                        s[j]='+';
                    }
                    else{
                        s[j]='-';
                    }
                }
                if(j != i+k && i+k >= len){
                    cout << "CASE #" << l << ": " << "IMPOSSIBLE" << endl;    
                    j = -1;
                    break;
                }
            }
        }
        if(j!=-1){
            cout << "CASE #" << l << ": " << ct << endl;
        }
    }
    return 0;
}
