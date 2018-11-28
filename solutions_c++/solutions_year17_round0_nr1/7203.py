#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<cmath>
#include<set>
#include<map>

using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,k;
    string s;
    cin>>T;
    for(int t=1; t<=T; t++) {

        cin>>s>>k;

        int n = s.size(), ans = 0;
        for(int i=0; i<n; i++) {
            if(s[i]=='+') continue;
            if(i+k<=n) {
                for(int j=i; j<i+k; j++)
                    if(s[j]=='+') s[j]='-';
                    else s[j]='+';
                ans++;
            }else {
                ans = n+1;
                break;
            }
        }
        cout<<"Case #"<<t<<": ";
        if(ans>n) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
}
