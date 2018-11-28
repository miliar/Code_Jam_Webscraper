#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;

#define vi vector<int>
#define pb push_back
#define rep(i,a,b) for(register int i=a;i<b;i++)

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    string s;
    cin>>t;
    rep(i,0,t)
    {
        cin>>s;
        cout<<"Case #"<<i+1<<": ";
        vector<char> h(s.size());
        h[h.size()-1]=s[s.size()-1];
        for(int j=h.size()-2;j>-1;j--)
        {
            if(s[j]<=h[j+1])
                h[j]=s[j];
            else
                h[j]=s[j]-1;
        }
        rep(j,0,s.size())
        {
            if(h[j]==s[j])
                cout<<h[j];
            else
            {
                if(h[j]!='0')
                cout<<h[j];
                rep(k,j+1,s.size())
                {
                    cout<<9;
                }
                break;
            }
        }
        cout<<'\n';
    }
}
