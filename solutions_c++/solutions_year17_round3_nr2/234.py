#include <bits/stdc++.h>
using namespace std;
bool cw[3000];
bool cj[3000];
int sc[3000][2];
int tp[3000][2];
int main()
{
    freopen("B.in","r",stdin);
    freopen("B4.out","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        for(int i=0;i<=2500;i++)
            cw[i]=1,cj[i]=1,sc[i][0]=1000000,sc[i][1]=1000000;
        int ac,aj,an=10000000;
        cin>>ac>>aj;
        for(int i=1;i<=ac;i++)
        {
            int b,e;
            cin>>b>>e;
            b++,e++;
            for(int j=b;j<e;j++)
                cw[j]=0;
        }
        for(int j=1;j<=aj;j++)
        {
            int b,e;
            cin>>b>>e;
            b++,e++;
            for(int j=b;j<e;j++)
                cj[j]=0;
        }
        sc[0][0]=0;
        sc[0][1]=10000000;
        for(int j=1;j<=1440;j++)
        {
            if(cw[j]==0)
                tp[0][0]=10000000;
            if(cj[j]==0)
                tp[0][1]=10000000;
            for(int k=0;k<=720;k++)
            {
                if(cw[j])
                    tp[k+1][0]=min(sc[k][0],sc[k][1]+1);
                else
                    tp[k+1][0]=100000000;
                if(cj[j])
                    tp[k][1]=min(sc[k][1],sc[k][0]+1);
                else
                    tp[k][1]=100000000;
            }
            for(int k=0;k<=720;k++)
                sc[k][0]=tp[k][0],sc[k][1]=tp[k][1];
        }
        an=min(sc[720][1]+1,sc[720][0]);
        for(int j=1;j<=2500;j++)
            sc[j][0]=1000000,sc[j][1]=1000000;
        sc[0][0]=10000000;
        sc[0][1]=0;
        for(int j=1;j<=1440;j++)
        {
            if(cw[j]==0)
                tp[0][0]=10000000;
            if(cj[j]==0)
                tp[0][1]=10000000;
            for(int k=0;k<=720;k++)
            {
                if(cw[j])
                    tp[k+1][0]=min(sc[k][0],sc[k][1]+1);
                else
                    tp[k+1][0]=100000000;
                if(cj[j])
                    tp[k][1]=min(sc[k][1],sc[k][0]+1);
                else
                    tp[k][1]=100000000;
            }
            for(int k=0;k<=720;k++)
                sc[k][0]=tp[k][0],sc[k][1]=tp[k][1];
        }
        an=min(min(an,sc[720][1]),sc[720][0]+1);
        printf("Case #%d: %d\n",tt,an);
    }
}
