#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,e;
//ofstream outFile;

//outFile.open("output11.txt");
    scanf("%d",&t);
    for(e=1;e<=t;e++)
    {
        long long int n,c;
        scanf("%lld",&n);
        c=n;
        int co,m,d,i=1,j,l=0;
        int a[30];
        while(n!=0)
        {
            n=n/10;
            l++;
        }

        if(l==1)
        {
           // outFile<<"Case #"<<e<<": "<<c<<"\n";
            printf("Case #%d: %lld\n",e,c);
            continue;
        }

        co=1;
        n=c;
        i=l;
        while(n!=0)
        {

            a[i]=(long long)n%10;
            n=n/10;
            i--;

        }

        n=c;
        m=a[1];
        for(j=2;j<=l;j++)
        {
           d=a[j];
           co++;
           if(d<m)
           {
               break;
           }
           m=d;
        }
        if(j==(l+1))
        {
            // outFile<<"Case #"<<e<<": "<<c<<"\n";
           printf("Case #%d: %lld\n",e,c);
           continue;
        }
        co--;

        for(i=co;i>=1;i--)
        {
            a[i]=a[i]-1;
        if(i>=2)
        {

            if(a[i]>=a[i-1])
            {

                break;
            }
        }

        }

if(i==0)
    i=1;

         printf("Case #%d: ",e);
        //  outFile<<"Case #"<<e<<": ";
         for(j=1;j<=i;j++)
         {
             if(j==1&&a[j]==0)
                continue;
            printf("%d",a[j]);
           // outFile<<a[j];
         }

         for(j=i+1;j<=l;j++)
         {
           // outFile<<"9";
            printf("9");
         }
         // outFile<<"\n";
         printf("\n");

}
return(0);
}

