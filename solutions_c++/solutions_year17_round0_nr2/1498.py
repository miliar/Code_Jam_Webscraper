#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int check(string s){
    int cnt=0;
    
    for(int i=0;i<s.length()-1;i++){
        if(s[i]-'0'<=s[i+1]-'0') cnt++;
    }
    if(cnt==s.length()-1) return 1;
    else return 0;
}
int main() {
    int t;
    cin>>t;int c=0;
  //  int c=0; 
    while(t--){
        c++;
    string s;
        cin>>s;
        int n=s.length();
        if(s.length()==1){
            cout<<"Case #"<<c<<": ";
            cout<<s<<endl;
            continue;
        }
        
        
        while(1){
            bool flag=true;
        for(int i=0;i<s.length();i++){
            if(flag ){
            if(i!=s.length()-1){    
            if(s[i]-'0'<=s[i+1]-'0') continue;
                else { 
                    
                   // int tmp=s[i]-'0'-1;
                    s[i]=s[i]-1;
                    flag=false;
                     
                     }
            }
                }
            else {
                s[i]='9';
            }
        }
        if(check(s)==1) break;
         //   cout<<s<<endl;
        }
        unsigned long long int ans=0;
    //    cout<<s<<endl;
        for(int i=n-1;i>=0;i--){
           // cout<<"i="<<i<<"   ";
            //cout<<s[i]-'0'<<" ";
            unsigned long long int p=pow(10,n-i-1);
            ans=ans+(s[i]-'0')*p;
           // cout<<"ans="<<ans<<endl;
        }
        cout<<"Case #"<<c<<": ";
        cout<<ans<<endl;
     //  cout<<s<<endl;
        
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
