#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    int j=1;
    string s;
    int n;
    while(t--){
        int cnt=0;
        cin>>s>>n;
        int i=0;
        for(;i<=s.size()-n;i++){
            if(s[i]=='+') {
                continue;
            }
            else{
                cnt++;
                for(int j=i;j<i+n;j++){
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
        }
        bool flag=0;
        for(;i<s.size();i++){
            if(s[i]=='-'){
                flag=1;
                break;
            }
        }
        if(flag==1) cout<<"Case #"<<j++<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<j++<<": "<<cnt<<endl;
    }
    return 0;
}
