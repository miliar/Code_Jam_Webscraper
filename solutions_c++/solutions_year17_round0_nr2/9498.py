#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int t,flag=0;
    string s;
    cin>>t;
    int p=1;
    while(t--){
        flag=0;
        cin>>s;
        int n=s.length();
         for(int i=0;i<n;i++){
            if(s[i]==s[i+1]){
            flag++;
            }
             if(flag==1){
                for(int i=0;i<n-1;i++){
                flag=1;
                if(s[i]<=s[i+1]){
                    flag=0;
                }
                }
             }
            if(flag==1){
                s[0]=s[0]-1;
                for(int i=1;i<n;i++){
                    s[i]='9';
                }
            }
            break;
        }
       
          if(flag!=2){ 
              for(int i=0;i<n-1;i++){
                if(s[i]>s[i+1])
                {
                s[i]=s[i]-1;
                for(int j=i+1;j<n;j++){
                    s[j]='9';
                }
                break;
            }
         }
          }
        cout<<"Case #"<<p++<<": ";
        for(int i=0;i<n;i++){
             if(s[i]!='0') cout<<s[i];
           }
        cout<<endl;
         }
    }

