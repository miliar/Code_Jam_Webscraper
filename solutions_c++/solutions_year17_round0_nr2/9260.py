#include<iostream>
#include<string>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
    string s;
    int sumn,maxn=0;
    int t;
    ifstream ins("f:\B-large.in",ios::in);
    ofstream ous("f:\B-large.out",ios::out);
    ins>>t;
    for(int k=0;k<t;k++){
        ins>>s;
        if(s.length()==1){
            ous<<"Case #"<<(k+1)<<": "<<s<<endl;
            continue;
        }
        for(int i=s.length()-1;i>0;i--){
            if(s[i]<s[i-1]){
                s[i]='9';
                if(s[i-1]>'0'){
                    s[i-1]--;
                }else if(i==1){
                    s[i-1]='0';
                }else{
                    s[i-1]='9';
                    s[i-2]--;
                }
            }else if((i-2>=0)&&(s[i-1]=='0')){
                s[i]='9';
                s[i-1]='9';
                s[i-2]--;
            }
            if(i+1<s.length() && s[i+1]<s[i]){
                    for(int m=i;m<s.length();m++){
                        s[m]='9';
                    }
                }
        }
            ous<<"Case #"<<(k+1)<<": ";
            for(int l=0;l<s.length();l++){
                if(s[l]!='0'){
                    ous<<s[l];
                }
            }
            ous<<endl;
    }
    ins.close();
    ous.close();
return 0;
}
