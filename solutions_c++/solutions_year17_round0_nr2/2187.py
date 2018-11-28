#include <bits/stdc++.h>

using namespace std;

int t, stop;
char cur;
string s;
long long ret = 0;

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    cin>>t;
    for(int i = 0; i < t; i++){
        cout<<"Case #"<<i+1<<": ";
        cin>>s;
        cur = '0';
        stop = false;
        for(int j = 0; j < s.length(); j++){
            if(s[j] < cur){
                ret = 0;
                int k = 0;
                for(k = 0; k < j; k++){
                    if(s[k] < cur){
                        ret = ret*10 + (s[k] - '0');
                    }else{
                        ret = ret*10 + (s[k] - '1');
                        break;
                    }
                }
                for(k = k +1; k < s.length(); k++){
                    ret = ret*10 + 9;
                }
                stop = true;
                break;
            }else{
                cur = s[j];
            }
        }
        if(!stop){
            cout<<s<<endl;
        }else{
            cout<<ret<<endl;
        }
    }

    return 0;
}
