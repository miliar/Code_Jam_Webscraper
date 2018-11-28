#include<bits/stdc++.h>
using namespace std;
string s;
int d;
int ans(){
    int k=0;
    for(int i=0;i<s.size()-d+1;i++){
        if(s[i]=='-'){
            k++;
        for(int j=i;j<s.size()&&j<i+d;j++){
            if(s[j]=='+')
                s[j]='-';
            else
                s[j]='+';
        }
        }
    }
    for(int i=0;i<s.size();i++){
        if(s[i]=='-')
            return -1;
    }
    return k;
}
int main(){
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        cin>>s>>d;
        int val=ans();
        if(val==-1)
            cout<<"Case #"<<ii<<": "<<"IMPOSSIBLE"<<' '<<endl;
        else
            cout<<"Case #"<<ii<<": "<<val<<' '<<endl;
    }
    return 0;
}
