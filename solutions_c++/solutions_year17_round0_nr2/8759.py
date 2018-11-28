#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        long long i,n,ci,a,k;
        cin>>n;
        for(i=n;i>=1;i--)
        {
            if(i%10==i)
                break;
            int temp[200],k=0;
            ci=i;
            while(ci)
            {
                temp[k++]=ci%10;
                ci=ci/10;
            }
            for(a=1;a<k;a++)
                if(temp[a]>temp[a-1])
                    break;
            if(a==k)
                break;
        }
        cout<<"Case #"<<j<<": "<<i<<endl;
    }
    return 0;
}


