#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


using namespace std;


int main() {
    
    int t,i,j,count=0,num=0,len,k; string s; cin>>t;
    while(t--){
        count=0;
        cin>>s;        cin>>k;
        
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
        cout<<"Case #"<<++num<<": ";
        for(;i<len;i++) if(s[i]=='-') break;
        if(i==len) cout<<count;
        else cout<<"IMPOSSIBLE";
        
        cout<<endl;
        
    }
    
    
    return 0;
}
