#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t,ti=0;
    cin>>t;
    while(t--)
    {
        ti++;
        string st;
        cin>>st;
        char prev=st[st.size()-1];
        ll i=st.size()-1;
        while(i>=0)
        {
            if(st[i]>prev)
            {
                st[i]--;
                for(int j=i+1;j<st.size();j++)
                    st[j]='9';
            }
            prev=st[i];
            i--;
        }
        cout<<"Case #"<<ti<<": ";
        if(st[0]=='0')
            cout<<st.substr(1,st.size()-1)<<"\n";
        else
        cout<<st<<"\n";
    }
}
