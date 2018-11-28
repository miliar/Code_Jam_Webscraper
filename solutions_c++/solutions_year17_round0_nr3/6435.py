#include<bits/stdc++.h>
using namespace std;
map <long long,long long > mp;
int main()
{
    int q;
    cin>>q;
    for(int i=1;i<=q;i++)
    {
        long long n,k;
        long long ans;
        cin>>n>>k;
        mp[n]++;
        while(k>0)
        {
            map<long long ,long long>::iterator it=mp.end();
            it--;
            mp[(it->first-1)/2]+=it->second;
            mp[(it->first-1)/2+(it->first-1)%2]+=it->second;
            ans=it->first;
            k-=it->second;
            mp.erase(it);
        }
        ans--;
        printf("Case #%d: %lld %lld\n",i,(ans/2+ans%2),ans/2);
        mp.clear();
    }
}
