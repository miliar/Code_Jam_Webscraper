#include <bits/stdc++.h>
using namespace std;
string s;
int k;
int ans;
void solve(int i){
    ans += 1;
    if(i+k <= s.size()){
        int n = i + k;
        for(; i < n ; i++){
            if(s[i] == '+')
                s[i] = '-';
            else
                s[i] = '+';
        }
    }
}
int main(){
    freopen("in.txt" , "r" ,  stdin);
    freopen("out.txt" , "w" , stdout);
    int tc;
    scanf("%d" , &tc);
    for(int i = 1 ; i <= tc; i++){
        cin >> s >> k;
        ans = 0;
        set<char> var;
        for(int i = 0 ; i < s.size() ; i++){
            if(s[i]=='-'){
                solve(i);
            }
        }
        for(int i = 0 ; i < s.size() ; i++){
            var.insert(s[i]);
        }
        if(var.size() != 1){
            ans = -1;
        }
        cout << "Case #" << i << ": ";
        if(ans == -1){
            cout << "IMPOSSIBLE\n";
        }
        else{
            cout << ans << "\n";
        }
    }


}
