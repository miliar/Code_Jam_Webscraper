#include <bits/stdc++.h>
typedef unsigned long long LL;
using namespace std;
bool isTidy(LL no){
    stringstream ss;
    ss<<no;
    string s;
    ss>>s;
    for(int i=1;i<s.length();i++)
        if(s[i]<s[i-1]) return false;
    return true;
}
int main()
{
    int T,c=1;
    cin>>T;
    while(T--) {
        LL no;
        cin>>no;
        for(LL i=no;i>=1;i--)
            if(isTidy(i)){
                cout<<"Case #"<<c++<<": "<<i<<"\n";
                break;
            }

    }
    return 0;
}
