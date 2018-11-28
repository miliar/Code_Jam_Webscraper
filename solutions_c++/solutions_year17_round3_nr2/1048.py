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
#define f first
#define s second
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
#define int long long
using namespace std;
pii c[102],j[102];
main()
{
    //freopen("data.txt","r",stdin);
    //freopen("data2.in","r",stdin);
    //freopen("out3.txt","w",stdout);
    int t,l1=0;
    cin>>t;
    while(t--)
    {
        l1++;
        int n,m,i,k,l;
        int ac,aj;
        cin>>ac>>aj;
        for(i=0;i<ac;i++)
        {
            cin>>c[i].f>>c[i].s;
        }
        for(i=0;i<aj;i++)
        {
            cin>>j[i].f>>j[i].s;
        }
        int ans=0;
        if((ac+aj<=1)||(ac==1&&aj==1))
        {
            ans=2;
        }
        else if(ac==0)
        {
            c[0]=j[0];
            c[1]=j[1];
            aj=0;
            ac=2;
        }
        if(!ans)
        {
            sort(c,c+2);
            if((c[0].f+1440-c[1].s>=720)||(c[1].f-c[0].s)>=720)
                ans=2;
            else
            {
                ans=4;
            }
        }
        cout<<"Case #"<<l1<<": "<<ans<<"\n";
    }
    return 0;
}
