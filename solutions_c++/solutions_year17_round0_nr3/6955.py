#include<bits/stdc++.h>
using namespace std;
long long arr[100];
int ind=0;
void pre()
    {
    arr[0]=1;
    ind=1;
     while(1)
         {
         if(arr[ind-1]>=1e18||arr[ind-1]<0)
             break;
         arr[ind]=arr[ind-1]*2;
         ind++;
     }
    arr[ind-1]=0;
}
int main()
    {
    pre();
    long long n,t,i,j,k;
    cin>>t;
    int r=1;
    while(t--)
        {
        cin>>n>>k;
        int x=0;
        if(k==1)
            {
            cout<<"Case #"<<r<<": "<<n/2<<" "<<(n-1)/2<<"\n";
            r++;
            continue;
        }
        while(k>=arr[x])
            {
            x++;
        }
        long long y=arr[x-1];
        //cout<<y;
       // cout<<y<<"\n";
       n-=k;
        long long q=n/y;
        //cout<<q;
        cout<<"Case #"<<r<<": "<<ceil(q/2.0)<<" "<<q/2<<"\n";
        r++;
    }
}
