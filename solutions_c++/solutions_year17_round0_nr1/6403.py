#include<bits/stdc++.h>
using namespace std;

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("Alarge.txt","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++){
        string s;
        int k;
        cin>>s>>k;
        int num=0;
        for(int i=0;i<=s.size()-k;i++){
            if(s[i]=='-'){
                num++;
                //cout<<i<<"  "<<i+k<<endl;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
            //cout<<s<<endl;
        }
        bool flag=false;
        for(int i=0;i<s.size();i++){
            if(s[i]=='-') flag=true;
        }
        if(flag) cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<tc<<": "<<num<<"\n";

    }
}
