#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#define ll long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
#define int long long
using namespace std;
main()
{
    //freopen("data.txt","r",stdin);
    //freopen("data4.in","r",stdin);
    //freopen("out4.txt","w",stdout);
    int t,l1=0;
    cin>>t;
    while(t--)
    {
        l1++;
        cout<<"Case #"<<l1<<": ";
        int n,m,i,j,k,l,r,y,b,o,g,v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        pair<int,char> col[]={mp(r,'R'),mp(y,'Y'),mp(b,'B')};
        sort(col,col+3);
        if(col[2].first>(col[0].first+col[1].first))
        {
            cout<<"IMPOSSIBLE\n";
            continue;
        }
        int both=col[0].first+col[1].first-col[2].first;
        //string boths="";
        //boths+=col[0].second;
        //boths+=col[1].second;
        int only0=col[0].first-both;
        int only1=col[1].first-both;
        //string only0s="",only1s="";
        //only0s+=col[0].second;
        //only1s+=col[1].second;
        //string maxs="";
        //maxs+=col[2].second;
        i=0;
        string ans="";
        j=0;
        while(i<n)
        {
            if(j%2==0)
            {
                ans.pb(col[2].second);
            }
            else if(both)
            {
                ans.pb(col[0].second);
                ans.pb(col[1].second);
                i++;
                both--;
            }
            else if(only0)
            {
                ans.pb(col[0].second);
                only0--;
            }
            else if(only1)
            {
                ans.pb(col[1].second);
                only1--;
            }
            i++;
            j++;
        }
        cout<<ans<<"\n";
    }
    return 0;
}
