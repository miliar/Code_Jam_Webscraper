//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

int ar[109];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int i,j,k,l,n,cas,test,flag,temp,now,ans=0,p,r,s,pos,m;


    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n>>m;
        memset(ar,0,sizeof(ar));

        pos=0;
        ans=0;

        for(i=1;i<=n;i++)
        {
            cin>>j;
            ar[j%m]++;
        }

        if(m==1) ans=n;
        else if(m==2) ans=ar[0]+(ar[1]+1)/2;
        else if(m==3) ans=ar[0]+min(ar[1],ar[2])+(max(ar[1],ar[2])-min(ar[1],ar[2])+2)/3;
        else
        {
            temp=min(ar[1],ar[3]);
            ans=ar[0]+min(ar[1],ar[3])+ar[2]/2;
            ar[2]%=2;
            ar[1]-=temp;
            ar[3]-=temp;
            if(ar[2])
            {
                temp=max(ar[1],ar[3]);

                if(temp>2)
                {
                    temp-=2;
                    ans++;
                    ans+=(temp+3)/4;
                }
                else ans++;
            }
            else ans+=(max(ar[1],ar[3])+3)/4;
        }


        printf("Case #%d: %d\n",cas,ans);



    }



}
