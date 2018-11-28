#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    int j=1;
    long long int x;
    string s;
    cin>>t;
    while(t--){
        cin>>x;
        s=to_string(x);
        //cout<<s<<" ";
        int i=0;
        bool flag=0;
        for(;i<s.size();i++){
            if(i>0 && (s[i]-'0'<s[i-1]-'0')){
                flag=1;
                break;
            }
        }
        if(flag==0){
            cout<<"Case #"<<j++<<": "<<x<<endl;
            continue;
        }
        int maxi=--i;
        //cout<<i<<" ";
        while(i>0 && s[i]==s[i-1]){
            i--;
        }
        //cout<<i<<" ";
        s[i]=s[i]-1;
        i++;
        for(;i<s.size();i++){
            s[i]='9';
        }
        //cout<<s<<" ";
        x=stoll(s);
        cout<<"Case #"<<j++<<": "<<x<<endl;
    }
    return 0;
}
