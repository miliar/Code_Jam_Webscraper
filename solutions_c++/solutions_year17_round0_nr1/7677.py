#include <bits/stdc++.h>
using namespace std;
string str;
        int n;
void flip(int s){
    for(int i = s;i< s + n;i++){
        str[i] = (str[i] == '+') ? '-' : '+';
    }
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for(int cs = 0;cs < tc;cs++){
        int cnt = 0;
        cin >> str >> n;
        for(int i = 0;i < str.size() - n + 1;i++){
            if(str[i] == '-'){
                cnt++;
                flip(i);
            }
        }
        bool f = true;
        for(int i = str.size() - n + 1;i < str.size();i++){
            if(str[i] == '-'){
                f = false;
                break;
            }
        }
        if(f)
            printf("Case #%d: %d\n", cs + 1, cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n", cs + 1);
    }
}
