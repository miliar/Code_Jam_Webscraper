#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long i,j,k,m,t;
    cin>>t;
    long long n,a[100],c=1;
    while(t--)
    {
        cin>>n;
        while(n)
        {
            m=n;
            i=0;
            k=0;
            while(m)
            {
                a[i]=m%10;
                m=m/10;
                if(i)
                {
                    if(a[i]>a[i-1])
                    {
                        k=1;
                        break;
                    }
                }
                i++;
            }
            if(k==0)
            {
                break;
            }
            n--;
        }
        cout<<"Case #"<<c++<<": "<<n<<endl;
    }
}
