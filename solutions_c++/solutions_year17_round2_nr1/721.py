//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

long long D[100009];
long long S[100009];
double EPS  = 1e-9;

int main()
{
    //freopen("A-large.in","r",stdin);
    freopen("out.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    long long i,j,k,l,cnt=0,n,cas,test,flag,now,ans=0,m;
    double lo,mid,hi,temp;
    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>m>>n;
        for(i=1;i<=n;i++)
        {
            cin>>D[i]>>S[i];
        }

        lo=0;
        hi=0;
        for(i=1;i<=n;i++) hi=max(hi,m*1.0/((m*1.0-D[i])/S[i]));
        //hi=1e20;
        cnt=0;

        while(++cnt<=100)
        {
            mid=lo+hi;
            mid/=2;

            temp=1e20;
            for(i=1;i<=n;i++)
            {
                if(mid<S[i]) continue;
                if(fabs(mid-S[i])<=EPS) continue;
                temp=min(temp,(1.0*D[i])/(mid-S[i]));
            }

            temp*=mid;

            //cout<<mid<<" "<<temp<<endl;

            if(temp>m || fabs(temp-m)<=EPS) lo=mid;
            else hi=mid;
        }

        //cout<<mid<<endl;

        printf("Case #%d: ",cas);
        cout<<fixed<<setprecision(10)<<mid<<endl;
    }



}
