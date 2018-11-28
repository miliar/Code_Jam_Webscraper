#include<bits/stdc++.h>
using namespace std;
int main()
{

    int t,j=0;
    scanf("%d",&t);
    while(t--)
    {j++;
        long long int n,k,a;
        double m,min1=0.0,b;
        cin>>n>>k;
        for(int i=0;i<k;i++)
        {
            cin>>a>>b;
            m=(n-a)/b;
            //cout<<m;
            if(i!=0)
            {if(m>min1)
            min1=m;
            }
            else
            min1=m;
        }
        min1=n/min1;
        cout<<"Case #"<<j<<": ";
            printf("%.6f",min1);
            printf("\n");
    }
}
