#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("ll.in","r",stdin);
    freopen("2nd.out","w",stdout);
    long long int n,a,b,c,d,i;
    int t;bool val=true;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        cin>>n;
        for(i=n;i>0;i--)
        {
            a=i;
            d=-1;
            val=true;
            while(a!=0)
            {
                c=a%10;
                a=a/10;
                if(d==-1||d>=c)
                {
                    d=c;
                }
                else{val=false;break;}

            }
            if(val){cout<<"Case #"<<z<<": "<<i<<"\n";break;}
        }
    }
}
