#include<bits/stdc++.h>
using namespace std;
int  n,t,cs=1;
bool v[1006];
int a[10];
int main()
{
    int i,j,k,l;
    n=1001;
    for(i=0;i<=n;i++)
    {
        if(i<10)
            v[i]=1;
        else
        {
           l=0;
            j=i;

            while(j>0)
            {
                a[l++]=j%10;
                j/=10;
            }

            sort(a,a+l);
            j=0;
            k=0;
            while(j<l)
            {
                k*=10;
                k+=a[j];
                j++;
            }
            if(k<1006)
            v[k]=1;
        }
    }
    freopen("ot.txt","w",stdout);
    freopen("in.txt","r",stdin);
    cin>>t;
    while(t--)
    {
        cin>>n;
        cout<<"Case #"<<cs++<<": ";
        for(i=n;i>=0;i--)
        {
            if(v[i]==1)
            {
                cout<<i<<endl;
                break;
            }
        }
    }

}
