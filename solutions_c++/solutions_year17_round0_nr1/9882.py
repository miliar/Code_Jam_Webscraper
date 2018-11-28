#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("codejam_output", "w", stdout);
    int ts;
    cin>>ts;
    for(int l = 1; l <= ts; l++){
    int k;
    string s;
    cin>>s;
    cin>>k;
    bool flip = false;
    int co = 0;
    for(int i = 0; i <=s.length()-k; i++){
        if(s[i] == '-'){
            for(int j = i; j <k+i; j++){
            if(s[j] == '-'){
                s[j] = '+';
            }
            else{
                s[j] = '-';
            }
        }
        co++;
        //cout<<s<<" and co = "<<co;
        }
    }
    flip = false;
    for(int i = 0; i<s.length(); i++){
        if(s[i] == '-'){
                flip = true;
            cout<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<endl;
            break;
        }
    }
    if(!flip){
            cout<<"Case #"<<l<<": "<<co<<endl;
    }
    }
    return 0;
}
