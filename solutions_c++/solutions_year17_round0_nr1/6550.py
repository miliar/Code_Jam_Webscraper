#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
char s[1024];
int main(){
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin>>t;
    for (int j=0; j<t; ++j){
        int k;
        cin>>s>>k;
        int n = strlen(s);
        int ans = 0;
        for (int i=0; i<=n-k; ++i){
            if (s[i]=='-'){
                for (int j=0; j<k; ++j){
                    if (s[i+j]=='+'){s[i+j]='-';}
                    else {s[i+j]='+';}
                }
                ++ans;
            }
        }
        for (int i=n-k+1; i<n; ++i){
            if (s[i]=='-'){ans=-1;}
        }
        cout<<"case #"<<j+1<<": ";
        if (ans==-1){cout<<"IMPOSSIBLE\n";}
        else{cout<<ans<<"\n";}
    }
    return 0;
}
