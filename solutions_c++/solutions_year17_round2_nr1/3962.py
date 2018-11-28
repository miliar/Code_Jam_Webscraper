#include<bits/stdc++.h> // akash231997
using namespace std;

    int main()
    {

        int a=1;
        int t;
        scanf("%d",&t);
        while(t--)
        {
            long long int d,i;
            double n,m=0;
             cin>>d>>n;
            for(i=0;i<n;i++)
            {
                long long a;
                 double b;
                 cin>>a>>b;
                m=max(m,(d-a)/b);
            }
            double p=d/m;
            printf("Case #%d: %0.6f\n",a,p);
            a++;
        }
        return 0;
    }
