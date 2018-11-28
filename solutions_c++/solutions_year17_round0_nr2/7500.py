#include <iostream>
#include <cstdio>
using namespace std;
int main(){
    freopen("B-large.in" , "r" , stdin);
    freopen("B-large.out" , "w" , stdout);
    int n;
    cin>>n;
    for(int z=1;z<=n;z++){
        string s,ans;
        cin>>s;
        for(int j=s.size()-1;j>0;j--){
            if(s[j-1]>s[j]){
                s[j-1]--;
                for(int i=j;i<s.size();i++)
                    s[i]='9';
            }
        }
        ans="";
        int i=0;
        while(s[i]=='0')
            i++;
        for(;i<s.size();i++)
            ans+=s[i];
        cout<<"Case #"<<z<<": ";
        cout<<ans<<endl;
    }
    return 0;
}
