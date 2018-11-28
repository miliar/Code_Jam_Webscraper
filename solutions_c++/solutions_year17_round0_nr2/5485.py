#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

string lgs(string str) {
lint n = str.length();
lint i;

    for(i=0;i<n-1;i++)
    if(str[i]>str[i+1])
    break;

    if(i==n-1) return str;

    str[i]-=1;
    while(i<n-1)
    str[++i]='9';

    for(i=0;i<n-1;i++)
    if(str[i]>str[i+1])
    {
    while(i>=0 && str[i]>str[i+1]) {
    str[i]-=1;
    str[i+1]='9';
    i--;
    }
    break;
    }

    for(i=0;str[i]=='0';i++);


    return str.substr(i);
}

int main() {
lint t,test=0;cin>>t;
    while(t--)
    {
    string str;
    cin>>str;
    cout<<"Case #"<<(++test)<<": "<<lgs(str)<<endl;
    }

return 0;
}
