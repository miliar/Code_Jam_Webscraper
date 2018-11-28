#include <bits/stdc++.h>

using namespace std;

int main()
{  freopen("A-large.in","r+",stdin);
    freopen("A-large.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1; j<=t; j++){
        string s;
        cin>>s;
        int k, cpt=0,flag=1;
        cin>>k;
       for(int i=0; i<=s.size()-k; i++){
        if (s[i]=='-')  {cpt++;
        for(int j=0; j<k; j++) {
            if (s[i+j]=='-') s[i+j]='+';
            else s[i+j]='-';
        }}
       }
       //cout<<s;
       for(int i=0; i<s.size(); i++)
       if(s[i]=='-') {flag=0; break;}
       cout<<"Case #"<<j<<": ";
        if(!flag) cout<<"IMPOSSIBLE";
        else cout<<cpt;
            cout<<endl;
    }

            return 0;
}
