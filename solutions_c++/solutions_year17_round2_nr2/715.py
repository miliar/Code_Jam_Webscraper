//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

long long keep[100009];
long long ar[100009];
vector<pair<long long,long long> >vec;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    //freopen("out.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    long long i,j,k,l,cnt=0,n,cas,test,flag,now,ans=0,m,pos;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n;
        for(i=1;i<=6;i++) cin>>ar[i];

        vec.clear();
        vec.push_back(make_pair(ar[1],1));
        vec.push_back(make_pair(ar[3],3));
        vec.push_back(make_pair(ar[5],5));

        sort(vec.begin(),vec.end());
        reverse(vec.begin(),vec.end());

        pos=1;
        for(i=0;i<3;i++)
        {
            for(j=0;j<vec[i].first;j++)
            {
                if(vec[i].second==1) keep[pos]='R';
                if(vec[i].second==3) keep[pos]='Y';
                if(vec[i].second==5) keep[pos]='B';
                pos+=2;
                if(pos>n) pos=2;
            }
        }

        flag=1;
        for(i=1;i<=n;i++) if(keep[i]==keep[i-1]) flag=0;
        if(keep[1]==keep[n]) flag=0;

        if(flag)
        {
            printf("Case #%lld: ",cas);
            for(i=1;i<=n;i++) printf("%c",keep[i]);
            cout<<endl;
        }
        else printf("Case #%lld: IMPOSSIBLE\n",cas);

    }



}
