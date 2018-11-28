#include<iostream>
#include<vector>
using namespace std;

#define vi vector<int>
#define rep(i,a,b) for(register int i=a;i<b;i++)

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t,C,k;
    string s;
    cin>>t;
    rep(i,0,t)
    {
        C=0;
        cin>>s>>k;
        cout<<"Case #"<<i+1<<": ";
        rep(j,0,s.size()-k+1)
        {
            if(s[j]=='-')
            {
                C++;
                rep(h,0,k)
                {
                    s[j+h]=((s[j+h]=='+')?'-':'+');
                }
            }
        }
        bool f=1;
        rep(j,s.size()-k+1,s.size())
        {
            if(s[j]=='-')
            {
                cout<<"IMPOSSIBLE\n";
                f=0;
                break;
            }
        }
        if(f)
            cout<<C<<'\n';
    }
}
