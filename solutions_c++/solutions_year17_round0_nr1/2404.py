#include <bits/stdc++.h>
using namespace std;

char rev(char be) {
    if(be=='+') {
        return '-';
    }
    return '+';
}

int main()
{
    freopen("be.txt","r",stdin);
    freopen("ki.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=0;tc<t;tc++) {
        string s; int k;
        cin>>s>>k;
        int sol=0;
        for(int i=0;i<=s.size()-k;i++) {
            if(s[i]=='-') {
                for(int j=i;j<i+k;j++) {
                    s[j]=rev(s[j]);
                }
                sol++;
            }
        }
        for(int i=s.size()-k+1;i<s.size();i++) {
            if(s[i]=='-') {
                sol=-1;
            }
        }
        if(sol!=-1) {
            cout<<"Case #"<<tc+1<<": "<<sol<<endl;
        }
        else {
            cout<<"Case #"<<tc+1<<": IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
