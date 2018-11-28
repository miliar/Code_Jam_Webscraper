#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;
int main(){

    freopen("B.in", "r", stdin); // redirects standard input
    freopen("output2.out", "w", stdout); // redirects standard output
    int t,f,l=0;
    //unsigned long long int n,temp,ans;
    string s;
    cin>>t;
    while(t--){
        cin>>s;
        l++;
        for(int i=0;i<s.length()-1;++i){
            if(s[i]>s[i+1]){
                for(int j=i+1;j<s.length();++j){
                    s[j]='9';
                }
                //int d = s[i]-'0';
                s[i] = s[i] - 1;
                for(int j=i;j>0;j--){
                    if(s[j]<s[j-1]){
                        s[j] = '9';
                        s[j-1] = s[j-1] - 1;
                    }
                }
                break;
            }
        }
        f=1;
        cout<<"Case #"<<l<<": ";
        for(int i=0;i<s.length();++i){
            if(f==1 && s[i]!='0'){
                f=0;
                cout<<s[i];
            }
            else if(s[i]!='0'){
                cout<<s[i];
            }
        }
        cout<<endl;
    }
    return 0;
}
