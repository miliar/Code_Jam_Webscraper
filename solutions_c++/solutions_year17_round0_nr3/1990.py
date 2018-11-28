#include <iostream>
#include<list>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++){
    unsigned long long int n,k;
    cin>>n>>k;
    while(n>1000 && k>1)
    {
        if(k%2==1 && n%2==0)
        {
            n=n-1;
        }
        else{
        n=n/2;
        k=k/2;
        }

    }
    if(k==1)
    {
         if(n%2==0)
    {
        cout<<"Case #"<<t<<": "<<n/2<<" "<<n/2 -1<<endl;
    }
    else{
        cout<<"Case #"<<t<<": "<<n/2<<" "<<n/2<<endl;
    }
    }
    else{

    long long int arr[n+2]={};
    arr[0]=1;
    long long int z=0;
    long long int ab,prev;
    arr[n+1]=1;
    while(z!=k-1){
    long long int diff=-1;
    long long int beg=0;
    for(long long int i=1;i<n+2;i++)
    {
        if(arr[i]!=0){
        prev=beg;
        beg=i;
        if((beg-prev)>diff)
        {
        diff=beg-prev;
        ab=prev;
        }
        }
    }

    diff=diff/2;
    z++;

    arr[ab+diff]=1;

    }
    long long int ma=-1;
    long long int ct=0;
    for(long long int i=0;i<n+2;i++)
    {

        if(arr[i]==0)
        {
            ct++;
        }
        else{

            if(ct>ma)
            {
                ma=ct;

            }
            ct=0;
        }



    }

    if(ma%2==0)
    {
        cout<<"Case #"<<t<<": "<<ma/2<<" "<<ma/2 -1<<endl;
    }
    else{
        cout<<"Case #"<<t<<": "<<ma/2<<" "<<ma/2<<endl;
    }
    }
    }
    return 0;
}
