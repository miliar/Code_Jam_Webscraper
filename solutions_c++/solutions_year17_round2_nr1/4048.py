#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    int ka=0;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        double d;
        int n;
        cin>>d>>n;
        printf("Case #%d: ",++ka);
        if(n==1)
        {
            double k1,s1;
            cin>>k1>>s1;
            double q=(d-k1)/s1;
            printf("%.6f\n",d/q);
        }
        else if(n==2)
        {
            double k1,s1,k2,s2;
            cin>>k1>>s1>>k2>>s2;
            if(k1<k2)swap(k1,k2),swap(s1,s2);
            if(s2<=s1)
            {
                double q=(d-k2)/s2;
                printf("%.6f\n",d/q);
            }
            else{
                double tt=(k1-k2)/(s2-s1);
                double z;
                if(k1+tt*s1<d){
                z=(d-k1-tt*s1)/min(s1,s2);
                printf("%.6f\n",d/(tt+z));
                }
                else{
                z=(d-k2)/s2;
                printf("%.6f\n",d/z);
                }
            }
        }
    }
    return 0;
}
