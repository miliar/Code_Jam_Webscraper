#include <bits/stdc++.h>

using namespace std;

char rev(char s){
    if(s == '+')
        return '-';
    return '+';
}


int t, k, ret, stop;
string s;

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin>>t;
    for(int i = 0; i < t; i ++ ){
        cout<<"Case #"<<i + 1<<": ";
        cin>>s>>k;
        stop = false;
        ret = 0;
        for(int j = 0; j < s.length(); j++){
            if(s[j] == '-'){
                if(j + k <= s.length()){
                    ret++;
                    for(int m = 0; m < k; m++){
                        s[j + m] = rev(s[j + m]);
                    }
                }else{
                    stop = true;
                    break;
                }
            }
        }
        if(stop){
            cout<<"IMPOSSIBLE\n";
        }else{
            cout<<ret<<endl;
        }
    }

    return 0;
}
