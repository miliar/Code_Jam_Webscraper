#include<iostream>
#include<string>
using namespace std;
int T;
string S;
void flip(string& s,int t){
    for(;t<s.size();t++)
        s[t]='9';
}
string solve(string s){
    for(int i=s.size()-1;i>0;i--){
       if(s[i]<s[i-1]){
           s[i-1] -= 1;
           flip(s,i);
       }
    }
    for(int i=0;i<s.size();i++){
       if(s[i]!='0')
           return s.substr(i);
    }
    return "0";
}
int main(){
    cin>>T;
    for(int _c=1;_c<=T;_c++){
        cin>>S;
        cout<<"Case #"<<_c<<": "<<solve(S)<<endl;
    }
    return 0;
}
