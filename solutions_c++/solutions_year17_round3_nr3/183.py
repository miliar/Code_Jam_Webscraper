#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<cmath>
#include<cstring>
using namespace std;
int n,k;
int main()
{
    freopen("C-small-1.in","r",stdin);
    freopen("C-small-1.out","w",stdout);
    int T, cas=0;scanf("%d",&T);
    while(T--)
    {
        double u;
        double p[60];
        scanf("%d%d",&n,&k);
        cin>>u;
        for(int i=0;i<n;i++) cin>>p[i];

        while(u>0)
        {
            sort(p,p+n);
            p[n]=1;
            double small=p[0];
            if(small==1)
            break;
            int j=0;
            for(j=0;j<=n;j++)
            {
                if(j==n) break;
                if(p[j]>small) break;
            }
            int len=j;
            double ma=p[j]-small;
            if(ma*len <u)
            {
                for(int k=0;k<j;k++) p[k]+=ma;
                u-=ma*len;
            }
            else
            {
                for(int k=0;k<j;k++) p[k] +=u/len;
                u=0;
            }
        }
        double pp=1;
        for(int i=0;i<n;i++) pp*=p[i];
        printf("Case #%d: %.8f\n", ++cas, pp);

    }
}
