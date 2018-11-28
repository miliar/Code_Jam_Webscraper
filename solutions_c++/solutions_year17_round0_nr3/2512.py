//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

set<pair<long long,long long> >sett;
map<long long,long long>mymap;
std::set<pair<long long,long long> >::iterator it;

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    long long i,j,k,l,n,cas,test,a,b,c,d,flag,temp,now,ans=0,m,anss;
    pair<long long,long long>  NOW;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n>>m;

        mymap.clear();
        sett.clear();

        sett.insert(make_pair(-n,1));

        for(i=0;i<m;)
        {
            it=sett.begin();
            NOW=*it;
            a=-NOW.first;
            b=NOW.second;

            i+=b;
            sett.erase(it);

            c=mymap[(a-1)/2];
            d=mymap[(a)/2];

            sett.erase(make_pair(-((a-1)/2),c));
            sett.erase(make_pair(-((a)/2),d));

            mymap[(a-1)/2]+=b;
            mymap[(a)/2]+=b;

            sett.insert(make_pair(-((a-1)/2),mymap[((a-1)/2)]));
            sett.insert(make_pair(-((a)/2),mymap[((a)/2)]));

            ans=(a-1)/2;
            anss=a/2;
        }

        printf("Case #%lld: %lld %lld\n",cas,anss,ans);
    }
}
