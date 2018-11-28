#include<bits/stdc++.h>
using namespace std;

string process(string s){
    bool flag=false;
    if(s.size()==1) return s;
    for(int i=1;i<s.size();i++){
        if(flag){
            s[i]='9';
            continue;
        }
        if(s[i-1]>s[i]){
            s[i-1]--;
            s[i]='9';
            flag=true;
        }
    }
    string s1;
    int i=0;
    while(s[i]=='0') i++;
    for(i;i<s.size();i++) s1+=s[i];
    return s1;
}
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("blarge.txt","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++){
        string s;
        cin>>s;
        bool flag=true;
        while(flag){

           s=process(s);
           //cout<<s<<endl;
           flag=false;
           for(int i=1;i<s.size();i++){
                if(s[i]<s[i-1]) {
                    flag=true;
                    break;
                }
           }
        }

        cout<<"Case #"<<tc<<": "<<s<<"\n";

    }
}
