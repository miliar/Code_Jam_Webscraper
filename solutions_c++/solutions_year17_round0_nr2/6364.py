#include <bits/stdc++.h>
#define lli long long int
using namespace std;
int main()
{
    lli T,i=1;
    cin>>T;
    while(i<=T)
    {
        lli n,no,j=0,k=0;
        lli a[18];
        memset(a,0,sizeof(a));
        cin>>n;
        no=n;
        while(n!=0)
        {
            a[j]=n%10;
            n=n/10;
            j++;
        }
        while(k<j-1)
        {
            if(a[k]<a[k+1])
            {
                for(lli l=k;l>=0;l--)
                {
                    a[l]=9;
                }
                a[k+1]=a[k+1]-1;
            }
            k++;
        }
        cout<<"Case #"<<i<<": ";
        for(lli m=j-1;m>=0;m--)
        {
            if(a[m]==0&&m==j-1)
            {
                continue;
            }
            else
            cout<<a[m];
        }
        cout<<endl;
        i++;
    }
}
