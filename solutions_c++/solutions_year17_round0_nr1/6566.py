#include <cstdio>
#include<iostream>
#include<cmath>
using namespace std;
void flip(string &s,int i,int j){
    for(int p=i;p<=j;p++){
        if(s[p]=='+')s[p]='-';
        else s[p]='+';
    }
}
int main() {
    int t;
    cin>>t;
    while(t--){
        string s;int k;
        cin>>s;
        cin>>k;
        int c=0,m=0;
        for(int i=0;i<s.length();i++){
            if(s[i]=='-'){
                if((i+k-1)<s.length()){
                    flip(s,i,i+k-1);
                    c++;
                }
                else{
                    cout<<"Case #"<<100-t<<": "<<"IMPOSSIBLE"<<endl;m=1;
                    break;
                }
            }
        }
        if(m==0)cout<<"Case #"<<100-t<<": "<<c<<endl;
    }
    return 0;
}
