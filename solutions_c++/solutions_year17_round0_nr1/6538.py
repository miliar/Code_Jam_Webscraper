#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int main() {
    int n;
    // freopen("A-large.in","r",stdin);
    // freopen("A-large.out","w",stdout);
    cin>>n;
    for(int i=1;i<=n;i++) {
        printf("Case #%d: ",i );
        string s;
        int k;
        cin>>s>>k;
        int l = s.length();
        int cnt=0;
        for(int i=0;i<=l-k;i++)
        {
            if(s[i]=='-') {
                cnt++;
                for(int j=i;j<i+k;j++)
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
            }
            // cout<<s<<endl;
        }
        bool flag=0;
        for(int i=0;i<l;i++)if(s[i]=='-')flag=1;
        if(flag)cout<<"IMPOSSIBLE"<<endl;
        else cout<<cnt<<endl;
    }
}