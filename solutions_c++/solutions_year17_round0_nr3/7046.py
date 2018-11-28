#include<iostream>
#include<stdio.h>

using namespace std;

#define mil 4000

void calc(bool *occupied,int n,int *maxlr,int *minlr,int i)
{
    int l=0;
    int r=0;
    int k=i+1;
    while(!occupied[k])
    {
        r++;
        k++;
    }
    k=i-1;
    while(!occupied[k])
    {
        l++;
        k--;
    }
    maxlr[i]=max(l,r);
    minlr[i]=min(l,r);
}

void enter(bool *occupied,int n,int *maxlr,int *minlr)
{
    for(int i=1;i<=n;i++)
        calc(occupied,n,maxlr,minlr,i);



    bool flag=0;
    bool flag1=1;
    int maximal;int pos;
    int maximal2;

    for(int i=1;i<=n;i++)
    { if(!occupied[i])
       {
        if(flag1)
            {
                maximal=minlr[i];pos=i;
                flag1=0;
            }
        else
       {
           if(minlr[i]>maximal)
         {
            maximal=minlr[i];
            pos=i;
            flag=0;
         }
         else if(minlr[i]==maximal)
            {flag=1;
            }
       }
       }
    }
    if(flag==1)
    {
        flag1=1;
        for(int i=1;i<=n;i++)
           if(!occupied[i])
           {

           if(minlr[i]==maximal)
        {
            if(flag1)
            {
                maximal2=maxlr[i];
                pos=i;
                flag1=0;
            }
            else if(maxlr[i]>maximal2)
            {
                maximal2=maxlr[i];
                pos=i;
            }
        }
        }
    }


        occupied[pos]=1;
        maxlr[0]=maxlr[pos];
        minlr[0]=minlr[pos];
}

int main()
{
    freopen("C-small-1-attempt0 (1).in","r",stdin);
    freopen("C-small-1-attempt-output-0.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {


    bool occupied[mil]={0};
    int n,k;
    int maxlr[mil]={0};
    int minlr[mil]={0};

    cin>>n>>k;
    occupied[0]=1;occupied[n+1]=1;
   while(k--)
    {
        enter(occupied,n,maxlr,minlr);

    }
   cout<<"Case #"<<i<<": "<<maxlr[0]<<' '<<minlr[0]<<endl;;
    }
    return 0;
}
