#include <bits/stdc++.h>

using namespace std;
#define ll long long

void success(int res){
    cout<<res<<endl;
}

ll last(string s){
    int slen = s.length();
    int k=slen-1;
    for(int i=slen-2;i>=0;i--){
        if(s[i]>s[i+1]){
            k = i;
            s[i]-=1;
        }
    }
    for(int j=k+1;j<slen;j++){
        s[j] = '9';
    }
    ll ans =0;
    for(int i=0;i<slen;i++){
        ans = ans*10 + (s[i]-'0');
    }
    return ans;
}

int main()
{
    freopen("B2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int iter=1;iter<=T;iter++){
        string s;
        cin>>s;
        cout<<"Case #"<<iter<<": "<<last(s)<<endl;


    }
}

