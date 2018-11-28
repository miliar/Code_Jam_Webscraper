#include<bits/stdc++.h>
using namespace std;
bool check(string str){
    for(int i = 0; i < str.length()-1; i++){
        if(str[i] > str[i+1]) return false;
    }
    return true;
}
string reduce(string str){
    string ans;
    for(int i = 0; i < str.length()-1; i++){
        if(str[i] > str[i+1]){
            for(int j = 0; j < i; j++){
                ans += str[j];
            }
            ans += str[i]-1;
            for(; i+1 < str.length(); i++){
                ans += "9";
            }
            break;
        }
    }
    return ans;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("B-large.in.txt","r",stdin);
    freopen("outlarge.txt","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        string str;
        cin >> str;
        string ans = str;
        while(!check(ans)){
            ans = reduce(ans);
        }
        if(ans.length() != 0){
            while(ans[0] == '0'){
                ans.erase(ans.begin());
            }
        }
        if(ans.length() == 0){
            cout << str << "\n";
        }
        else{
            cout << ans << "\n";
        }
    }
    return 0;
}
