#include <iostream>
#include <cstdio>
using namespace std;
int main(){
    freopen("A-large.in" , "r" , stdin);
    freopen("A-large.out" , "w" , stdout);
    int n;
    cin>>n;
    for(int z=1;z<=n;z++){
        string s;
        int k;
        cin>>s>>k;
        int ans=0;
        for(int i=0;i<=s.size()-k;i++){
            if(s[i]=='-'){
                ans++;
                for(int j=i;j<i+k;j++)
                    s[j]=(s[j]=='-' ? '+' : '-');
            }
        }
        for(int i=0;i<s.size();i++)
            if(s[i]=='-')
                ans=-1;
        cout<<"Case #"<<z<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
    }
    return 0;
}
