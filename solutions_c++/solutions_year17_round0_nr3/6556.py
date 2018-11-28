#include<stdlib.h>
#include<iostream>
#include<string.h>

using namespace std;

void calcRange(long long int n,long long int *left,long long int *right,bool*flg)
{
    long long int i,maxCount=0,count=0,l,r;
    for(i=1;i<=n;i++)
    {
        if(flg[i]==false)
        {
            if(count==0)
                l=i;
            count++;
        }
        else
        {
            r=i-1;
            if(count>maxCount)
            {
                *left=l;
                *right=r;
                maxCount=count;
            }
            count=0;
        }
    }
    if(count>maxCount)
    {
        *left=l;
        *right=n;
        maxCount=count;
    }
}

int main()
{
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        long long int n,k,max=0,min=0,left,right,j;
        cin>>n>>k;
        /*if(n==k)
        {
            cout<<"Case #"<<i<<": "<<0<<" "<<0<<endl;
            continue;
        }*/
        bool flg[n+1]={false};

        for(j=0;j<k;j++)
        {
            calcRange(n,&left,&right,flg);
            long long int no=right-left+1,mid;
            if(no%2==0)
                mid=left+no/2-1;
            else
                mid=left+no/2;
            flg[mid]=true;
            max=right-mid;
            min=mid-left;
        }
        cout<<"Case #"<<i<<": "<<max<<" "<<min<<endl;
    }
}
