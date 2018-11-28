#include <iostream>
#define ll long long
#include <algorithm>

using namespace std;
string test (string s){
    for(int i=s.length()-1;i>0;--i){
        if(int(s[i]-'0')<int(s[i-1]-'0')){
            int aux=s[i-1]-'0'-1;
            s[i-1]=aux+48;
            for(int j=i;j<s.length();++j)
                s[j]='9';
        }

    }
    for(int i=0;i<s.length();++i)
    {
        if(s[i]=='0'){
            s.erase(s.begin());
            i--;
        }
        else
            break;
    }
    return s;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("res.txt","w",stdout);
    int t;
    cin>>t;
    int i=0;
    while(t--){
    i++;
    string a;
    cin>>a;
    cout<<"Case #"<<i<<": "<<test(a)<<endl;
    }
    return 0;
}
