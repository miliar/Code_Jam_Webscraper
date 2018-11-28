#include <bits/stdc++.h>

using namespace std;

int t;
string s;

bool check(string st){
    for(int i = 1; i < st.length(); i++)
        if(st[i-1]>st[i]) return false;
    return true;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    //freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin>>t;
    for(int tt = 1; tt <= t; tt++){
        cin>>s;
        int len = s.length();
        int po = len-1;
        while(!check(s)){
            s[po] = '9';
            po--;
            while(s[po]=='0'){
                s[po] = '9';
                po--;
            }
            s[po] = s[po] - 1;
        }
        cout<<"Case #"<<tt<<": ";
        po = 0;
        while(s[po]=='0') po++;
        for(int i = po; i < len; i++) cout<<s[i];
        cout<<endl;
    }
    return 0;
}
