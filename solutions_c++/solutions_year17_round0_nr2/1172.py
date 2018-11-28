#include<bits/stdc++.h>
using namespace std;
bool istidy(string s){
for(int i=1;i<s.length();++i){
    if(s[i]<s[i-1]){
        return false;
    }
}
return true;
}

int main(){
    int t,x=1;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        bool f=false;string c=s;
        for(int i=s.length()-1;i>=0;--i){
            for(int j=9;j>=0;--j){
                c[i]=char('0'+j);
                if(c<=s&&istidy(c)){
                    int k=0;
                    while(c[k]=='0'){
                        ++k;
                    }
                    for(;k<c.length();++k){
                        cout<<c[k];
                    }cout<<endl;
                    f=true;
                    break;}
                if(f){
                    break;}}
            c[i]='9';}
    }
return 0;
}

