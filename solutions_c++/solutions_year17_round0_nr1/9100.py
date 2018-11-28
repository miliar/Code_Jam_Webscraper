#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int t,k,flag,count;
    string s;
    cin>>t;
    int p=1;
    while(t--){
       cin>>s>>k;
       int n=s.length();
       flag=0;
       count=0;
        for(int i=0;i<n-k+1;i++){
            if(s[i]=='-'){
            for(int j=i;j<i+k;j++){
                if(s[j]=='-')s[j]='+';
                else s[j]='-';
            }
                count++;
            }
        }
          for(int i=0;i<n;i++){
            if(s[i]=='-'){
            flag=1;
            break;
            }
        }
        if(flag==1)cout<<"Case #"<<p++<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<p++<<": "<<count<<endl;
    }
    
}

