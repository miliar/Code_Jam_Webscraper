#include<bits/stdc++.h>

using namespace std;
string s;

void makenine(int k){
    for(int i=k;k<s.size();k++)s[k]='9';
}

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("tidy.txt","w",stdout);
    int T;
    cin>>T;
    for(int O=0;O<T;O++){
       cin>>s;

        for(int i=0;i<s.size()-1;i++){
            if(s[i]>s[i+1]){
                s[i]--;
                makenine(i+1);
                i=-1;
            }
        }
        string ans="";
        bool fnd=false;
        for(int i=0;i<s.size();i++){
            if(s[i]=='0'&&fnd)ans+=s[i];
            if(s[i]!='0'){
                ans+=s[i];
                fnd=true;
            }
        }


    cout<<"Case #"<<O+1<<": "<<ans<<endl;
    }
}
