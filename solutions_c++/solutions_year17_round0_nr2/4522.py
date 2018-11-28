#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
string d_digit(int d,char c){
    string ans="";
    while(d--){
        ans=ans+c;
    }
    return ans;
}
int cmp(string s1,string s2,int d){
    for(int i=0;i<d;i++){
        if(s1[i]>s2[i]){
            return 1;
        }else if(s1[i]<s2[i]){
            return -1;
        }
    }
    return 0;
}
bool isTidy(string s,int d){
    for(int i=1;i<d;i++){
        if(s[i]<s[i-1]){
            return false;
        }
    }
    return true;
}
int main(){
    int t,x;
    string s;
    cin>>t;
    for(x=1;x<=t;x++){
        cin>>s;
        cout<<"Case #"<<x<<": ";
        int d=s.length();
        string s1=d_digit(d,'1');
        if(isTidy(s,d)){
            cout<<s<<endl;
        }else if(cmp(s,s1,d)==-1){
            cout<<d_digit(d-1,'9')<<endl;
        }else{
            while(!isTidy(s,d)){
                for(int i=0;i<(d-1);i++){
                    if(s[i]>s[i+1]){
                        s[i]=s[i++]-1;
                        while(i<d){
                            s[i++]='9';
                        }
                        break;
                    }
                }
            }
            cout<<s<<endl;
        }
    }
    return 0;
}
