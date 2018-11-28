#include<bits/stdc++.h>

using namespace std;

string flip(string s, int i, int k, int direction){
    if(direction){
        int c = 0;
        while(c < k){
            if(s[i] == '+'){
                s[i] = '-';
            }else{
                s[i] = '+';
            }
            c++;
            i++;
        }
        return s;
    }else{
        int c = 0;
        while(c < k){
            if(s[i] == '+'){
                s[i] = '-';
            }else{
                s[i] = '+';
            }
            i--;
            c++;
        }
        return s;
    }
}

bool checkIfHappy(string s){
    for(int i = 0; i < s.length(); i++){
        if(s[i] == '-')
            return false;
    }
    return true;
}

int main(){

    int t, l;
    string s;
    cin>>t;
    for(l = 0; l < t; l++){
        int k, i, j, ans = 0, flag = 1;
        cin>>s>>k;
        i = 0;
        j = s.length() - 1;
        while(j - i + 1 >= k){
       // cout<<s[i]<<s[j];
            if(s[i] == '-'){
                s = flip(s, i, k, 1);
                ans++;
            }
            if(s[j] == '-'){
                s = flip(s, j, k, 0);
                ans++;
            }
            if(s[i] == '-' || s[j] == '-'){
                flag = 0;
                break;
            }
            i++;
            j--;
        }
        if(flag && checkIfHappy(s)){
            cout<<"Case #"<<l+1<<": "<<ans<<endl;
        }else{
            cout<<"Case #"<<l+1<<": "<<"IMPOSSIBLE"<<endl;
        }
    }
return 0;
}
