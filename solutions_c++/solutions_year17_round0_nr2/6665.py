#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long T,cnt=1;
    cin>>T;
    long long arr[20];
    while(T--)
    {
        long long pos=-1,i=0,n,flag=0,n1;
        cin>>n;
        n1=n;
        while(n)
        {
            arr[i++]=n%10;
            n=n/10;
        }
        /*for(int j=0;j<i;j++)
            cout<<arr[j]<<" ";
        cout<<endl;*/
        long long count=1,k=1;
        for(long long j=0;j<(i-1);j++)
        {
           if(arr[j]<=arr[j+1])
           {
               pos=j+1;
           }
           if(arr[j]>=arr[j+1])
            k++;
           if(arr[j]==arr[j+1])
               count++;
        }
        //cout<<count<<"  "<<i<<endl;
        cout<<"Case #"<<cnt<<":"<<" ";
        if(i==count || i==k){
         cout<<n1;
         flag=1;
        }
        for(long long j=(i-1);j>=0 ;j--)
        {
            if(flag==1)
                break;
           /* if(i==1){
                cout<<arr[j];
                break;
            }*/
            if(j==pos)
            {
                if((arr[j]-1))
                    cout<<arr[j]-1;
            }
            else if(j<pos)
            {
                cout<<"9";
            }
            else
            {
                cout<<arr[j];
            }
        }
        cout<<endl;
        cnt++;
    }
    return 0;
}
