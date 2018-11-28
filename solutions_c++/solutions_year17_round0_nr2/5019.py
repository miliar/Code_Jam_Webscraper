#include <bits/stdc++.h>
#define ll long long

using namespace std;

string last(string s){
    while(s[0]=='0')s.erase(s.begin());
    string ret;
    int i(0);
    while(i<s.size()-1 && s[i]<=s[i+1])++i;
    if(i==s.size()-1)return s;
    while(i && char(s[i]-1)<s[i-1])--i;
    for(int j=0;j<i;++j)ret += s[j];
    if(s[i]!='1')ret += char(s[i]-1);
    for(int j=i+1;j<s.size();++j)ret += '9';
    while(ret[0]=='0')ret.erase(ret.begin());
    return ret;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs(0);
    cin>>t;
    string s;
    while(t--){
        cs++;
        cin>>s;
        cout<<"Case #"<<cs<<": "<<last(s)<<"\n";
    }
    return 0;
}
