#include <bits/stdc++.h>
using namespace std;

vector<long long>v;

map<long long,long long>mp;

ifstream fin("C-large.in");
ofstream fout("C-large.sol");

void solve(long long x)
{
    int i;
    if(x==0)return;
    if(x%2==1)
    {
        i=0;
        for(i=0;i<v.size();i++)
        {
            if(v[i]==x/2)
            {
                break;
            }
        }
        if(i==v.size())
        {
            v.push_back(x/2);
            solve(x/2);
        }
    }
    else
    {
        i=0;
        for(i=0;i<v.size();i++)
        {
            if(v[i]==x/2)
            {
                break;
            }
        }
        if(i==v.size())
        {
            v.push_back(x/2);
            solve(x/2);
        }
        i=0;
        for(i=0;i<v.size();i++)
        {
            if(v[i]==(x/2-1))
            {
                break;
            }
        }
        if(i==v.size())
        {
            v.push_back((x/2-1));
            solve(x/2-1);
        }
    }
}

int main()
{
    int t;
    long long n,k,ans;
    fin>>t;
    for(int i=0;i<t;i++)
    {
        long long r=0;
        v.clear();
        mp.clear();
        fin>>n>>k;
        v.push_back(n);
        mp[n]=1;
        solve(n);
        sort(v.begin(),v.end());
        for(int j=v.size()-1;j>0;j--)
        {
            r+=mp[v[j]];
            if(v[j]%2==1)
            {
                mp[v[j]/2]+=2*mp[v[j]];
            }
            else
            {
                mp[v[j]/2]+=mp[v[j]];
                mp[v[j]/2-1]+=mp[v[j]];
            }
            if(r>=k)
            {
                ans=v[j];
                break;
            }
        }
        fout<<"Case #"<<i+1<<": ";
        if(ans%2==1)fout<<ans/2<<" "<<ans/2<<endl;
        else fout<<ans/2<<" "<<ans/2-1<<endl;
    }
    return 0;
}
