#include<bits/stdc++.h>
using namespace std;
int main(){
    int tc,n,mas,tot=0,ans,l,r;
    bool ban=true;
    string str;
    cin>>tc;
    for(int t=1; t<=tc; t++){
        cin>>str>>n;
        l=0,r=str.size()-1,tot=0;
        for(int i=0; i<str.size(); i++)
            tot+=str[i]=='+';
        ans=0;
        ban=true;
        while(l+n<=str.size()||r-n>=0){
            mas=0;
            if(ban){
                while(l+n<=str.size()&&str[l]!='-') l++;
                if(l+n>str.size()) break;
                for(int i=l; i<l+n; i++){
                    if(str[i]=='-'){
                        str[i]='+';
                        mas++;
                    }
                    else str[i]='-';
                }
                tot+=2*mas-n;
                ans++;
                l++;
            }
            else{
                while(r-n>=0&&str[r]!='-') r--;
                if(r-n<0) break;
                for(int i=r; i>r-n; i--){
                    if(str[i]=='-'){
                        str[i]='+';
                        mas++;
                    }
                    else str[i]='-';
                }
                tot+=2*mas-n;
                ans++;
                r--;
            }
            ban=!ban;
        }
        if(tot==str.size())
            cout<<"Case #"<<t<<": "<<ans<<endl;
        else
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
    }
}
