#include<iostream>
#include<bits/stdc++.h>

using namespace std;

bool sortf(pair<long int,long int> a, pair<long int,long int> b)
{
    long double k1,s1,k2,s2,t1,t2;
    k1=a.first;
    s1=a.second;
    t1=k1/s1;
    k2=b.first;
    s2=b.second;
    t2=k2/s2;
    if(t1>t2)
        return true;
    else
        return false;

}

int main()
{
    long int t,a,j,k,l,d,n,s;
    double z,x,c,b,ans;
    cin>>t;
    vector<pair<long int,long int> > v;
    for(a=1;a<=t;a++)
    {
        cin>>d>>n;
        for(j=0;j<n;j++)
        {
            cin>>k>>s;
            v.push_back(make_pair(d-k,s));
        }
        sort(v.begin(),v.end(),sortf);
        b=d;
        x=v[0].first;
        c=v[0].second;
        z=x/c;
        ans=b/z;
        cout<<"Case #"<<a<<": ";
        cout<<std::fixed<<std::setprecision(6)<<ans<<endl;
        v.clear();

    }


    return 0;
}
