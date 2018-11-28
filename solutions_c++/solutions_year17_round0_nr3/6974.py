#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int loc;
    int mi[t],ma[t];
    for(int i=0;i<t;i++)
    {
        int n,k;
        cin>>n>>k;
        int l[n+1],r[n+1],a[n+2],min1[n+1],max33[n+1];

        a[0]=0;
        a[n+1]=0;
        for(int j=1;j<n+1;j++)
        {
            a[j]=-1;
            l[j]=r[j]=0;
        }
        for(int uu=0;uu<k;uu++)
        {
        for(int j=1;j<n+1;j++)
        {
            l[j]=r[j]=0;
        }
        for(int j=1;j<n+1;j++)
        {
            for(int k=j;k>=1&&a[j]==-1&&a[k]==-1;k--)
            {
                l[j]=l[j]+1;
            }
            for(int k=j;k<=n+1&&a[j]==-1&&a[k]==-1;k++)
            {
                r[j]=r[j]+1;
            }
            if(l[j]>r[j])
            {
                min1[j]=r[j];
                max33[j]=l[j];
            }
            else
            {
                min1[j]=l[j];
                max33[j]=r[j];
            }
        }
        int max3=min1[1];
            for(int ii=2;ii<n+1;ii++)
            {
                if(max3<min1[ii])
                {
                    max3=min1[ii];
                }
            }
            int clash[n];
            int ko=0;
            for(int ii=1;ii<n+1;ii++)
            {
                if(max3==min1[ii])
                {
                    clash[ko]=ii;
                    ko++;
                }
            }
            loc=clash[0];
            if(ko==1)
            {
                a[clash[0]]=0;
                continue;
            }
            else
            {
                int r=0;
                loc=clash[r];
                max3=max33[clash[r]];
                for(r=1;r<ko;r++)
                {
                     if(max3<max33[clash[r]])
                     {
                         max3=max33[clash[r]];
                         loc=clash[r];
                     }
                }
                a[loc]=0;
            }
        }
            l[loc]=r[loc]=0;
            for(int k=loc-1;k>=1&&a[k]==-1;k--)
            {
                l[loc]=l[loc]+1;
            }
            for(int k=loc+1;k<=n+1&&a[k]==-1;k++)
            {
                r[loc]=r[loc]+1;
            }
            if(l[loc]>r[loc])
            {
                min1[loc]=r[loc];
                max33[loc]=l[loc];
            }
            else
            {
                min1[loc]=l[loc];
                max33[loc]=r[loc];
            }
            ma[i]=max33[loc];
            mi[i]=min1[loc];
    }
    for(int i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": "<<ma[i]<<" "<<mi[i]<<"\n";
    }
return 0;
}
