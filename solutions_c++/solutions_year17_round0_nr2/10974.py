#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    freopen("out.txt", "w", stdout);
    freopen("B-small-attempt0.in", "r", stdin);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        cout<<"Case #"<<tt<<": ";
        ll x;
        cin>>x;
        vector<int>v;
        while(x)
        {
            v.push_back(x%10);
            x/=10;
        }
        reverse(v.begin(),v.end());
        int idx=0,tmp=0;
        bool f=0;
        for(int i=0;i<v.size()-1;i++)
        {
            if(v[i]>v[i+1])
            {
               idx=tmp;
               f=1;
            }
            else if(v[i]<v[i+1])
                tmp=i+1;
        }
        if(f==0)
        {
            for(int i=0;i<v.size();i++)
                cout<<v[i];
            cout<<endl;
        }
        else if(idx==0&&v[0]==1)
        {
            for(int i=0;i<v.size()-1;i++)
                cout<<9;
            cout<<endl;
        }
        else
        {
            for(int i=0;i<idx;i++)
                cout<<v[i];
            cout<<v[idx]-1;
            for(int i=idx+1;i<v.size();i++)
                cout<<9;
            cout<<endl;
        }

    }
    return 0;
}
