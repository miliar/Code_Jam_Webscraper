#include <bits/stdc++.h>
using namespace std;
string str;
bool foo = true;
string ans;
int solve(string var){
        //cout << var << "\n";
        if(var.size() == str.size()){
                ans = var;
                return (var <= str);
        }
        for(char ch = '9' ; ch >= '0' && foo; ch --){
                string can = var + ch;
                //cout << can << " ";
                int id1 = int(can.size()) - 1;
                int id2 = int(can.size()) - 2;
                char cur = can[id1];
                char prev = can[id2];
                //cout << cur << " " << prev << "\n";
                string x = str.substr(0,var.size() + 1);
                if(can <= x && cur >= prev){
                        if(solve(can) == true)
                                foo = false;
                }
        }
}
int main(){
        freopen("in3.txt" , "r" ,  stdin);
        freopen("out.txt" , "w" , stdout);
        int tc;
        cin >> tc;
        for(int tcase = 1 ; tcase <= tc ; tcase ++){
        cin >> str;
        ans = "-1";
        foo = true;
        for(char i = '9' ; i >= '0' ; i--){
                if(str[0] >= i){
                        string var = "";
                        var += i;
                        solve(var);
                        if(ans !="-1")
                                break;
                        //cout << "Ans :" << ret << "\n";
                }
        }
        //ans = "0000000021";
        //cout << ans << "\n";
        int id = 0;
        string fans = "";
        for(;id < ans.size() ; id++){
                if(ans[id] != '0')
                        break;
        }
        for(;id < ans.size() ; id++)
                fans+=ans[id];
        cout <<"Case #" << tcase << ": " <<  fans << "\n";
        }
}
