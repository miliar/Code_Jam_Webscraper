#include<bits/stdc++.h>
using namespace std;
#define ll long long
multiset<int> s;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,n,k,i,j,ma,mi;
    cin>>t;
    for(ll te=1;te<=t;te++)
    {
        cin>>n>>k;
        s.clear();
        s.insert(n);
        while(k--)
        {
           int j=*s.rbegin();
           s.erase(s.find(j));
           ma=j/2;
           if(j&1)
           mi=j/2;
           else
            mi=j/2-1;
           s.insert(ma);
           s.insert(mi);
        }
        cout<<"Case #"<<te<<": "<<ma<<" "<<mi<<endl;
    }
    return 0;
}
