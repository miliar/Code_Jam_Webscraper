#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

using namespace std;

int main(){
    int n, i, count, flag;
    string s;
    cin >> n;
    vector<string> pan;
    int k[n];
    for(i=0; i<n; ++i){
        cin >> s >> k[i];
        pan.push_back(s);
    }
    i = 0;
    while(i < n){
        s = pan[i];
        count = 0;
        flag = 0;
        for(int j = 0; j<s.size(); ++j){
            if(s[j] == '-'){
                if(j+k[i] > s.size()) {flag = 1; break;}
                else{
                    for(int m = 0; m<k[i]; ++m) s[j+m] = (s[j+m] == '-')?'+':'-';
                    count++;
                }
            }
        }
        (flag)?printf("Case #%d: IMPOSSIBLE\n", i+1):printf("Case #%d: %d\n", i+1, count);
        ++i;
    }
    return 0;
}
