#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<iomanip>
#include<map>
#define ll long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
#define int long long
using namespace std;
int pos[10004],speed[10004];
double tim[10004];
main()
{
    //freopen("data3.in","r",stdin);
    //freopen("data.txt","r",stdin);
    //freopen("out3.txt","w",stdout);
    int t,l1=0;
    cin>>t;
    while(t--)
    {
        l1++;
        int n,m,i,j,k,l,d;
        cin>>d>>n;
        for(i=0;i<n;i++)
        {
            cin>>pos[i]>>speed[i];
        }
        /*time[n-1]=(1.0*d-pos[n-1])/speed[n-1]*1.0;
        double sr=1.0*speed[n-2]/speed[n-1]*1.0
        sr-=1.0;
        /// they were already met
        double dd=pos[n-1]-pos[n-2];
        double x2=dd/sr;
        for(i=n-1;i>=0;i--)
        {
            time[i]=
        }*/
        double mt=0;
        for(i=0;i<n;i++)
        {
            tim[i]=(d*1.0-1.0*pos[i])/speed[i]*1.0;
            if(mt<tim[i])
                mt=tim[i];
        }
        cout<<"Case #"<<l1<<": ";
        cout<<setprecision(12)<<d*1.0/mt*1.0<<"\n";
    }
    return 0;
}
