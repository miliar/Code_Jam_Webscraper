#include<bits/stdc++.h>

using namespace std;

int fun(string s, int k) {
    int res=0;
    for(int i=0; i<=s.length()-k; i++) {
        if(s[i]=='+')
            continue;
        res++;
        for(int j=i; j<i+k; j++) {
            if(s[j]=='+')
                s[j] = '-';
            else
                s[j] = '+';
        }
    }

    for(int i=s.length()-k; i<s.length(); i++)
        if(s[i]=='-')
            return -1;

    return res;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;

    for(int test=1; test<=t; test++) {
        string s;
        int k;
        cin>>s>>k;

        int res = fun(s, k);

        if(res==-1)
            cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<test<<": "<<res<<endl;
    }

    return 0;
}
