#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


using namespace std;


int main() {

    vector <char> arr;
    int t,i,j,count=0,num=0,len,k; string s; int a; cin>>t;
    while(t--){
        count=0;
        cout<<"Case #"<<++num<<": ";
        cin>>s;
        cin>>k;
        
        len=s.size();
        
        for(i=0;i<=len-k;i++){
            if(s[i]=='-'){
                count++;
                for(j=i;j<i+k;j++){
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
        }
        i--;
        for(;i<len;i++) if(s[i]=='-') break;
        if(i==len) cout<<count<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
        
        
        
    }
    
    
    return 0;
}