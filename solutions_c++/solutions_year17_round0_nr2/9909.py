#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    freopen("x.in","r",stdin);
    freopen("y.txt","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;++k)
    {
        ll n,temp;
        cin>>n;
        while(1)
        {
            temp=n;
            int save=temp%10;
            temp/=10;
            while(temp!=0)
            {
                int r=temp%10;
                if(save<r)
                {
                    break;
                }
                save=r;
                temp/=10;
            }
            if(temp!=0)
                n=n-1;
            else
            {
                cout<<"Case #"<<k<<": "<<n<<"\n";
                break;
            }
        }
    }
    return 0;
}
