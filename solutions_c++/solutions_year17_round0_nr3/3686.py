#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t=0;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        long long n,k,mn,mx;
        cin>>n>>k;
        map<long long,long long> m;
        m[n]++;
        while(k>0)
        {
            map<long long,long long>::iterator it=m.end();
            it--;
            long long val=it->first;
            mn=(val-1)/2;
            mx=val/2;
            m[mn]+=it->second;
            m[mx]+=it->second;
            k-=it->second;
            m.erase(it);
        }
        cout<<"Case #"<<tc<<": "<<mx<<" "<<mn<<endl;
    }
}