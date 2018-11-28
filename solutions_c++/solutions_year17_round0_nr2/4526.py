#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,n,no=0;
    freopen("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    scanf("%lld",&t);
    while(t--)
    {
        no++;
        long long int x=0,a[30],n,j,i,tot,f=0,k;
        scanf("%lld",&n);
        while(n)
        a[x++]=n%10,n/=10;
        tot=x;
        for(i=x-2;i>=0;i--)
        if(a[i]<a[i+1])
        {
            j=i+1;
            if(a[j]==1)
            {
                f=1;
                break;
            }

            while(j<x && a[j]==a[i+1])
            {
                if(a[j]!=a[i+1])
                break;
                j++;
            }
            if(j==x)
            {
                a[x-1]-=1;
                for(k=x-2;k>=0;k--)
                a[k]=9;
            }
            else
            {
                a[j-1]-=1;
                for(k=j-2;k>=0;k--)
                a[k]=9;
            }


        }
        printf("Case #%d: ",no);
        if(f)
        {
            tot--;
            for(i=0;i<tot;i++)
            printf("9");
            printf("\n");
        }
        else
        {
            for(i=tot-1;i>=0;i--)
            printf("%lld",a[i]);
            printf("\n");
        }


    }

}

