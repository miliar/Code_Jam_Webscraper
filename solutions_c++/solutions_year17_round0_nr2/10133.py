#include<iostream>
//#include<stdlib.h>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
    int t;
    int n,x,i,cnt,ans;
    int arr[1000];
   // cout<<"enter t";
    cin>>t;
    for(int c=1;c<=t;c++)
    {
        int num;
        cin>>num;
        int org=num+1;
        while(org--)
        {
            num=org;

            n=0;
            while(num!=0)
            {
            x=num%10;
            arr[n]=x;
            n++;
            num=num/10;
            }
        if(n==1)
        {
            ans=org;
            goto abc;
        }
        cnt=0;
        for(i=n-1;i>0;i--)
        {
            if(arr[i]>arr[i-1])
            {
                //cout<<"break";
                break;
            }
            else
            {
                cnt++;
            }
            if(cnt==(n-1))
            {
                ans=org;
                goto abc;
            }
        }
        }
        abc:
            cout<<"Case #"<<c<<": "<<ans<<endl;
    }

}
