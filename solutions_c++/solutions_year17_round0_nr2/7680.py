#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for(int cs = 0;cs < tc;cs++){
        string s;
        cin >> s;
        int f = 0;
        for(int i = 1;i < s.size();i++){
             if(s[i] < s[i - 1]){
                s[f] = s[f] - 1;
                for(int j = f + 1;j < s.size();j++){
                    s[j] = '9';
                }
            }else if (s[i] > s[i - 1]){
                f = i;
            }
        }
        if(s[0] == '0')s = s.substr(1);
        printf("Case #%d: %s\n", cs + 1, s.c_str());

    }
}
