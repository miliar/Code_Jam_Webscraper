#include<iostream>
#include<stdio.h>
using namespace std;
int L(int);
int main()
    {
        long long int j,i,n,k,b[100000],T;k=0;
        cin>>T;
        for(j=1;j<=T;j++)
    {
        cin>>n;
        i=1;
        for( ;i<=n; )
        {
            if(L(i)==1)
                b[++k]=i++;
            else
            {
               i++;
                continue;
            }
        }
        cout<<"Case #"<<j<<": "<<b[k];
        cout<<"\n";
    }
        return 0;
    }

int L(int n1)
{
    int i,j,n,k,c,a[10],b[10],d;d=i=k=c=j=0;
     n=n1;
    if(n%10==n)
    {
        return 1;
    }
    else
    {
    while(n!=0)
    {
        d=n%10;
        a[++i]=d;
        ++c;
        n=n/10;
        }
     while(i!=0)
     {
         b[++j]=a[i];
         i--;
     }
         while((b[j]-b[j-1])>=1)
            {
            j=j-1;
            }
            //cout<<"\n"<<i<<" ";
          while((b[c]-b[c-1])>=0)
          {
              c=c-1;
              k++;
          }
     if(j==1||(c==1&&k>=1))
        return 1;
        else
        return 0;
    }
}
