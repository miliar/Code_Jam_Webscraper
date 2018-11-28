#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    for(int cases=1;cases<=t;cases++){
            string s;
            cin>>s;
            int k;
            cin>>k;
            int ans=0;
            for(int i=0;i<=s.size()-k;i++)
            {
                    if(s[i]=='-')
                    {
                        for(int j=i;j<i+k;j++)
                        {
                            if(s[j]=='-')
                                s[j]='+';
                            else
                                s[j]='-';
                        }
                        ans++;
                    }
            }

            int flag=1;
            for(int i=s.size()-k;i<s.size();i++)
            if(s[i]=='-')
            {
                flag=0;
                break;
            }
            cout<<"Case #"<<cases<<": ";
            if(flag)
            cout<<ans<<endl;
            else
            cout<<"IMPOSSIBLE"<<endl;

    }

    return 0;
}