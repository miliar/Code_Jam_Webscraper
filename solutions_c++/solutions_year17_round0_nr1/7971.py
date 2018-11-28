#include <bits/stdc++.h>
using namespace std;

int func(string s, int k)
{
    if((int)s.size()<k) return 0;
    int ans=0;
    for(int i=0; i<s.size(); i++) {
        if(s[i]=='-') {
            if(i+k>(int)s.size()) {
                return -1;
            }
            for(int j=i; j<i+k; j++) {
                if(s[j]=='-') {
                    s[j]='+';
                }
                else {
                    s[j]='-';
                }
            }
            ans++;
            //cout<<s<<endl;
        }
    }
    return ans;
}

int main ()
{
    //freopen("output.txt", "w", stdout);
    int cs; cin>>cs;
    for(int t=1; t<=cs; t++) {
        int k; string s;
        cin>>s>>k;
        int ret=func(s, k);
        printf("Case #%d: ", t);
        if(ret==-1) {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<ret<<endl;
    }
    return 0;
}
